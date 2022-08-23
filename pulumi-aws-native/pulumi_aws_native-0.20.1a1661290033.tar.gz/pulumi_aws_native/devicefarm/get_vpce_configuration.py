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
    'GetVPCEConfigurationResult',
    'AwaitableGetVPCEConfigurationResult',
    'get_vpce_configuration',
    'get_vpce_configuration_output',
]

@pulumi.output_type
class GetVPCEConfigurationResult:
    def __init__(__self__, arn=None, service_dns_name=None, tags=None, vpce_configuration_description=None, vpce_configuration_name=None, vpce_service_name=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if service_dns_name and not isinstance(service_dns_name, str):
            raise TypeError("Expected argument 'service_dns_name' to be a str")
        pulumi.set(__self__, "service_dns_name", service_dns_name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if vpce_configuration_description and not isinstance(vpce_configuration_description, str):
            raise TypeError("Expected argument 'vpce_configuration_description' to be a str")
        pulumi.set(__self__, "vpce_configuration_description", vpce_configuration_description)
        if vpce_configuration_name and not isinstance(vpce_configuration_name, str):
            raise TypeError("Expected argument 'vpce_configuration_name' to be a str")
        pulumi.set(__self__, "vpce_configuration_name", vpce_configuration_name)
        if vpce_service_name and not isinstance(vpce_service_name, str):
            raise TypeError("Expected argument 'vpce_service_name' to be a str")
        pulumi.set(__self__, "vpce_service_name", vpce_service_name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[str]:
        return pulumi.get(self, "service_dns_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.VPCEConfigurationTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpceConfigurationDescription")
    def vpce_configuration_description(self) -> Optional[str]:
        return pulumi.get(self, "vpce_configuration_description")

    @property
    @pulumi.getter(name="vpceConfigurationName")
    def vpce_configuration_name(self) -> Optional[str]:
        return pulumi.get(self, "vpce_configuration_name")

    @property
    @pulumi.getter(name="vpceServiceName")
    def vpce_service_name(self) -> Optional[str]:
        return pulumi.get(self, "vpce_service_name")


class AwaitableGetVPCEConfigurationResult(GetVPCEConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVPCEConfigurationResult(
            arn=self.arn,
            service_dns_name=self.service_dns_name,
            tags=self.tags,
            vpce_configuration_description=self.vpce_configuration_description,
            vpce_configuration_name=self.vpce_configuration_name,
            vpce_service_name=self.vpce_service_name)


def get_vpce_configuration(arn: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVPCEConfigurationResult:
    """
    AWS::DeviceFarm::VPCEConfiguration creates a new Device Farm VPCE Configuration
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:devicefarm:getVPCEConfiguration', __args__, opts=opts, typ=GetVPCEConfigurationResult).value

    return AwaitableGetVPCEConfigurationResult(
        arn=__ret__.arn,
        service_dns_name=__ret__.service_dns_name,
        tags=__ret__.tags,
        vpce_configuration_description=__ret__.vpce_configuration_description,
        vpce_configuration_name=__ret__.vpce_configuration_name,
        vpce_service_name=__ret__.vpce_service_name)


@_utilities.lift_output_func(get_vpce_configuration)
def get_vpce_configuration_output(arn: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVPCEConfigurationResult]:
    """
    AWS::DeviceFarm::VPCEConfiguration creates a new Device Farm VPCE Configuration
    """
    ...
