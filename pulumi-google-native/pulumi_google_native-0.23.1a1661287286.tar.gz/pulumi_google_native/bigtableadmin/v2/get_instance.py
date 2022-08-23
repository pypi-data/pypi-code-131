# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    def __init__(__self__, create_time=None, display_name=None, labels=None, name=None, satisfies_pzs=None, state=None, type=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if satisfies_pzs and not isinstance(satisfies_pzs, bool):
            raise TypeError("Expected argument 'satisfies_pzs' to be a bool")
        pulumi.set(__self__, "satisfies_pzs", satisfies_pzs)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        A server-assigned timestamp representing when this Instance was created. For instances created before this field was added (August 2021), this value is `seconds: 0, nanos: 1`.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The descriptive name for this instance as it appears in UIs. Can be changed at any time, but should be kept globally unique to avoid confusion.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. They can be used to filter resources and aggregate metrics. * Label keys must be between 1 and 63 characters long and must conform to the regular expression: `\\p{Ll}\\p{Lo}{0,62}`. * Label values must be between 0 and 63 characters long and must conform to the regular expression: `[\\p{Ll}\\p{Lo}\\p{N}_-]{0,63}`. * No more than 64 labels can be associated with a given resource. * Keys and values must both be under 128 bytes.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The unique name of the instance. Values are of the form `projects/{project}/instances/a-z+[a-z0-9]`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> bool:
        """
        Reserved for future use.
        """
        return pulumi.get(self, "satisfies_pzs")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the instance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the instance. Defaults to `PRODUCTION`.
        """
        return pulumi.get(self, "type")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            create_time=self.create_time,
            display_name=self.display_name,
            labels=self.labels,
            name=self.name,
            satisfies_pzs=self.satisfies_pzs,
            state=self.state,
            type=self.type)


def get_instance(instance_id: Optional[str] = None,
                 project: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Gets information about an instance.
    """
    __args__ = dict()
    __args__['instanceId'] = instance_id
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:bigtableadmin/v2:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        create_time=__ret__.create_time,
        display_name=__ret__.display_name,
        labels=__ret__.labels,
        name=__ret__.name,
        satisfies_pzs=__ret__.satisfies_pzs,
        state=__ret__.state,
        type=__ret__.type)


@_utilities.lift_output_func(get_instance)
def get_instance_output(instance_id: Optional[pulumi.Input[str]] = None,
                        project: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Gets information about an instance.
    """
    ...
