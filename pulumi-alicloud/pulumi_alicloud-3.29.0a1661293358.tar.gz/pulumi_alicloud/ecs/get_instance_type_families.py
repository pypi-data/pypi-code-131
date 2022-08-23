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
    'GetInstanceTypeFamiliesResult',
    'AwaitableGetInstanceTypeFamiliesResult',
    'get_instance_type_families',
    'get_instance_type_families_output',
]

@pulumi.output_type
class GetInstanceTypeFamiliesResult:
    """
    A collection of values returned by getInstanceTypeFamilies.
    """
    def __init__(__self__, families=None, generation=None, id=None, ids=None, instance_charge_type=None, output_file=None, spot_strategy=None, zone_id=None):
        if families and not isinstance(families, list):
            raise TypeError("Expected argument 'families' to be a list")
        pulumi.set(__self__, "families", families)
        if generation and not isinstance(generation, str):
            raise TypeError("Expected argument 'generation' to be a str")
        pulumi.set(__self__, "generation", generation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_charge_type and not isinstance(instance_charge_type, str):
            raise TypeError("Expected argument 'instance_charge_type' to be a str")
        pulumi.set(__self__, "instance_charge_type", instance_charge_type)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if spot_strategy and not isinstance(spot_strategy, str):
            raise TypeError("Expected argument 'spot_strategy' to be a str")
        pulumi.set(__self__, "spot_strategy", spot_strategy)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def families(self) -> Sequence['outputs.GetInstanceTypeFamiliesFamilyResult']:
        return pulumi.get(self, "families")

    @property
    @pulumi.getter
    def generation(self) -> Optional[str]:
        """
        The generation of the instance type family.
        """
        return pulumi.get(self, "generation")

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
        A list of instance type family IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="instanceChargeType")
    def instance_charge_type(self) -> Optional[str]:
        return pulumi.get(self, "instance_charge_type")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="spotStrategy")
    def spot_strategy(self) -> Optional[str]:
        return pulumi.get(self, "spot_strategy")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[str]:
        return pulumi.get(self, "zone_id")


class AwaitableGetInstanceTypeFamiliesResult(GetInstanceTypeFamiliesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceTypeFamiliesResult(
            families=self.families,
            generation=self.generation,
            id=self.id,
            ids=self.ids,
            instance_charge_type=self.instance_charge_type,
            output_file=self.output_file,
            spot_strategy=self.spot_strategy,
            zone_id=self.zone_id)


def get_instance_type_families(generation: Optional[str] = None,
                               instance_charge_type: Optional[str] = None,
                               output_file: Optional[str] = None,
                               spot_strategy: Optional[str] = None,
                               zone_id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceTypeFamiliesResult:
    """
    This data source provides the ECS instance type families of Alibaba Cloud.

    > **NOTE:** Available in 1.54.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.ecs.get_instance_type_families(instance_charge_type="PrePaid")
    pulumi.export("firstInstanceTypeFamilyId", default.families[0].id)
    pulumi.export("instanceIds", default.ids)
    ```


    :param str generation: The generation of the instance type family, Valid values: `ecs-1`, `ecs-2`, `ecs-3` and `ecs-4`. For more information, see [Instance type families](https://www.alibabacloud.com/help/doc-detail/25378.htm).
    :param str instance_charge_type: Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`.
    :param str spot_strategy: Filter the results by ECS spot type. Valid values: `NoSpot`, `SpotWithPriceLimit` and `SpotAsPriceGo`. Default to `NoSpot`.
    :param str zone_id: The Zone to launch the instance.
    """
    __args__ = dict()
    __args__['generation'] = generation
    __args__['instanceChargeType'] = instance_charge_type
    __args__['outputFile'] = output_file
    __args__['spotStrategy'] = spot_strategy
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:ecs/getInstanceTypeFamilies:getInstanceTypeFamilies', __args__, opts=opts, typ=GetInstanceTypeFamiliesResult).value

    return AwaitableGetInstanceTypeFamiliesResult(
        families=__ret__.families,
        generation=__ret__.generation,
        id=__ret__.id,
        ids=__ret__.ids,
        instance_charge_type=__ret__.instance_charge_type,
        output_file=__ret__.output_file,
        spot_strategy=__ret__.spot_strategy,
        zone_id=__ret__.zone_id)


@_utilities.lift_output_func(get_instance_type_families)
def get_instance_type_families_output(generation: Optional[pulumi.Input[Optional[str]]] = None,
                                      instance_charge_type: Optional[pulumi.Input[Optional[str]]] = None,
                                      output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                      spot_strategy: Optional[pulumi.Input[Optional[str]]] = None,
                                      zone_id: Optional[pulumi.Input[Optional[str]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceTypeFamiliesResult]:
    """
    This data source provides the ECS instance type families of Alibaba Cloud.

    > **NOTE:** Available in 1.54.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.ecs.get_instance_type_families(instance_charge_type="PrePaid")
    pulumi.export("firstInstanceTypeFamilyId", default.families[0].id)
    pulumi.export("instanceIds", default.ids)
    ```


    :param str generation: The generation of the instance type family, Valid values: `ecs-1`, `ecs-2`, `ecs-3` and `ecs-4`. For more information, see [Instance type families](https://www.alibabacloud.com/help/doc-detail/25378.htm).
    :param str instance_charge_type: Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`.
    :param str spot_strategy: Filter the results by ECS spot type. Valid values: `NoSpot`, `SpotWithPriceLimit` and `SpotAsPriceGo`. Default to `NoSpot`.
    :param str zone_id: The Zone to launch the instance.
    """
    ...
