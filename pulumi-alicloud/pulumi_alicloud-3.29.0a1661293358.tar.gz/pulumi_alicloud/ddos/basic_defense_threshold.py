# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BasicDefenseThresholdArgs', 'BasicDefenseThreshold']

@pulumi.input_type
class BasicDefenseThresholdArgs:
    def __init__(__self__, *,
                 ddos_type: pulumi.Input[str],
                 instance_id: pulumi.Input[str],
                 instance_type: pulumi.Input[str],
                 bps: Optional[pulumi.Input[int]] = None,
                 internet_ip: Optional[pulumi.Input[str]] = None,
                 is_auto: Optional[pulumi.Input[bool]] = None,
                 pps: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a BasicDefenseThreshold resource.
        :param pulumi.Input[str] ddos_type: The type of the threshold to query. Valid values: `defense`,`blackhole`.
               -`defense` - scrubbing threshold.
               -`blackhole` - DDoS mitigation threshold.
        :param pulumi.Input[str] instance_id: The ID of the instance.
        :param pulumi.Input[str] instance_type: The instance type of the public IP address asset. Value: `ecs`,`slb`,`eip`.
        :param pulumi.Input[int] bps: Specifies the traffic scrubbing threshold. Unit: Mbit/s. The traffic scrubbing threshold cannot exceed the peak inbound or outbound Internet traffic, whichever is larger, of the asset.
        :param pulumi.Input[str] internet_ip: The Internet IP address.
        :param pulumi.Input[bool] is_auto: Whether it is the system default threshold. Value:
               - `true`: indicates yes, that is, the DDoS protection service dynamically adjusts the cleaning threshold according to the traffic load of the cloud server.
               - `false`: indicates no, that is, you manually set the cleaning threshold.
        :param pulumi.Input[int] pps: The current message number cleaning threshold. Unit: pps.
        """
        pulumi.set(__self__, "ddos_type", ddos_type)
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "instance_type", instance_type)
        if bps is not None:
            pulumi.set(__self__, "bps", bps)
        if internet_ip is not None:
            pulumi.set(__self__, "internet_ip", internet_ip)
        if is_auto is not None:
            pulumi.set(__self__, "is_auto", is_auto)
        if pps is not None:
            pulumi.set(__self__, "pps", pps)

    @property
    @pulumi.getter(name="ddosType")
    def ddos_type(self) -> pulumi.Input[str]:
        """
        The type of the threshold to query. Valid values: `defense`,`blackhole`.
        -`defense` - scrubbing threshold.
        -`blackhole` - DDoS mitigation threshold.
        """
        return pulumi.get(self, "ddos_type")

    @ddos_type.setter
    def ddos_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "ddos_type", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[str]:
        """
        The instance type of the public IP address asset. Value: `ecs`,`slb`,`eip`.
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter
    def bps(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the traffic scrubbing threshold. Unit: Mbit/s. The traffic scrubbing threshold cannot exceed the peak inbound or outbound Internet traffic, whichever is larger, of the asset.
        """
        return pulumi.get(self, "bps")

    @bps.setter
    def bps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bps", value)

    @property
    @pulumi.getter(name="internetIp")
    def internet_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The Internet IP address.
        """
        return pulumi.get(self, "internet_ip")

    @internet_ip.setter
    def internet_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "internet_ip", value)

    @property
    @pulumi.getter(name="isAuto")
    def is_auto(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether it is the system default threshold. Value:
        - `true`: indicates yes, that is, the DDoS protection service dynamically adjusts the cleaning threshold according to the traffic load of the cloud server.
        - `false`: indicates no, that is, you manually set the cleaning threshold.
        """
        return pulumi.get(self, "is_auto")

    @is_auto.setter
    def is_auto(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_auto", value)

    @property
    @pulumi.getter
    def pps(self) -> Optional[pulumi.Input[int]]:
        """
        The current message number cleaning threshold. Unit: pps.
        """
        return pulumi.get(self, "pps")

    @pps.setter
    def pps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "pps", value)


@pulumi.input_type
class _BasicDefenseThresholdState:
    def __init__(__self__, *,
                 bps: Optional[pulumi.Input[int]] = None,
                 ddos_type: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 internet_ip: Optional[pulumi.Input[str]] = None,
                 is_auto: Optional[pulumi.Input[bool]] = None,
                 max_bps: Optional[pulumi.Input[int]] = None,
                 max_pps: Optional[pulumi.Input[int]] = None,
                 pps: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering BasicDefenseThreshold resources.
        :param pulumi.Input[int] bps: Specifies the traffic scrubbing threshold. Unit: Mbit/s. The traffic scrubbing threshold cannot exceed the peak inbound or outbound Internet traffic, whichever is larger, of the asset.
        :param pulumi.Input[str] ddos_type: The type of the threshold to query. Valid values: `defense`,`blackhole`.
               -`defense` - scrubbing threshold.
               -`blackhole` - DDoS mitigation threshold.
        :param pulumi.Input[str] instance_id: The ID of the instance.
        :param pulumi.Input[str] instance_type: The instance type of the public IP address asset. Value: `ecs`,`slb`,`eip`.
        :param pulumi.Input[str] internet_ip: The Internet IP address.
        :param pulumi.Input[bool] is_auto: Whether it is the system default threshold. Value:
               - `true`: indicates yes, that is, the DDoS protection service dynamically adjusts the cleaning threshold according to the traffic load of the cloud server.
               - `false`: indicates no, that is, you manually set the cleaning threshold.
        :param pulumi.Input[int] max_bps: The maximum traffic scrubbing threshold. Unit: Mbit/s.
        :param pulumi.Input[int] max_pps: The maximum packet scrubbing threshold. Unit: pps.
        :param pulumi.Input[int] pps: The current message number cleaning threshold. Unit: pps.
        """
        if bps is not None:
            pulumi.set(__self__, "bps", bps)
        if ddos_type is not None:
            pulumi.set(__self__, "ddos_type", ddos_type)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if instance_type is not None:
            pulumi.set(__self__, "instance_type", instance_type)
        if internet_ip is not None:
            pulumi.set(__self__, "internet_ip", internet_ip)
        if is_auto is not None:
            pulumi.set(__self__, "is_auto", is_auto)
        if max_bps is not None:
            pulumi.set(__self__, "max_bps", max_bps)
        if max_pps is not None:
            pulumi.set(__self__, "max_pps", max_pps)
        if pps is not None:
            pulumi.set(__self__, "pps", pps)

    @property
    @pulumi.getter
    def bps(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the traffic scrubbing threshold. Unit: Mbit/s. The traffic scrubbing threshold cannot exceed the peak inbound or outbound Internet traffic, whichever is larger, of the asset.
        """
        return pulumi.get(self, "bps")

    @bps.setter
    def bps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bps", value)

    @property
    @pulumi.getter(name="ddosType")
    def ddos_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the threshold to query. Valid values: `defense`,`blackhole`.
        -`defense` - scrubbing threshold.
        -`blackhole` - DDoS mitigation threshold.
        """
        return pulumi.get(self, "ddos_type")

    @ddos_type.setter
    def ddos_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ddos_type", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[str]]:
        """
        The instance type of the public IP address asset. Value: `ecs`,`slb`,`eip`.
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter(name="internetIp")
    def internet_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The Internet IP address.
        """
        return pulumi.get(self, "internet_ip")

    @internet_ip.setter
    def internet_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "internet_ip", value)

    @property
    @pulumi.getter(name="isAuto")
    def is_auto(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether it is the system default threshold. Value:
        - `true`: indicates yes, that is, the DDoS protection service dynamically adjusts the cleaning threshold according to the traffic load of the cloud server.
        - `false`: indicates no, that is, you manually set the cleaning threshold.
        """
        return pulumi.get(self, "is_auto")

    @is_auto.setter
    def is_auto(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_auto", value)

    @property
    @pulumi.getter(name="maxBps")
    def max_bps(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum traffic scrubbing threshold. Unit: Mbit/s.
        """
        return pulumi.get(self, "max_bps")

    @max_bps.setter
    def max_bps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_bps", value)

    @property
    @pulumi.getter(name="maxPps")
    def max_pps(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum packet scrubbing threshold. Unit: pps.
        """
        return pulumi.get(self, "max_pps")

    @max_pps.setter
    def max_pps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_pps", value)

    @property
    @pulumi.getter
    def pps(self) -> Optional[pulumi.Input[int]]:
        """
        The current message number cleaning threshold. Unit: pps.
        """
        return pulumi.get(self, "pps")

    @pps.setter
    def pps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "pps", value)


class BasicDefenseThreshold(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bps: Optional[pulumi.Input[int]] = None,
                 ddos_type: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 internet_ip: Optional[pulumi.Input[str]] = None,
                 is_auto: Optional[pulumi.Input[bool]] = None,
                 pps: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides a Ddos Basic defense threshold resource.

        For information about Ddos Basic Antiddos and how to use it, see [What is Defense Threshold](https://www.alibabacloud.com/help/en/ddos-protection/latest/modifydefensethreshold).

        > **NOTE:** Available in v1.168.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.ecs.EipAddress("default",
            address_name=var["name"],
            isp="BGP",
            internet_charge_type="PayByBandwidth",
            payment_type="PayAsYouGo")
        example = alicloud.ddos.BasicDefenseThreshold("example",
            instance_id=default.id,
            ddos_type="defense",
            instance_type="eip",
            bps=390,
            pps=90000)
        ```

        ## Import

        Ddos Basic Antiddos can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ddos/basicDefenseThreshold:BasicDefenseThreshold example <instance_id>:<instance_type>:<ddos_type>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] bps: Specifies the traffic scrubbing threshold. Unit: Mbit/s. The traffic scrubbing threshold cannot exceed the peak inbound or outbound Internet traffic, whichever is larger, of the asset.
        :param pulumi.Input[str] ddos_type: The type of the threshold to query. Valid values: `defense`,`blackhole`.
               -`defense` - scrubbing threshold.
               -`blackhole` - DDoS mitigation threshold.
        :param pulumi.Input[str] instance_id: The ID of the instance.
        :param pulumi.Input[str] instance_type: The instance type of the public IP address asset. Value: `ecs`,`slb`,`eip`.
        :param pulumi.Input[str] internet_ip: The Internet IP address.
        :param pulumi.Input[bool] is_auto: Whether it is the system default threshold. Value:
               - `true`: indicates yes, that is, the DDoS protection service dynamically adjusts the cleaning threshold according to the traffic load of the cloud server.
               - `false`: indicates no, that is, you manually set the cleaning threshold.
        :param pulumi.Input[int] pps: The current message number cleaning threshold. Unit: pps.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BasicDefenseThresholdArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Ddos Basic defense threshold resource.

        For information about Ddos Basic Antiddos and how to use it, see [What is Defense Threshold](https://www.alibabacloud.com/help/en/ddos-protection/latest/modifydefensethreshold).

        > **NOTE:** Available in v1.168.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.ecs.EipAddress("default",
            address_name=var["name"],
            isp="BGP",
            internet_charge_type="PayByBandwidth",
            payment_type="PayAsYouGo")
        example = alicloud.ddos.BasicDefenseThreshold("example",
            instance_id=default.id,
            ddos_type="defense",
            instance_type="eip",
            bps=390,
            pps=90000)
        ```

        ## Import

        Ddos Basic Antiddos can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ddos/basicDefenseThreshold:BasicDefenseThreshold example <instance_id>:<instance_type>:<ddos_type>
        ```

        :param str resource_name: The name of the resource.
        :param BasicDefenseThresholdArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BasicDefenseThresholdArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bps: Optional[pulumi.Input[int]] = None,
                 ddos_type: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 internet_ip: Optional[pulumi.Input[str]] = None,
                 is_auto: Optional[pulumi.Input[bool]] = None,
                 pps: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BasicDefenseThresholdArgs.__new__(BasicDefenseThresholdArgs)

            __props__.__dict__["bps"] = bps
            if ddos_type is None and not opts.urn:
                raise TypeError("Missing required property 'ddos_type'")
            __props__.__dict__["ddos_type"] = ddos_type
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if instance_type is None and not opts.urn:
                raise TypeError("Missing required property 'instance_type'")
            __props__.__dict__["instance_type"] = instance_type
            __props__.__dict__["internet_ip"] = internet_ip
            __props__.__dict__["is_auto"] = is_auto
            __props__.__dict__["pps"] = pps
            __props__.__dict__["max_bps"] = None
            __props__.__dict__["max_pps"] = None
        super(BasicDefenseThreshold, __self__).__init__(
            'alicloud:ddos/basicDefenseThreshold:BasicDefenseThreshold',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bps: Optional[pulumi.Input[int]] = None,
            ddos_type: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            instance_type: Optional[pulumi.Input[str]] = None,
            internet_ip: Optional[pulumi.Input[str]] = None,
            is_auto: Optional[pulumi.Input[bool]] = None,
            max_bps: Optional[pulumi.Input[int]] = None,
            max_pps: Optional[pulumi.Input[int]] = None,
            pps: Optional[pulumi.Input[int]] = None) -> 'BasicDefenseThreshold':
        """
        Get an existing BasicDefenseThreshold resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] bps: Specifies the traffic scrubbing threshold. Unit: Mbit/s. The traffic scrubbing threshold cannot exceed the peak inbound or outbound Internet traffic, whichever is larger, of the asset.
        :param pulumi.Input[str] ddos_type: The type of the threshold to query. Valid values: `defense`,`blackhole`.
               -`defense` - scrubbing threshold.
               -`blackhole` - DDoS mitigation threshold.
        :param pulumi.Input[str] instance_id: The ID of the instance.
        :param pulumi.Input[str] instance_type: The instance type of the public IP address asset. Value: `ecs`,`slb`,`eip`.
        :param pulumi.Input[str] internet_ip: The Internet IP address.
        :param pulumi.Input[bool] is_auto: Whether it is the system default threshold. Value:
               - `true`: indicates yes, that is, the DDoS protection service dynamically adjusts the cleaning threshold according to the traffic load of the cloud server.
               - `false`: indicates no, that is, you manually set the cleaning threshold.
        :param pulumi.Input[int] max_bps: The maximum traffic scrubbing threshold. Unit: Mbit/s.
        :param pulumi.Input[int] max_pps: The maximum packet scrubbing threshold. Unit: pps.
        :param pulumi.Input[int] pps: The current message number cleaning threshold. Unit: pps.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BasicDefenseThresholdState.__new__(_BasicDefenseThresholdState)

        __props__.__dict__["bps"] = bps
        __props__.__dict__["ddos_type"] = ddos_type
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["instance_type"] = instance_type
        __props__.__dict__["internet_ip"] = internet_ip
        __props__.__dict__["is_auto"] = is_auto
        __props__.__dict__["max_bps"] = max_bps
        __props__.__dict__["max_pps"] = max_pps
        __props__.__dict__["pps"] = pps
        return BasicDefenseThreshold(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bps(self) -> pulumi.Output[int]:
        """
        Specifies the traffic scrubbing threshold. Unit: Mbit/s. The traffic scrubbing threshold cannot exceed the peak inbound or outbound Internet traffic, whichever is larger, of the asset.
        """
        return pulumi.get(self, "bps")

    @property
    @pulumi.getter(name="ddosType")
    def ddos_type(self) -> pulumi.Output[str]:
        """
        The type of the threshold to query. Valid values: `defense`,`blackhole`.
        -`defense` - scrubbing threshold.
        -`blackhole` - DDoS mitigation threshold.
        """
        return pulumi.get(self, "ddos_type")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[str]:
        """
        The instance type of the public IP address asset. Value: `ecs`,`slb`,`eip`.
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="internetIp")
    def internet_ip(self) -> pulumi.Output[str]:
        """
        The Internet IP address.
        """
        return pulumi.get(self, "internet_ip")

    @property
    @pulumi.getter(name="isAuto")
    def is_auto(self) -> pulumi.Output[bool]:
        """
        Whether it is the system default threshold. Value:
        - `true`: indicates yes, that is, the DDoS protection service dynamically adjusts the cleaning threshold according to the traffic load of the cloud server.
        - `false`: indicates no, that is, you manually set the cleaning threshold.
        """
        return pulumi.get(self, "is_auto")

    @property
    @pulumi.getter(name="maxBps")
    def max_bps(self) -> pulumi.Output[int]:
        """
        The maximum traffic scrubbing threshold. Unit: Mbit/s.
        """
        return pulumi.get(self, "max_bps")

    @property
    @pulumi.getter(name="maxPps")
    def max_pps(self) -> pulumi.Output[int]:
        """
        The maximum packet scrubbing threshold. Unit: pps.
        """
        return pulumi.get(self, "max_pps")

    @property
    @pulumi.getter
    def pps(self) -> pulumi.Output[int]:
        """
        The current message number cleaning threshold. Unit: pps.
        """
        return pulumi.get(self, "pps")

