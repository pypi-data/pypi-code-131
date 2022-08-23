"""get_runs SDK for Kubernetes"""
from __future__ import annotations

import datetime as dt
import logging
from concurrent.futures import Future
from typing import Any, Dict, List, NamedTuple, Optional, Sequence, Set, Union, overload

import yaml
from typing_extensions import Literal

from mcli.api.engine.engine import run_in_threadpool, run_kube_in_threadpool
from mcli.api.model.run import Run
from mcli.api.runs.api_get_runs import get_runs as mapi_get_runs
from mcli.config import FeatureFlag, MCLIConfig
from mcli.models.mcli_platform import MCLIPlatform
from mcli.models.run_config import FinalRunConfig
from mcli.serverside.job.mcli_job import RUN_CONFIG_FILE_NAME
from mcli.serverside.platforms.gpu_type import GPUType
from mcli.utils.utils_epilog import ContextPodStatus
from mcli.utils.utils_kube import KubeContext, list_config_maps_across_contexts, list_pods_across_contexts
from mcli.utils.utils_kube_labels import extract_label_values, label
from mcli.utils.utils_run_status import RunStatus

logger = logging.getLogger(__name__)

__all__ = ['get_runs']


class RunComponents(NamedTuple):
    """Grouping of a run's pods and configmap
    """
    pods: List[Dict[str, Any]]
    config_map: Optional[Dict[str, Any]] = None


CONFIG_NOT_FOUND = {'error': 'Config not found!'}
"""Singleton for when a run's corresponding FinalRunConfig cannot be found in the cluster
"""


def _get_runs_mapi(
    runs: Optional[List[str]] = None,
    platforms: Optional[List[str]] = None,
    gpu_types: Optional[List[str]] = None,
    gpu_nums: Optional[List[int]] = None,
    statuses: Optional[List[str]] = None,
) -> Future[List[Run]]:
    """Get runs from MAPI as a future and filter them in a thread
    """

    runs_future = mapi_get_runs(runs, statuses=statuses, future=True)

    if not platforms and not gpu_types and not gpu_nums:
        return runs_future

    return run_in_threadpool(
        _filter_mapi_runs,
        runs_future,
        platforms=platforms,
        gpu_types=gpu_types,
        gpu_nums=gpu_nums,
    )


def _filter_mapi_runs(
    runs_future: Future[List[Run]],
    platforms: Optional[List[str]] = None,
    gpu_types: Optional[List[str]] = None,
    gpu_nums: Optional[List[int]] = None,
    statuses: Optional[List[str]] = None,
) -> List[Run]:
    """Function to be called in a thread to filter the MAPI get_runs response
    """

    all_runs = runs_future.result()
    runs: List[Run] = []
    for run in all_runs:
        if platforms and run.config.platform not in platforms:
            continue
        if gpu_types and run.config.gpu_type not in gpu_types:
            continue
        if gpu_nums and run.config.gpu_num not in gpu_nums:
            continue
        if statuses and run.status not in statuses:
            continue
        runs.append(run)

    return runs


def _get_runs_kube(
    runs: Optional[List[str]] = None,
    platforms: Optional[List[str]] = None,
    gpu_types: Optional[List[str]] = None,
    gpu_nums: Optional[List[int]] = None,
    statuses: Optional[List[str]] = None,
) -> Future[List[Run]]:
    """Get runs from all registered Kubernetes platforms
    """

    # Setup filters for kubernetes
    # Filter platforms
    conf = MCLIConfig.load_config(safe=True)
    if platforms is not None:
        chosen_platforms: List[MCLIPlatform] = []
        looking_for: Set[str] = set(platforms)
        for platform in conf.platforms:
            if platform.name in looking_for:
                looking_for.discard(platform.name)
                chosen_platforms.append(platform)
            if not looking_for:
                break
        if looking_for:
            logger.warning(f'Ignoring unknown platform(s): {", ".join(sorted(list(looking_for)))}')
        if not chosen_platforms:
            raise RuntimeError(f'No platforms found matching filter: {", ".join(platforms)}')
    else:
        chosen_platforms = conf.platforms

    # Filter by names, gpu types and gpu num using labels
    # Filter to any pod with the "job" label present, by default
    labels: Dict[str, Optional[Union[str, List[str]]]] = {label.mosaic.JOB: None}
    if runs is not None:
        labels[label.mosaic.JOB] = list(runs)

    # Filter instances
    if gpu_types is not None:
        labels[label.mosaic.compute_selectors.LABEL_GPU_TYPE] = list(gpu_types)

    if gpu_nums is not None:
        labels[label.mosaic.compute_selectors.LABEL_GPU_NUM] = [str(i) for i in gpu_nums]

    # Use only the Kubernetes contexts for the platforms we want
    contexts = [p.to_kube_context() for p in chosen_platforms]

    res = run_kube_in_threadpool(_threaded_get_runs, contexts, labels, statuses)
    return res


