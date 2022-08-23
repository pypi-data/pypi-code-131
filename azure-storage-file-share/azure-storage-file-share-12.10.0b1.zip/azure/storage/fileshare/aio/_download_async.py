# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
# pylint: disable=invalid-overridden-method
import asyncio
import sys
import warnings
from io import BytesIO
from itertools import islice
from typing import AsyncIterator

from azure.core.exceptions import HttpResponseError, ResourceModifiedError
from .._download import _ChunkDownloader
from .._shared.request_handlers import validate_and_format_range_headers
from .._shared.response_handlers import process_storage_error, parse_length_from_content_range


async def process_content(data):
    if data is None:
        raise ValueError("Response cannot be None.")

    try:
        return data.response.body()
    except Exception as error:
        raise HttpResponseError(message="Download stream interrupted.", response=data.response, error=error)


class _AsyncChunkDownloader(_ChunkDownloader):
    def __init__(self, **kwargs):
        super(_AsyncChunkDownloader, self).__init__(**kwargs)
        self.stream_lock = asyncio.Lock() if kwargs.get('parallel') else None
        self.progress_lock = asyncio.Lock() if kwargs.get('parallel') else None

    async def process_chunk(self, chunk_start):
        chunk_start, chunk_end = self._calculate_range(chunk_start)
        chunk_data = await self._download_chunk(chunk_start, chunk_end - 1)
        length = chunk_end - chunk_start
        if length > 0:
            await self._write_to_stream(chunk_data, chunk_start)
            await self._update_progress(length)

    async def yield_chunk(self, chunk_start):
        chunk_start, chunk_end = self._calculate_range(chunk_start)
        return await self._download_chunk(chunk_start, chunk_end - 1)

    async def _update_progress(self, length):
        if self.progress_lock:
            async with self.progress_lock:  # pylint: disable=not-async-context-manager
                self.progress_total += length
        else:
            self.progress_total += length

        if self.progress_hook:
            await self.progress_hook(self.progress_total, self.total_size)

    async def _write_to_stream(self, chunk_data, chunk_start):
        if self.stream_lock:
            async with self.stream_lock:  # pylint: disable=not-async-context-manager
                self.stream.seek(self.stream_start + (chunk_start - self.start_index))
                self.stream.write(chunk_data)
        else:
            self.stream.write(chunk_data)

    async def _download_chunk(self, chunk_start, chunk_end):
        range_header, range_validation = validate_and_format_range_headers(
            chunk_start,
            chunk_end,
            check_content_md5=self.validate_content
        )
        try:
            _, response = await self.client.download(
                range=range_header,
                range_get_content_md5=range_validation,
                validate_content=self.validate_content,
                data_stream_total=self.total_size,
                download_stream_current=self.progress_total,
                **self.request_options
            )
            if response.properties.etag != self.etag:
                raise ResourceModifiedError(message="The file has been modified while downloading.")
        except HttpResponseError as error:
            process_storage_error(error)

        chunk_data = await process_content(response)
        return chunk_data


class _AsyncChunkIterator(object):
    """Async iterator for chunks in blob download stream."""

    def __init__(self, size, content, downloader, chunk_size):
        self.size = size
        self._chunk_size = chunk_size
        self._current_content = content
        self._iter_downloader = downloader
        self._iter_chunks = None
        self._complete = (size == 0)

    def __len__(self):
        return self.size

    def __iter__(self):
        raise TypeError("Async stream must be iterated asynchronously.")

    def __aiter__(self):
        return self

    async def __anext__(self):
        """Iterate through responses."""
        if self._complete:
            raise StopAsyncIteration("Download complete")
        if not self._iter_downloader:
            # cut the data obtained from initial GET into chunks
            if len(self._current_content) > self._chunk_size:
                return self._get_chunk_data()
            self._complete = True
            return self._current_content

        if not self._iter_chunks:
            self._iter_chunks = self._iter_downloader.get_chunk_offsets()

        # initial GET result still has more than _chunk_size bytes of data
        if len(self._current_content) >= self._chunk_size:
            return self._get_chunk_data()

        try:
            chunk = next(self._iter_chunks)
            self._current_content += await self._iter_downloader.yield_chunk(chunk)
        except StopIteration:
            self._complete = True
            # it's likely that there some data left in self._current_content
            if self._current_content:
                return self._current_content
            raise StopAsyncIteration("Download complete")

        return self._get_chunk_data()

    def _get_chunk_data(self):
        chunk_data = self._current_content[: self._chunk_size]
        self._current_content = self._current_content[self._chunk_size:]
        return chunk_data


