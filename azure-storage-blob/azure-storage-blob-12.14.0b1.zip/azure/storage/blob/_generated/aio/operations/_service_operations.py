# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterator, Callable, Dict, IO, List, Optional, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._service_operations import (
    build_filter_blobs_request,
    build_get_account_info_request,
    build_get_properties_request,
    build_get_statistics_request,
    build_get_user_delegation_key_request,
    build_list_containers_segment_request,
    build_set_properties_request,
    build_submit_batch_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ServiceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.blob.aio.AzureBlobStorage`'s
        :attr:`service` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def set_properties(  # pylint: disable=inconsistent-return-statements
        self,
        storage_service_properties: _models.StorageServiceProperties,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Sets properties for a storage account's Blob service endpoint, including properties for Storage
        Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :param storage_service_properties: The StorageService properties. Required.
        :type storage_service_properties: ~azure.storage.blob.models.StorageServiceProperties
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        restype = kwargs.pop("restype", _params.pop("restype", "service"))  # type: str
        comp = kwargs.pop("comp", _params.pop("comp", "properties"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/xml"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _content = self._serialize.body(storage_service_properties, "StorageServiceProperties", is_xml=True)

        request = build_set_properties_request(
            url=self._config.url,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            restype=restype,
            comp=comp,
            content_type=content_type,
            version=self._config.version,
            content=_content,
            template_url=self.set_properties.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    set_properties.metadata = {"url": "{url}"}  # type: ignore

    @distributed_trace_async
    async def get_properties(
        self, timeout: Optional[int] = None, request_id_parameter: Optional[str] = None, **kwargs: Any
    ) -> _models.StorageServiceProperties:
        """gets the properties of a storage account's Blob service, including properties for Storage
        Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageServiceProperties or the result of cls(response)
        :rtype: ~azure.storage.blob.models.StorageServiceProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        restype = kwargs.pop("restype", _params.pop("restype", "service"))  # type: str
        comp = kwargs.pop("comp", _params.pop("comp", "properties"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.StorageServiceProperties]

        request = build_get_properties_request(
            url=self._config.url,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            restype=restype,
            comp=comp,
            version=self._config.version,
            template_url=self.get_properties.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        deserialized = self._deserialize("StorageServiceProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get_properties.metadata = {"url": "{url}"}  # type: ignore

    @distributed_trace_async
    async def get_statistics(
        self, timeout: Optional[int] = None, request_id_parameter: Optional[str] = None, **kwargs: Any
    ) -> _models.StorageServiceStats:
        """Retrieves statistics related to replication for the Blob service. It is only available on the
        secondary location endpoint when read-access geo-redundant replication is enabled for the
        storage account.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "stats". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageServiceStats or the result of cls(response)
        :rtype: ~azure.storage.blob.models.StorageServiceStats
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        restype = kwargs.pop("restype", _params.pop("restype", "service"))  # type: str
        comp = kwargs.pop("comp", _params.pop("comp", "stats"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.StorageServiceStats]

        request = build_get_statistics_request(
            url=self._config.url,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            restype=restype,
            comp=comp,
            version=self._config.version,
            template_url=self.get_statistics.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        deserialized = self._deserialize("StorageServiceStats", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get_statistics.metadata = {"url": "{url}"}  # type: ignore

    @distributed_trace_async
    async def list_containers_segment(
        self,
        prefix: Optional[str] = None,
        marker: Optional[str] = None,
        maxresults: Optional[int] = None,
        include: Optional[List[Union[str, "_models.ListContainersIncludeType"]]] = None,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ListContainersSegmentResponse:
        """The List Containers Segment operation returns a list of the containers under the specified
        account.

        :param prefix: Filters the results to return only containers whose name begins with the
         specified prefix. Default value is None.
        :type prefix: str
        :param marker: A string value that identifies the portion of the list of containers to be
         returned with the next listing operation. The operation returns the NextMarker value within the
         response body if the listing operation did not return all containers remaining to be listed
         with the current page. The NextMarker value can be used as the value for the marker parameter
         in a subsequent call to request the next page of list items. The marker value is opaque to the
         client. Default value is None.
        :type marker: str
        :param maxresults: Specifies the maximum number of containers to return. If the request does
         not specify maxresults, or specifies a value greater than 5000, the server will return up to
         5000 items. Note that if the listing operation crosses a partition boundary, then the service
         will return a continuation token for retrieving the remainder of the results. For this reason,
         it is possible that the service will return fewer results than specified by maxresults, or than
         the default of 5000. Default value is None.
        :type maxresults: int
        :param include: Include this parameter to specify that the container's metadata be returned as
         part of the response body. Default value is None.
        :type include: list[str or ~azure.storage.blob.models.ListContainersIncludeType]
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword comp: comp. Default value is "list". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListContainersSegmentResponse or the result of cls(response)
        :rtype: ~azure.storage.blob.models.ListContainersSegmentResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        comp = kwargs.pop("comp", _params.pop("comp", "list"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ListContainersSegmentResponse]

        request = build_list_containers_segment_request(
            url=self._config.url,
            prefix=prefix,
            marker=marker,
            maxresults=maxresults,
            include=include,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            comp=comp,
            version=self._config.version,
            template_url=self.list_containers_segment.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        deserialized = self._deserialize("ListContainersSegmentResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    list_containers_segment.metadata = {"url": "{url}"}  # type: ignore

    @distributed_trace_async
    async def get_user_delegation_key(
        self,
        key_info: _models.KeyInfo,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> _models.UserDelegationKey:
        """Retrieves a user delegation key for the Blob service. This is only a valid operation when using
        bearer token authentication.

        :param key_info: Key information. Required.
        :type key_info: ~azure.storage.blob.models.KeyInfo
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "userdelegationkey". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: UserDelegationKey or the result of cls(response)
        :rtype: ~azure.storage.blob.models.UserDelegationKey
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        restype = kwargs.pop("restype", _params.pop("restype", "service"))  # type: str
        comp = kwargs.pop("comp", _params.pop("comp", "userdelegationkey"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/xml"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.UserDelegationKey]

        _content = self._serialize.body(key_info, "KeyInfo", is_xml=True)

        request = build_get_user_delegation_key_request(
            url=self._config.url,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            restype=restype,
            comp=comp,
            content_type=content_type,
            version=self._config.version,
            content=_content,
            template_url=self.get_user_delegation_key.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        deserialized = self._deserialize("UserDelegationKey", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get_user_delegation_key.metadata = {"url": "{url}"}  # type: ignore

    @distributed_trace_async
    async def get_account_info(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Returns the sku name and account kind.

        :keyword restype: restype. Default value is "account". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        restype = kwargs.pop("restype", _params.pop("restype", "account"))  # type: str
        comp = kwargs.pop("comp", _params.pop("comp", "properties"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_account_info_request(
            url=self._config.url,
            restype=restype,
            comp=comp,
            version=self._config.version,
            template_url=self.get_account_info.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))
        response_headers["x-ms-sku-name"] = self._deserialize("str", response.headers.get("x-ms-sku-name"))
        response_headers["x-ms-account-kind"] = self._deserialize("str", response.headers.get("x-ms-account-kind"))
        response_headers["x-ms-is-hns-enabled"] = self._deserialize("bool", response.headers.get("x-ms-is-hns-enabled"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    get_account_info.metadata = {"url": "{url}"}  # type: ignore

    @distributed_trace_async
    async def submit_batch(
        self,
        content_length: int,
        body: IO,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterator[bytes]:
        """The Batch operation allows multiple API calls to be embedded into a single HTTP request.

        :param content_length: The length of the request. Required.
        :type content_length: int
        :param body: Initial data. Required.
        :type body: IO
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword comp: comp. Default value is "batch". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Async iterator of the response bytes or the result of cls(response)
        :rtype: AsyncIterator[bytes]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        comp = kwargs.pop("comp", _params.pop("comp", "batch"))  # type: str
        multipart_content_type = kwargs.pop(
            "multipart_content_type", _headers.pop("Content-Type", "application/xml")
        )  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[AsyncIterator[bytes]]

        _content = body

        request = build_submit_batch_request(
            url=self._config.url,
            content_length=content_length,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            comp=comp,
            multipart_content_type=multipart_content_type,
            version=self._config.version,
            content=_content,
            template_url=self.submit_batch.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=True, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    submit_batch.metadata = {"url": "{url}"}  # type: ignore

    @distributed_trace_async
    async def filter_blobs(
        self,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        where: Optional[str] = None,
        marker: Optional[str] = None,
        maxresults: Optional[int] = None,
        include: Optional[List[Union[str, "_models.FilterBlobsIncludeItem"]]] = None,
        **kwargs: Any
    ) -> _models.FilterBlobSegment:
        """The Filter Blobs operation enables callers to list blobs across all containers whose tags match
        a given search expression.  Filter blobs searches across all containers within a storage
        account but can be scoped within the expression to a single container.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param where: Filters the results to return only to return only blobs whose tags match the
         specified expression. Default value is None.
        :type where: str
        :param marker: A string value that identifies the portion of the list of containers to be
         returned with the next listing operation. The operation returns the NextMarker value within the
         response body if the listing operation did not return all containers remaining to be listed
         with the current page. The NextMarker value can be used as the value for the marker parameter
         in a subsequent call to request the next page of list items. The marker value is opaque to the
         client. Default value is None.
        :type marker: str
        :param maxresults: Specifies the maximum number of containers to return. If the request does
         not specify maxresults, or specifies a value greater than 5000, the server will return up to
         5000 items. Note that if the listing operation crosses a partition boundary, then the service
         will return a continuation token for retrieving the remainder of the results. For this reason,
         it is possible that the service will return fewer results than specified by maxresults, or than
         the default of 5000. Default value is None.
        :type maxresults: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response. Default value is None.
        :type include: list[str or ~azure.storage.blob.models.FilterBlobsIncludeItem]
        :keyword comp: comp. Default value is "blobs". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FilterBlobSegment or the result of cls(response)
        :rtype: ~azure.storage.blob.models.FilterBlobSegment
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        comp = kwargs.pop("comp", _params.pop("comp", "blobs"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.FilterBlobSegment]

        request = build_filter_blobs_request(
            url=self._config.url,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            where=where,
            marker=marker,
            maxresults=maxresults,
            include=include,
            comp=comp,
            version=self._config.version,
            template_url=self.filter_blobs.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        deserialized = self._deserialize("FilterBlobSegment", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    filter_blobs.metadata = {"url": "{url}"}  # type: ignore
