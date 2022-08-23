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
    'GetBandwidthPackagesResult',
    'AwaitableGetBandwidthPackagesResult',
    'get_bandwidth_packages',
    'get_bandwidth_packages_output',
]

@pulumi.output_type
class GetBandwidthPackagesResult:
    """
    A collection of values returned by getBandwidthPackages.
    """
    def __init__(__self__, id=None, ids=None, include_reservation_data=None, instance_id=None, name_regex=None, names=None, output_file=None, packages=None, status=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if include_reservation_data and not isinstance(include_reservation_data, bool):
            raise TypeError("Expected argument 'include_reservation_data' to be a bool")
        pulumi.set(__self__, "include_reservation_data", include_reservation_data)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if packages and not isinstance(packages, list):
            raise TypeError("Expected argument 'packages' to be a list")
        pulumi.set(__self__, "packages", packages)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

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
        """
        A list of specific CEN Bandwidth Package IDs.
        * `names` (Available in 1.98.0+) - A list of CEN Bandwidth Package Names.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="includeReservationData")
    def include_reservation_data(self) -> Optional[bool]:
        return pulumi.get(self, "include_reservation_data")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[str]:
        """
        The ID of the CEN instance that are associated with the bandwidth package.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def packages(self) -> Sequence['outputs.GetBandwidthPackagesPackageResult']:
        """
        A list of CEN bandwidth package. Each element contains the following attributes:
        """
        return pulumi.get(self, "packages")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Status of the CEN Bandwidth Package in CEN instance, including `Idle` and `InUse`.
        """
        return pulumi.get(self, "status")


class AwaitableGetBandwidthPackagesResult(GetBandwidthPackagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBandwidthPackagesResult(
            id=self.id,
            ids=self.ids,
            include_reservation_data=self.include_reservation_data,
            instance_id=self.instance_id,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            packages=self.packages,
            status=self.status)


def get_bandwidth_packages(ids: Optional[Sequence[str]] = None,
                           include_reservation_data: Optional[bool] = None,
                           instance_id: Optional[str] = None,
                           name_regex: Optional[str] = None,
                           output_file: Optional[str] = None,
                           status: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBandwidthPackagesResult:
    """
    This data source provides CEN Bandwidth Packages available to the user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.cen.get_bandwidth_packages(instance_id="cen-id1",
        name_regex="^foo")
    pulumi.export("firstCenBandwidthPackageId", example.packages[0].id)
    ```


    :param Sequence[str] ids: Limit search to a list of specific CEN Bandwidth Package IDs.
    :param bool include_reservation_data: -Indicates whether to include renewal data. Valid values: `true`: Return renewal data in the response. `false`: Do not return renewal data in the response.
    :param str instance_id: ID of a CEN instance.
    :param str name_regex: A regex string to filter CEN Bandwidth Package by name.
    :param str status: Status of the CEN Bandwidth Package in CEN instance, Valid value: `Idle` and `InUse`.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['includeReservationData'] = include_reservation_data
    __args__['instanceId'] = instance_id
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:cen/getBandwidthPackages:getBandwidthPackages', __args__, opts=opts, typ=GetBandwidthPackagesResult).value

    return AwaitableGetBandwidthPackagesResult(
        id=__ret__.id,
        ids=__ret__.ids,
        include_reservation_data=__ret__.include_reservation_data,
        instance_id=__ret__.instance_id,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        packages=__ret__.packages,
        status=__ret__.status)


@_utilities.lift_output_func(get_bandwidth_packages)
def get_bandwidth_packages_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                  include_reservation_data: Optional[pulumi.Input[Optional[bool]]] = None,
                                  instance_id: Optional[pulumi.Input[Optional[str]]] = None,
                                  name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                  output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                  status: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBandwidthPackagesResult]:
    """
    This data source provides CEN Bandwidth Packages available to the user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.cen.get_bandwidth_packages(instance_id="cen-id1",
        name_regex="^foo")
    pulumi.export("firstCenBandwidthPackageId", example.packages[0].id)
    ```


    :param Sequence[str] ids: Limit search to a list of specific CEN Bandwidth Package IDs.
    :param bool include_reservation_data: -Indicates whether to include renewal data. Valid values: `true`: Return renewal data in the response. `false`: Do not return renewal data in the response.
    :param str instance_id: ID of a CEN instance.
    :param str name_regex: A regex string to filter CEN Bandwidth Package by name.
    :param str status: Status of the CEN Bandwidth Package in CEN instance, Valid value: `Idle` and `InUse`.
    """
    ...
