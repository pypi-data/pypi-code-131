# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PrivateZoneArgs', 'PrivateZone']

@pulumi.input_type
class PrivateZoneArgs:
    def __init__(__self__, *,
                 access_region_id: pulumi.Input[str],
                 cen_id: pulumi.Input[str],
                 host_region_id: pulumi.Input[str],
                 host_vpc_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a PrivateZone resource.
        :param pulumi.Input[str] access_region_id: The access region. The access region is the region of the cloud resource that accesses the PrivateZone service through CEN.
        :param pulumi.Input[str] cen_id: The ID of the CEN instance.
        :param pulumi.Input[str] host_region_id: The service region. The service region is the target region of the PrivateZone service to be accessed through CEN.
        :param pulumi.Input[str] host_vpc_id: The VPC that belongs to the service region.
        """
        pulumi.set(__self__, "access_region_id", access_region_id)
        pulumi.set(__self__, "cen_id", cen_id)
        pulumi.set(__self__, "host_region_id", host_region_id)
        pulumi.set(__self__, "host_vpc_id", host_vpc_id)

    @property
    @pulumi.getter(name="accessRegionId")
    def access_region_id(self) -> pulumi.Input[str]:
        """
        The access region. The access region is the region of the cloud resource that accesses the PrivateZone service through CEN.
        """
        return pulumi.get(self, "access_region_id")

    @access_region_id.setter
    def access_region_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_region_id", value)

    @property
    @pulumi.getter(name="cenId")
    def cen_id(self) -> pulumi.Input[str]:
        """
        The ID of the CEN instance.
        """
        return pulumi.get(self, "cen_id")

    @cen_id.setter
    def cen_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cen_id", value)

    @property
    @pulumi.getter(name="hostRegionId")
    def host_region_id(self) -> pulumi.Input[str]:
        """
        The service region. The service region is the target region of the PrivateZone service to be accessed through CEN.
        """
        return pulumi.get(self, "host_region_id")

    @host_region_id.setter
    def host_region_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "host_region_id", value)

    @property
    @pulumi.getter(name="hostVpcId")
    def host_vpc_id(self) -> pulumi.Input[str]:
        """
        The VPC that belongs to the service region.
        """
        return pulumi.get(self, "host_vpc_id")

    @host_vpc_id.setter
    def host_vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "host_vpc_id", value)


@pulumi.input_type
class _PrivateZoneState:
    def __init__(__self__, *,
                 access_region_id: Optional[pulumi.Input[str]] = None,
                 cen_id: Optional[pulumi.Input[str]] = None,
                 host_region_id: Optional[pulumi.Input[str]] = None,
                 host_vpc_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PrivateZone resources.
        :param pulumi.Input[str] access_region_id: The access region. The access region is the region of the cloud resource that accesses the PrivateZone service through CEN.
        :param pulumi.Input[str] cen_id: The ID of the CEN instance.
        :param pulumi.Input[str] host_region_id: The service region. The service region is the target region of the PrivateZone service to be accessed through CEN.
        :param pulumi.Input[str] host_vpc_id: The VPC that belongs to the service region.
        :param pulumi.Input[str] status: The status of the PrivateZone service. Valid values: ["Creating", "Active", "Deleting"].
        """
        if access_region_id is not None:
            pulumi.set(__self__, "access_region_id", access_region_id)
        if cen_id is not None:
            pulumi.set(__self__, "cen_id", cen_id)
        if host_region_id is not None:
            pulumi.set(__self__, "host_region_id", host_region_id)
        if host_vpc_id is not None:
            pulumi.set(__self__, "host_vpc_id", host_vpc_id)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="accessRegionId")
    def access_region_id(self) -> Optional[pulumi.Input[str]]:
        """
        The access region. The access region is the region of the cloud resource that accesses the PrivateZone service through CEN.
        """
        return pulumi.get(self, "access_region_id")

    @access_region_id.setter
    def access_region_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_region_id", value)

    @property
    @pulumi.getter(name="cenId")
    def cen_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the CEN instance.
        """
        return pulumi.get(self, "cen_id")

    @cen_id.setter
    def cen_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cen_id", value)

    @property
    @pulumi.getter(name="hostRegionId")
    def host_region_id(self) -> Optional[pulumi.Input[str]]:
        """
        The service region. The service region is the target region of the PrivateZone service to be accessed through CEN.
        """
        return pulumi.get(self, "host_region_id")

    @host_region_id.setter
    def host_region_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_region_id", value)

    @property
    @pulumi.getter(name="hostVpcId")
    def host_vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        The VPC that belongs to the service region.
        """
        return pulumi.get(self, "host_vpc_id")

    @host_vpc_id.setter
    def host_vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_vpc_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the PrivateZone service. Valid values: ["Creating", "Active", "Deleting"].
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class PrivateZone(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_region_id: Optional[pulumi.Input[str]] = None,
                 cen_id: Optional[pulumi.Input[str]] = None,
                 host_region_id: Optional[pulumi.Input[str]] = None,
                 host_vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This topic describes how to configure PrivateZone access.
        PrivateZone is a VPC-based resolution and management service for private domain names.
        After you set a PrivateZone access, the Cloud Connect Network (CCN) and Virtual Border Router (VBR) attached to a CEN instance can access the PrivateZone service through CEN.

        For information about CEN Private Zone and how to use it, see [Manage CEN Private Zone](https://www.alibabacloud.com/help/en/doc-detail/106693.htm).

        > **NOTE:** Available in 1.83.0+

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # Create a cen Private Zone resource and use it.
        default_instance = alicloud.cen.Instance("defaultInstance")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name="test_name",
            cidr_block="172.16.0.0/12")
        default_instance_attachment = alicloud.cen.InstanceAttachment("defaultInstanceAttachment",
            instance_id=default_instance.id,
            child_instance_id=default_network.id,
            child_instance_type="VPC",
            child_instance_region_id="cn-hangzhou",
            opts=pulumi.ResourceOptions(depends_on=[
                    default_instance,
                    default_network,
                ]))
        default_private_zone = alicloud.cen.PrivateZone("defaultPrivateZone",
            access_region_id="cn-hangzhou",
            cen_id=default_instance.id,
            host_region_id="cn-hangzhou",
            host_vpc_id=default_network.id,
            opts=pulumi.ResourceOptions(depends_on=[default_instance_attachment]))
        ```

        ## Import

        CEN Private Zone can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:cen/privateZone:PrivateZone example cen-abc123456:cn-hangzhou
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_region_id: The access region. The access region is the region of the cloud resource that accesses the PrivateZone service through CEN.
        :param pulumi.Input[str] cen_id: The ID of the CEN instance.
        :param pulumi.Input[str] host_region_id: The service region. The service region is the target region of the PrivateZone service to be accessed through CEN.
        :param pulumi.Input[str] host_vpc_id: The VPC that belongs to the service region.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateZoneArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This topic describes how to configure PrivateZone access.
        PrivateZone is a VPC-based resolution and management service for private domain names.
        After you set a PrivateZone access, the Cloud Connect Network (CCN) and Virtual Border Router (VBR) attached to a CEN instance can access the PrivateZone service through CEN.

        For information about CEN Private Zone and how to use it, see [Manage CEN Private Zone](https://www.alibabacloud.com/help/en/doc-detail/106693.htm).

        > **NOTE:** Available in 1.83.0+

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # Create a cen Private Zone resource and use it.
        default_instance = alicloud.cen.Instance("defaultInstance")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name="test_name",
            cidr_block="172.16.0.0/12")
        default_instance_attachment = alicloud.cen.InstanceAttachment("defaultInstanceAttachment",
            instance_id=default_instance.id,
            child_instance_id=default_network.id,
            child_instance_type="VPC",
            child_instance_region_id="cn-hangzhou",
            opts=pulumi.ResourceOptions(depends_on=[
                    default_instance,
                    default_network,
                ]))
        default_private_zone = alicloud.cen.PrivateZone("defaultPrivateZone",
            access_region_id="cn-hangzhou",
            cen_id=default_instance.id,
            host_region_id="cn-hangzhou",
            host_vpc_id=default_network.id,
            opts=pulumi.ResourceOptions(depends_on=[default_instance_attachment]))
        ```

        ## Import

        CEN Private Zone can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:cen/privateZone:PrivateZone example cen-abc123456:cn-hangzhou
        ```

        :param str resource_name: The name of the resource.
        :param PrivateZoneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateZoneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_region_id: Optional[pulumi.Input[str]] = None,
                 cen_id: Optional[pulumi.Input[str]] = None,
                 host_region_id: Optional[pulumi.Input[str]] = None,
                 host_vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateZoneArgs.__new__(PrivateZoneArgs)

            if access_region_id is None and not opts.urn:
                raise TypeError("Missing required property 'access_region_id'")
            __props__.__dict__["access_region_id"] = access_region_id
            if cen_id is None and not opts.urn:
                raise TypeError("Missing required property 'cen_id'")
            __props__.__dict__["cen_id"] = cen_id
            if host_region_id is None and not opts.urn:
                raise TypeError("Missing required property 'host_region_id'")
            __props__.__dict__["host_region_id"] = host_region_id
            if host_vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'host_vpc_id'")
            __props__.__dict__["host_vpc_id"] = host_vpc_id
            __props__.__dict__["status"] = None
        super(PrivateZone, __self__).__init__(
            'alicloud:cen/privateZone:PrivateZone',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_region_id: Optional[pulumi.Input[str]] = None,
            cen_id: Optional[pulumi.Input[str]] = None,
            host_region_id: Optional[pulumi.Input[str]] = None,
            host_vpc_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'PrivateZone':
        """
        Get an existing PrivateZone resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_region_id: The access region. The access region is the region of the cloud resource that accesses the PrivateZone service through CEN.
        :param pulumi.Input[str] cen_id: The ID of the CEN instance.
        :param pulumi.Input[str] host_region_id: The service region. The service region is the target region of the PrivateZone service to be accessed through CEN.
        :param pulumi.Input[str] host_vpc_id: The VPC that belongs to the service region.
        :param pulumi.Input[str] status: The status of the PrivateZone service. Valid values: ["Creating", "Active", "Deleting"].
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PrivateZoneState.__new__(_PrivateZoneState)

        __props__.__dict__["access_region_id"] = access_region_id
        __props__.__dict__["cen_id"] = cen_id
        __props__.__dict__["host_region_id"] = host_region_id
        __props__.__dict__["host_vpc_id"] = host_vpc_id
        __props__.__dict__["status"] = status
        return PrivateZone(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessRegionId")
    def access_region_id(self) -> pulumi.Output[str]:
        """
        The access region. The access region is the region of the cloud resource that accesses the PrivateZone service through CEN.
        """
        return pulumi.get(self, "access_region_id")

    @property
    @pulumi.getter(name="cenId")
    def cen_id(self) -> pulumi.Output[str]:
        """
        The ID of the CEN instance.
        """
        return pulumi.get(self, "cen_id")

    @property
    @pulumi.getter(name="hostRegionId")
    def host_region_id(self) -> pulumi.Output[str]:
        """
        The service region. The service region is the target region of the PrivateZone service to be accessed through CEN.
        """
        return pulumi.get(self, "host_region_id")

    @property
    @pulumi.getter(name="hostVpcId")
    def host_vpc_id(self) -> pulumi.Output[str]:
        """
        The VPC that belongs to the service region.
        """
        return pulumi.get(self, "host_vpc_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the PrivateZone service. Valid values: ["Creating", "Active", "Deleting"].
        """
        return pulumi.get(self, "status")

