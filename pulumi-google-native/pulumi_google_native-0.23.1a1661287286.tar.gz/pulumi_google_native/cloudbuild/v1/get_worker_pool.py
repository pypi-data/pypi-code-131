# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetWorkerPoolResult',
    'AwaitableGetWorkerPoolResult',
    'get_worker_pool',
    'get_worker_pool_output',
]

@pulumi.output_type
class GetWorkerPoolResult:
    def __init__(__self__, annotations=None, create_time=None, delete_time=None, display_name=None, etag=None, name=None, private_pool_v1_config=None, state=None, uid=None, update_time=None):
        if annotations and not isinstance(annotations, dict):
            raise TypeError("Expected argument 'annotations' to be a dict")
        pulumi.set(__self__, "annotations", annotations)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if delete_time and not isinstance(delete_time, str):
            raise TypeError("Expected argument 'delete_time' to be a str")
        pulumi.set(__self__, "delete_time", delete_time)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_pool_v1_config and not isinstance(private_pool_v1_config, dict):
            raise TypeError("Expected argument 'private_pool_v1_config' to be a dict")
        pulumi.set(__self__, "private_pool_v1_config", private_pool_v1_config)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def annotations(self) -> Mapping[str, str]:
        """
        User specified annotations. See https://google.aip.dev/128#annotations for more details such as format and size limitations.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Time at which the request to create the `WorkerPool` was received.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> str:
        """
        Time at which the request to delete the `WorkerPool` was received.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-specified, human-readable name for the `WorkerPool`. If provided, this value must be 1-63 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Checksum computed by the server. May be sent on update and delete requests to ensure that the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the `WorkerPool`, with format `projects/{project}/locations/{location}/workerPools/{worker_pool}`. The value of `{worker_pool}` is provided by `worker_pool_id` in `CreateWorkerPool` request and the value of `{location}` is determined by the endpoint accessed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privatePoolV1Config")
    def private_pool_v1_config(self) -> 'outputs.PrivatePoolV1ConfigResponse':
        """
        Legacy Private Pool configuration.
        """
        return pulumi.get(self, "private_pool_v1_config")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        `WorkerPool` state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def uid(self) -> str:
        """
        A unique identifier for the `WorkerPool`.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Time at which the request to update the `WorkerPool` was received.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetWorkerPoolResult(GetWorkerPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkerPoolResult(
            annotations=self.annotations,
            create_time=self.create_time,
            delete_time=self.delete_time,
            display_name=self.display_name,
            etag=self.etag,
            name=self.name,
            private_pool_v1_config=self.private_pool_v1_config,
            state=self.state,
            uid=self.uid,
            update_time=self.update_time)


def get_worker_pool(location: Optional[str] = None,
                    project: Optional[str] = None,
                    worker_pool_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkerPoolResult:
    """
    Returns details of a `WorkerPool`.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['workerPoolId'] = worker_pool_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:cloudbuild/v1:getWorkerPool', __args__, opts=opts, typ=GetWorkerPoolResult).value

    return AwaitableGetWorkerPoolResult(
        annotations=__ret__.annotations,
        create_time=__ret__.create_time,
        delete_time=__ret__.delete_time,
        display_name=__ret__.display_name,
        etag=__ret__.etag,
        name=__ret__.name,
        private_pool_v1_config=__ret__.private_pool_v1_config,
        state=__ret__.state,
        uid=__ret__.uid,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_worker_pool)
def get_worker_pool_output(location: Optional[pulumi.Input[str]] = None,
                           project: Optional[pulumi.Input[Optional[str]]] = None,
                           worker_pool_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkerPoolResult]:
    """
    Returns details of a `WorkerPool`.
    """
    ...