class StorageStreamDownloader(object):  # pylint: disable=too-many-instance-attributes
    """A streaming object to download from Azure Storage.

    :ivar str name:
        The name of the file being downloaded.
    :ivar: str path:
        The full path of the file.
    :ivar str share:
        The name of the share where the file is.
    :ivar ~azure.storage.fileshare.FileProperties properties:
        The properties of the file being downloaded. If only a range of the data is being
        downloaded, this will be reflected in the properties.
    :ivar int size:
        The size of the total data in the stream. This will be the byte range if speficied,
        otherwise the total size of the file.
    """

    def __init__(
            self,
            client=None,
            config=None,
            start_range=None,
            end_range=None,
            validate_content=None,
            max_concurrency=1,
            name=None,
            path=None,
            share=None,
            encoding=None,
            **kwargs
    ):
        self.name = name
        self.path = path
        self.share = share
        self.properties = None
        self.size = None

        self._client = client
        self._config = config
        self._start_range = start_range
        self._end_range = end_range
        self._max_concurrency = max_concurrency
        self._encoding = encoding
        self._validate_content = validate_content
        self._progress_hook = kwargs.pop('progress_hook', None)
        self._request_options = kwargs
        self._location_mode = None
        self._download_complete = False
        self._current_content = None
        self._file_size = None
        self._response = None
        self._etag = None

        # The service only provides transactional MD5s for chunks under 4MB.
        # If validate_content is on, get only self.MAX_CHUNK_GET_SIZE for the first
        # chunk so a transactional MD5 can be retrieved.
        self._first_get_size = self._config.max_single_get_size if not self._validate_content \
            else self._config.max_chunk_get_size
        initial_request_start = self._start_range if self._start_range is not None else 0
        if self._end_range is not None and self._end_range - self._start_range < self._first_get_size:
            initial_request_end = self._end_range
        else:
            initial_request_end = initial_request_start + self._first_get_size - 1

        self._initial_range = (initial_request_start, initial_request_end)

    def __len__(self):
        return self.size

    async def _setup(self):
        self._response = await self._initial_request()
        self.properties = self._response.properties
        self.properties.name = self.name
        self.properties.path = self.path
        self.properties.share = self.share

        # Set the content length to the download size instead of the size of
        # the last range
        self.properties.size = self.size

        # Overwrite the content range to the user requested range
        self.properties.content_range = 'bytes {0}-{1}/{2}'.format(
            self._start_range,
            self._end_range,
            self._file_size
        )

        # Overwrite the content MD5 as it is the MD5 for the last range instead
        # of the stored MD5
        # TODO: Set to the stored MD5 when the service returns this
        self.properties.content_md5 = None

        if self.size == 0:
            self._current_content = b""
        else:
            self._current_content = await process_content(self._response)

    async def _initial_request(self):
        range_header, range_validation = validate_and_format_range_headers(
            self._initial_range[0],
            self._initial_range[1],
            start_range_required=False,
            end_range_required=False,
            check_content_md5=self._validate_content)

        try:
            location_mode, response = await self._client.download(
                range=range_header,
                range_get_content_md5=range_validation,
                validate_content=self._validate_content,
                data_stream_total=None,
                download_stream_current=0,
                **self._request_options)

            # Check the location we read from to ensure we use the same one
            # for subsequent requests.
            self._location_mode = location_mode

            # Parse the total file size and adjust the download size if ranges
            # were specified
            self._file_size = parse_length_from_content_range(response.properties.content_range)
            if not self._file_size:
                raise ValueError("Required Content-Range response header is missing or malformed.")

            if self._end_range is not None:
                # Use the length unless it is over the end of the file
                self.size = min(self._file_size, self._end_range - self._start_range + 1)
            elif self._start_range is not None:
                self.size = self._file_size - self._start_range
            else:
                self.size = self._file_size

        except HttpResponseError as error:
            if self._start_range is None and error.response.status_code == 416:
                # Get range will fail on an empty file. If the user did not
                # request a range, do a regular get request in order to get
                # any properties.
                try:
                    _, response = await self._client.download(
                        validate_content=self._validate_content,
                        data_stream_total=0,
                        download_stream_current=0,
                        **self._request_options)
                except HttpResponseError as error:
                    process_storage_error(error)

                # Set the download size to empty
                self.size = 0
                self._file_size = 0
            else:
                process_storage_error(error)

        # If the file is small, the download is complete at this point.
        # If file size is large, download the rest of the file in chunks.
        if response.properties.size == self.size:
            self._download_complete = True
        self._etag = response.properties.etag
        return response

    def chunks(self):
        # type: () -> AsyncIterator[bytes]
        """Iterate over chunks in the download stream.

        :rtype: AsyncIterator[bytes]
        """
        if self.size == 0 or self._download_complete:
            iter_downloader = None
        else:
            data_end = self._file_size
            if self._end_range is not None:
                # Use the length unless it is over the end of the file
                data_end = min(self._file_size, self._end_range + 1)
            iter_downloader = _AsyncChunkDownloader(
                client=self._client,
                total_size=self.size,
                chunk_size=self._config.max_chunk_get_size,
                current_progress=self._first_get_size,
                start_range=self._initial_range[1] + 1,  # Start where the first download ended
                end_range=data_end,
                stream=None,
                parallel=False,
                validate_content=self._validate_content,
                use_location=self._location_mode,
                etag=self._etag,
                **self._request_options)
        return _AsyncChunkIterator(
            size=self.size,
            content=self._current_content,
            downloader=iter_downloader,
            chunk_size=self._config.max_chunk_get_size
        )

    async def readall(self):
        # type: () -> bytes
        """Download the contents of this file.

        This operation is blocking until all data is downloaded.
        :rtype: bytes
        """
        stream = BytesIO()
        await self.readinto(stream)
        data = stream.getvalue()
        if self._encoding:
            return data.decode(self._encoding)
        return data

    async def content_as_bytes(self, max_concurrency=1):
        """Download the contents of this file.

        This operation is blocking until all data is downloaded.

        :keyword int max_concurrency:
            The number of parallel connections with which to download.
        :rtype: bytes
        """
        warnings.warn(
            "content_as_bytes is deprecated, use readall instead",
            DeprecationWarning
        )
        self._max_concurrency = max_concurrency
        return await self.readall()

    async def content_as_text(self, max_concurrency=1, encoding="UTF-8"):
        """Download the contents of this file, and decode as text.

        This operation is blocking until all data is downloaded.

        :keyword int max_concurrency:
            The number of parallel connections with which to download.
        :param str encoding:
            Test encoding to decode the downloaded bytes. Default is UTF-8.
        :rtype: str
        """
        warnings.warn(
            "content_as_text is deprecated, use readall instead",
            DeprecationWarning
        )
        self._max_concurrency = max_concurrency
        self._encoding = encoding
        return await self.readall()

    async def readinto(self, stream):
        """Download the contents of this file to a stream.

        :param stream:
            The stream to download to. This can be an open file-handle,
            or any writable stream. The stream must be seekable if the download
            uses more than one parallel connection.
        :returns: The number of bytes read.
        :rtype: int
        """
        # the stream must be seekable if parallel download is required
        parallel = self._max_concurrency > 1
        if parallel:
            error_message = "Target stream handle must be seekable."
            if sys.version_info >= (3,) and not stream.seekable():
                raise ValueError(error_message)

            try:
                stream.seek(stream.tell())
            except (NotImplementedError, AttributeError):
                raise ValueError(error_message)

        # Write the content to the user stream
        stream.write(self._current_content)
        if self._progress_hook:
            await self._progress_hook(len(self._current_content), self.size)

        if self._download_complete:
            return self.size

        data_end = self._file_size
        if self._end_range is not None:
            # Use the length unless it is over the end of the file
            data_end = min(self._file_size, self._end_range + 1)

        downloader = _AsyncChunkDownloader(
            client=self._client,
            total_size=self.size,
            chunk_size=self._config.max_chunk_get_size,
            current_progress=self._first_get_size,
            start_range=self._initial_range[1] + 1,  # start where the first download ended
            end_range=data_end,
            stream=stream,
            parallel=parallel,
            validate_content=self._validate_content,
            use_location=self._location_mode,
            progress_hook=self._progress_hook,
            etag=self._etag,
            **self._request_options)

        dl_tasks = downloader.get_chunk_offsets()
        running_futures = [
            asyncio.ensure_future(downloader.process_chunk(d))
            for d in islice(dl_tasks, 0, self._max_concurrency)
        ]
        while running_futures:
            # Wait for some download to finish before adding a new one
            _done, running_futures = await asyncio.wait(
                running_futures, return_when=asyncio.FIRST_COMPLETED)
            try:
                next_chunk = next(dl_tasks)
            except StopIteration:
                break
            else:
                running_futures.add(asyncio.ensure_future(downloader.process_chunk(next_chunk)))

        if running_futures:
            # Wait for the remaining downloads to finish
            await asyncio.wait(running_futures)
        return self.size

    async def download_to_stream(self, stream, max_concurrency=1):
        """Download the contents of this file to a stream.

        :param stream:
            The stream to download to. This can be an open file-handle,
            or any writable stream. The stream must be seekable if the download
            uses more than one parallel connection.
        :returns: The properties of the downloaded file.
        :rtype: Any
        """
        warnings.warn(
            "download_to_stream is deprecated, use readinto instead",
            DeprecationWarning
        )
        self._max_concurrency = max_concurrency
        await self.readinto(stream)
        return self.properties
