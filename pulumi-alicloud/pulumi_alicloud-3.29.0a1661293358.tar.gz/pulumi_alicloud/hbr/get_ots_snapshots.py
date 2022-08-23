# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetOtsSnapshotsResult',
    'AwaitableGetOtsSnapshotsResult',
    'get_ots_snapshots',
    'get_ots_snapshots_output',
]

@pulumi.output_type
class GetOtsSnapshotsResult:
    """
    A collection of values returned by getOtsSnapshots.
    """
    def __init__(__self__, end_time=None, id=None, ids=None, output_file=None, snapshots=None, start_time=None):
        if end_time and not isinstance(end_time, str):
            raise TypeError("Expected argument 'end_time' to be a str")
        pulumi.set(__self__, "end_time", end_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if snapshots and not isinstance(snapshots, list):
            raise TypeError("Expected argument 'snapshots' to be a list")
        pulumi.set(__self__, "snapshots", snapshots)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[str]:
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def snapshots(self) -> Sequence['outputs.GetOtsSnapshotsSnapshotResult']:
        return pulumi.get(self, "snapshots")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[str]:
        return pulumi.get(self, "start_time")


class AwaitableGetOtsSnapshotsResult(GetOtsSnapshotsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOtsSnapshotsResult(
            end_time=self.end_time,
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            snapshots=self.snapshots,
            start_time=self.start_time)


def get_ots_snapshots(end_time: Optional[str] = None,
                      ids: Optional[Sequence[str]] = None,
                      output_file: Optional[str] = None,
                      start_time: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOtsSnapshotsResult:
    """
    This data source provides the Hbr Ots Snapshots of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.164.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    snapshots = alicloud.hbr.get_ots_snapshots()
    ```


    :param str end_time: The end time of the backup. This value must be a UNIX timestamp. Unit: milliseconds
    :param str start_time: The start time of the backup snapshot. This value is a UNIX timestamp. Unit: seconds.
    """
    __args__ = dict()
    __args__['endTime'] = end_time
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    __args__['startTime'] = start_time
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:hbr/getOtsSnapshots:getOtsSnapshots', __args__, opts=opts, typ=GetOtsSnapshotsResult).value

    return AwaitableGetOtsSnapshotsResult(
        end_time=__ret__.end_time,
        id=__ret__.id,
        ids=__ret__.ids,
        output_file=__ret__.output_file,
        snapshots=__ret__.snapshots,
        start_time=__ret__.start_time)


@_utilities.lift_output_func(get_ots_snapshots)
def get_ots_snapshots_output(end_time: Optional[pulumi.Input[Optional[str]]] = None,
                             ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                             output_file: Optional[pulumi.Input[Optional[str]]] = None,
                             start_time: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOtsSnapshotsResult]:
    """
    This data source provides the Hbr Ots Snapshots of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.164.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    snapshots = alicloud.hbr.get_ots_snapshots()
    ```


    :param str end_time: The end time of the backup. This value must be a UNIX timestamp. Unit: milliseconds
    :param str start_time: The start time of the backup snapshot. This value is a UNIX timestamp. Unit: seconds.
    """
    ...