def _threaded_get_runs(contexts: List[KubeContext],
                       labels: Dict[str, Optional[Union[str, List[str]]]],
                       statuses: Optional[Sequence[str]] = None) -> List[Run]:
    """Function to be called in a thread to return runs from the provided contexts that
    match the provided labels.
    """

    all_pods, _ = list_pods_across_contexts(contexts=contexts, labels=labels)
    if not all_pods:
        return []

    all_cms, _ = list_config_maps_across_contexts(contexts=contexts, labels=labels)
    run_components = _group_objects_by_label(all_pods, all_cms)

    return _run_from_components(run_components, statuses)


def _group_objects_by_label(
    pods: List[Dict[str, Any]],
    config_maps: List[Dict[str, Any]],
) -> Dict[str, RunComponents]:
    """Group pods and configmaps according to their value for the job label
    """

    group_by = label.mosaic.JOB

    cm_grouping: Dict[str, Dict[str, Any]] = {}
    labels: Dict[str, str]
    for cm in config_maps:
        labels = cm['metadata'].get('labels', {})
        key = labels.get(group_by, '-')
        if cm.get('data', {}).get(RUN_CONFIG_FILE_NAME):
            cm_grouping[key] = cm

    pod_grouping: Dict[str, List[Dict[str, Any]]] = {}
    for p in pods:
        labels = p['metadata'].get('labels', {})
        key = labels.get(group_by, '-')
        if key not in pod_grouping:
            pod_grouping[key] = []
        pod_grouping[key].append(p)

    return {
        key: RunComponents(pods=pods, config_map=cm_grouping.get(key, CONFIG_NOT_FOUND))
        for key, pods in pod_grouping.items()
    }


def _run_from_components(
    run_components: Dict[str, RunComponents],
    statuses: Optional[Sequence[str]] = None,
) -> List[Run]:
    """Extract the details for a :type Run: from a run's pods and configmaps
    """

    if statuses:
        valid_statuses = {RunStatus[status.upper()] for status in statuses}
    else:
        valid_statuses: Set[RunStatus] = set(RunStatus)

    dummy_run_data = {
        'run_uid': '',
        'job_config': {},
    }

    runs: List[Run] = []
    for name, components in run_components.items():

        # There will always be at least one pod associated with a job
        pod = components.pods[0]

        # Extract pod status
        status = ContextPodStatus.aggregate([ContextPodStatus.from_pod_dict(pod_dict) for pod_dict in components.pods
                                            ]).state
        if status not in valid_statuses:
            continue

        run_data: Dict[str, Any] = dummy_run_data.copy()
        run_data['name'] = name
        run_data['status'] = status

        if components.config_map and components.config_map != CONFIG_NOT_FOUND:
            config = FinalRunConfig(**yaml.safe_load(components.config_map['data'][RUN_CONFIG_FILE_NAME]))
        else:
            config = _extract_run_config(pod)

        # Extract times
        run_data['created_at'] = dt.datetime.fromisoformat(pod['metadata']['creationTimestamp'])

        # Add optional start and stop times
        run_data['completed_at'] = _get_end_time(pod)
        run_data['started_at'] = _get_start_time(pod)

        # Add updated time
        run_data['updated_at'] = _get_update_time(pod)

        run_data['config'] = config
        runs.append(Run(**run_data))

    return runs


def _extract_run_config(pod: Dict[str, Any]) -> FinalRunConfig:
    """Extract the :type FinalRunConfig: as best we can from one of a run's pods

    NOTE: This is only used as a fallback for runs performed before the
    :type FinalRunConfig: was stored in the run's configmap. As such, we will only
    extract information relevant for `mcli get runs`.
    """

    config_data = {
        'run_id': '',
        'name': '',
        'cpus': -1,
        'image': '',
        'command': '',
        'integrations': [],
        'env_variables': [],
        'parameters': {},
    }

    pod_labels: Dict[str, str] = dict(pod['metadata'].get('labels', {}))
    labels_to_get = [label.compute.LABEL_MCLI_PLATFORM, label.compute.LABEL_GPU_TYPE, label.compute.LABEL_GPU_NUM]
    label_vals = extract_label_values(pod_labels, labels_to_get, default='-')
    config_data['gpu_type'] = label_vals[label.compute.LABEL_GPU_TYPE]
    config_data['gpu_num'] = int(label_vals[label.compute.LABEL_GPU_NUM])
    config_data['platform'] = label_vals[label.compute.LABEL_MCLI_PLATFORM]

    # Try to get image
    try:
        image = pod['spec']['containers'][0]['image']
        config_data['image'] = image
    except (KeyError, IndexError):
        pass

    return FinalRunConfig(**config_data)


def _get_end_time(pod_dict: Dict[str, Any]) -> Optional[dt.datetime]:
    """Get a pod's end time from its container statuses
    """
    try:
        container_status = pod_dict['status']['containerStatuses'][0]
        terminated = container_status['state'].get('terminated')
        if terminated:
            return dt.datetime.fromisoformat(terminated['finishedAt'])
    except (KeyError, IndexError):
        pass


