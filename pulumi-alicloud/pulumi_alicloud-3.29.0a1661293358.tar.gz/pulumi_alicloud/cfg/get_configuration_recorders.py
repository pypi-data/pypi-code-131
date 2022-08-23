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
    'GetConfigurationRecordersResult',
    'AwaitableGetConfigurationRecordersResult',
    'get_configuration_recorders',
    'get_configuration_recorders_output',
]

@pulumi.output_type
class GetConfigurationRecordersResult:
    """
    A collection of values returned by getConfigurationRecorders.
    """
    def __init__(__self__, id=None, output_file=None, recorders=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if recorders and not isinstance(recorders, list):
            raise TypeError("Expected argument 'recorders' to be a list")
        pulumi.set(__self__, "recorders", recorders)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def recorders(self) -> Sequence['outputs.GetConfigurationRecordersRecorderResult']:
        """
        A list of Config Configuration Recorders. Each element contains the following attributes:
        """
        return pulumi.get(self, "recorders")


class AwaitableGetConfigurationRecordersResult(GetConfigurationRecordersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationRecordersResult(
            id=self.id,
            output_file=self.output_file,
            recorders=self.recorders)


def get_configuration_recorders(output_file: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationRecordersResult:
    """
    This data source provides the Config Configuration Recorders of the current Alibaba Cloud user.

    > **NOTE:**  Available in 1.99.0+.

    > **NOTE:** The Cloud Config region only support `cn-shanghai` and `ap-southeast-1`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.cfg.get_configuration_recorders()
    pulumi.export("listOfResourceTypes", data["alicloud_config_configuration_recorders"]["this"]["recorders"][0]["resource_types"])
    ```
    """
    __args__ = dict()
    __args__['outputFile'] = output_file
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:cfg/getConfigurationRecorders:getConfigurationRecorders', __args__, opts=opts, typ=GetConfigurationRecordersResult).value

    return AwaitableGetConfigurationRecordersResult(
        id=__ret__.id,
        output_file=__ret__.output_file,
        recorders=__ret__.recorders)


@_utilities.lift_output_func(get_configuration_recorders)
def get_configuration_recorders_output(output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigurationRecordersResult]:
    """
    This data source provides the Config Configuration Recorders of the current Alibaba Cloud user.

    > **NOTE:**  Available in 1.99.0+.

    > **NOTE:** The Cloud Config region only support `cn-shanghai` and `ap-southeast-1`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.cfg.get_configuration_recorders()
    pulumi.export("listOfResourceTypes", data["alicloud_config_configuration_recorders"]["this"]["recorders"][0]["resource_types"])
    ```
    """
    ...
