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
    'GetDBInstanceResult',
    'AwaitableGetDBInstanceResult',
    'get_db_instance',
    'get_db_instance_output',
]

@pulumi.output_type
class GetDBInstanceResult:
    def __init__(__self__, auto_minor_version_upgrade=None, d_b_instance_class=None, enable_performance_insights=None, endpoint=None, id=None, port=None, preferred_maintenance_window=None, tags=None):
        if auto_minor_version_upgrade and not isinstance(auto_minor_version_upgrade, bool):
            raise TypeError("Expected argument 'auto_minor_version_upgrade' to be a bool")
        pulumi.set(__self__, "auto_minor_version_upgrade", auto_minor_version_upgrade)
        if d_b_instance_class and not isinstance(d_b_instance_class, str):
            raise TypeError("Expected argument 'd_b_instance_class' to be a str")
        pulumi.set(__self__, "d_b_instance_class", d_b_instance_class)
        if enable_performance_insights and not isinstance(enable_performance_insights, bool):
            raise TypeError("Expected argument 'enable_performance_insights' to be a bool")
        pulumi.set(__self__, "enable_performance_insights", enable_performance_insights)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if port and not isinstance(port, str):
            raise TypeError("Expected argument 'port' to be a str")
        pulumi.set(__self__, "port", port)
        if preferred_maintenance_window and not isinstance(preferred_maintenance_window, str):
            raise TypeError("Expected argument 'preferred_maintenance_window' to be a str")
        pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[bool]:
        return pulumi.get(self, "auto_minor_version_upgrade")

    @property
    @pulumi.getter(name="dBInstanceClass")
    def d_b_instance_class(self) -> Optional[str]:
        return pulumi.get(self, "d_b_instance_class")

    @property
    @pulumi.getter(name="enablePerformanceInsights")
    def enable_performance_insights(self) -> Optional[bool]:
        return pulumi.get(self, "enable_performance_insights")

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[str]:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def port(self) -> Optional[str]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[str]:
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DBInstanceTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetDBInstanceResult(GetDBInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDBInstanceResult(
            auto_minor_version_upgrade=self.auto_minor_version_upgrade,
            d_b_instance_class=self.d_b_instance_class,
            enable_performance_insights=self.enable_performance_insights,
            endpoint=self.endpoint,
            id=self.id,
            port=self.port,
            preferred_maintenance_window=self.preferred_maintenance_window,
            tags=self.tags)


def get_db_instance(id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDBInstanceResult:
    """
    Resource Type definition for AWS::DocDB::DBInstance
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:docdb:getDBInstance', __args__, opts=opts, typ=GetDBInstanceResult).value

    return AwaitableGetDBInstanceResult(
        auto_minor_version_upgrade=__ret__.auto_minor_version_upgrade,
        d_b_instance_class=__ret__.d_b_instance_class,
        enable_performance_insights=__ret__.enable_performance_insights,
        endpoint=__ret__.endpoint,
        id=__ret__.id,
        port=__ret__.port,
        preferred_maintenance_window=__ret__.preferred_maintenance_window,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_db_instance)
def get_db_instance_output(id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDBInstanceResult]:
    """
    Resource Type definition for AWS::DocDB::DBInstance
    """
    ...