def _get_start_time(pod_dict: Dict[str, Any]) -> Optional[dt.datetime]:
    """Get a pod's start time

    note: pod startTime not the container start time. Useful for
    cost estimation and may be slightly less than container due
    to the time needed to pull the image inside the container
    """
    try:
        return dt.datetime.fromisoformat(pod_dict['status']['startTime'])
    except KeyError:
        pass


def _get_update_time(pod_dict: Dict[str, Any]) -> dt.datetime:
    """Get the last timestamp in metadata and status"""
    timestamps: List[dt.datetime] = [dt.datetime.fromisoformat(pod_dict['metadata']['creationTimestamp'])]

    status = pod_dict['status']

    # Get update time from each condition
    timestamps += [
        dt.datetime.fromisoformat(cond['lastTransitionTime'])
        for cond in status['conditions']
        if 'lastTransitionTime' in cond
    ]

    # Add container status
    if status.get('containerStatuses', []):
        container_status = status['containerStatuses'][0]
        state = container_status['state']
        if state.get('terminated'):
            timestamps.append(dt.datetime.fromisoformat(state['terminated']['finishedAt']))
        elif state.get('running'):
            timestamps.append(dt.datetime.fromisoformat(state['running']['startedAt']))

    return max(timestamps)


@overload
def get_runs(
    runs: Optional[Union[List[str], List[Run]]] = None,
    platforms: Optional[Union[List[str], List[MCLIPlatform]]] = None,
    gpu_types: Optional[Union[List[str], List[GPUType]]] = None,
    gpu_nums: Optional[List[int]] = None,
    statuses: Optional[Union[List[str], List[RunStatus]]] = None,
    timeout: Optional[float] = 10,
    future: Literal[False] = False,
) -> List[Run]:
    ...


@overload
def get_runs(
    runs: Optional[Union[List[str], List[Run]]] = None,
    platforms: Optional[Union[List[str], List[MCLIPlatform]]] = None,
    gpu_types: Optional[Union[List[str], List[GPUType]]] = None,
    gpu_nums: Optional[List[int]] = None,
    statuses: Optional[Union[List[str], List[RunStatus]]] = None,
    timeout: Optional[float] = None,
    future: Literal[True] = True,
) -> Future[List[Run]]:
    ...


def get_runs(
    runs: Optional[Union[List[str], List[Run]]] = None,
    platforms: Optional[Union[List[str], List[MCLIPlatform]]] = None,
    gpu_types: Optional[Union[List[str], List[GPUType]]] = None,
    gpu_nums: Optional[List[int]] = None,
    statuses: Optional[Union[List[str], List[RunStatus]]] = None,
    timeout: Optional[float] = 10,
    future: bool = False,
):
    """List runs that have been launched in the MosaicML Cloud

    The returned list will contain all of the details stored about the requested runs.

    Arguments:
        runs: List of run names on which to get information
        platforms: List of platforms to filter runs. This can be a list of str or
            :type MCLIPlatform: objects. Only runs submitted to these platforms will be
            returned.
        gpu_types: List of gpu types to filter runs. This can be a list of str or
            :type GPUType: enums. Only runs scheduled on these GPUs will be returned.
        gpu_nums: List of gpu counts to filter runs. Only runs scheduled on this number
            of GPUs will be returned.
        statuses: List of run statuses to filter runs. This can be a list of str or
            :type RunStatus: enums. Only runs currently in these phases will be returned.
        timeout: Time, in seconds, in which the call should complete. If the call
            takes too long, a TimeoutError will be raised. If ``future`` is ``True``, this
            value will be ignored.
        future: Return the output as a :type concurrent.futures.Future:. If True, the
            call to `get_runs` will return immediately and the request will be
            processed in the background. This takes precedence over the ``timeout``
            argument. To get the list of runs, use ``return_value.result()``
            with an optional ``timeout`` argument.

    Raises:
        MAPIException: If connecting to MAPI, raised when a MAPI communication error occurs
        KubernetesException: Raised when a Kubernetes error occurs when communicating with only 1 cluster
        RuntimeError: Raised when some error occurs in calls to multiple Kubernetes clusters
    """

    # Coerce arg types to strings
    if runs is not None:
        runs = [r.name if isinstance(r, Run) else r for r in runs]

    if platforms is not None:
        platforms = [pl.name if isinstance(pl, MCLIPlatform) else pl for pl in platforms]

    if gpu_types is not None:
        gpu_types = [gt.name if isinstance(gt, GPUType) else gt for gt in gpu_types]

    if statuses is not None:
        statuses = [st.name if isinstance(st, RunStatus) else st for st in statuses]

    # If requested pull runs from MAPI
    # Since MAPI doesn't yet return filtered values, filter client-sided
    conf = MCLIConfig.load_config()
    if conf.feature_enabled(FeatureFlag.USE_FEATUREDB):
        runs_future = _get_runs_mapi(runs, platforms, gpu_types, gpu_nums, statuses)
    else:
        runs_future = _get_runs_kube(runs, platforms, gpu_types, gpu_nums, statuses)

    if not future:
        return runs_future.result(timeout=timeout)
    else:
        return runs_future
