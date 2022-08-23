"""Implements watching run status for the Kubernetes API"""
from __future__ import annotations

from concurrent.futures import Future
from http import HTTPStatus
from typing import Optional, Union, overload

from kubernetes import client
from typing_extensions import Literal

from mcli.api.engine.engine import run_kube_in_threadpool
from mcli.api.exceptions import KubernetesException
from mcli.api.kube.runs import get_runs
from mcli.api.model.run import Run
from mcli.models.mcli_platform import MCLIPlatform
from mcli.utils.utils_epilog import RunEpilog
from mcli.utils.utils_run_status import RunStatus


class RunFailed(Exception):
    """Raised when a run has failed before reaching a user's requested status
    """
    pass


def _threaded_watch_run(run: Union[str, Run], status: RunStatus):
    """Function run in a thread that will wait until the run reaches a specific status

    Args:
        run_name (str): Name of the run
        status (RunStatus): Status to watch for

    Raises:
        KubernetesException: Raised with status code 404 if the requested run could not be found
        RunFailed: Raised if the run failed before reaching the requested status

    Returns:
        The :type Run: object when the requested status was reached
    """
    if isinstance(run, str):
        runs = get_runs([run], timeout=None)
        if not runs:
            raise KubernetesException(status=HTTPStatus.NOT_FOUND, message=f'Could not find the run {run}')
        run = runs[0]

    with MCLIPlatform.use(run.config.platform) as platform:
        try:
            watcher = RunEpilog(run.name, platform.namespace)
            pod_status = watcher.wait_until(pass_state=status)
        except client.ApiException as e:
            raise KubernetesException.transform_api_exception(e) from e
        # Narrowing type since pod_status cannot be None if the wait_until timeout is None
        assert pod_status is not None

        # Update the run status - it's the only thing that's changed
        run.status = pod_status.state

        if status == run.status:
            # If the status was requested, return the run now
            return run

        # If the status was not the requested one, could be because of failure, so error here
        if run.status == RunStatus.FAILED_PULL:
            # The run failed to start because of an image pull error
            raise RunFailed(f'Run {run.name} failed because the image "{run.config.image}" could not be pulled. '
                            'The run will likely not start and should be deleted. Try:\n\n'
                            f'delete_runs([{run.name}])\n\n'
                            'or from the CLI:\n\n'
                            f'mcli delete run {run.name}')
        elif run.status in RunStatus.failed_states:
            # The run has otherwise failed, so raise an error
            raise RunFailed(f'Run {run.name} has failed. You may be able to look at the logs with the command:\n\n'
                            f'mcli logs {run.name}')

        return run


@overload
def wait_for_run_status(run: Union[str, Run],
                        status: Union[str, RunStatus],
                        timeout: Optional[float] = None,
                        future: Literal[False] = False) -> Run:
    ...


@overload
def wait_for_run_status(run: Union[str, Run],
                        status: Union[str, RunStatus],
                        timeout: Optional[float] = None,
                        future: Literal[True] = True) -> Future[Run]:
    ...


def wait_for_run_status(run: Union[str, Run],
                        status: Union[str, RunStatus],
                        timeout: Optional[float] = None,
                        future: bool = False) -> Union[Run, Future[Run]]:
    """Wait for a launched run to reach a specific status

    Args:
        run_name (str): Name of the run
        status: Status to wait for. This can be any valid :type RunStatus: value. If the
            run never reaches this state (e.g. it fails or the wait times out), then an
            error will be raised. See exception details below.
        timeout: Optional time, in seconds, in which the call should complete. If `None`
            (default), then the call will never timeout. Otherwise, if the run does not
            reach the requested status in the specified time, a TimeoutError will be raised.
            If ``future`` is ``True``, this value will be ignored. Default: None
        future: Return the output as a :type concurrent.futures.Future:. If True, the
            call to `wait_for_run_status` will return immediately and the request will be
            processed in the background. This takes precedence over the ``timeout``
            argument. To get the :type Run: output, use ``return_value.result()``
            with an optional ``timeout`` argument.

    Raises:
        KubernetesException: Raised with status code 404 if the requested run could not be found
        RunFailed: Raised if the run failed before reaching the requested status
        TimeoutError: Raised if the run did not reach the correct status in the specified time

    Returns:
        The :type Run: object when the requested status was reached
    """
    if isinstance(status, str):
        try:
            status = RunStatus[status.upper()]
        except KeyError as e:
            status_names = ', '.join([status.value.lower() for status in list(RunStatus)])
            raise KeyError(f'Invalid status value. Must be one of: {status_names}') from e

    wait_future = run_kube_in_threadpool(_threaded_watch_run, run, status)

    if not future:
        return wait_future.result(timeout=timeout)
    else:
        return wait_future
