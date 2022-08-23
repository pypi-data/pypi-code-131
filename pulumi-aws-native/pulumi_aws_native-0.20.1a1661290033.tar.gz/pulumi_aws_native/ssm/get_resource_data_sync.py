# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetResourceDataSyncResult',
    'AwaitableGetResourceDataSyncResult',
    'get_resource_data_sync',
    'get_resource_data_sync_output',
]

@pulumi.output_type
class GetResourceDataSyncResult:
    def __init__(__self__, sync_source=None):
        if sync_source and not isinstance(sync_source, dict):
            raise TypeError("Expected argument 'sync_source' to be a dict")
        pulumi.set(__self__, "sync_source", sync_source)

    @property
    @pulumi.getter(name="syncSource")
    def sync_source(self) -> Optional['outputs.ResourceDataSyncSyncSource']:
        return pulumi.get(self, "sync_source")


class AwaitableGetResourceDataSyncResult(GetResourceDataSyncResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceDataSyncResult(
            sync_source=self.sync_source)


def get_resource_data_sync(sync_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceDataSyncResult:
    """
    Resource Type definition for AWS::SSM::ResourceDataSync
    """
    __args__ = dict()
    __args__['syncName'] = sync_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ssm:getResourceDataSync', __args__, opts=opts, typ=GetResourceDataSyncResult).value

    return AwaitableGetResourceDataSyncResult(
        sync_source=__ret__.sync_source)


@_utilities.lift_output_func(get_resource_data_sync)
def get_resource_data_sync_output(sync_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceDataSyncResult]:
    """
    Resource Type definition for AWS::SSM::ResourceDataSync
    """
    ...
