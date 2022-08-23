# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ClientVpnAuthorizationRuleArgs', 'ClientVpnAuthorizationRule']

@pulumi.input_type
class ClientVpnAuthorizationRuleArgs:
    def __init__(__self__, *,
                 client_vpn_endpoint_id: pulumi.Input[str],
                 target_network_cidr: pulumi.Input[str],
                 access_group_id: Optional[pulumi.Input[str]] = None,
                 authorize_all_groups: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ClientVpnAuthorizationRule resource.
        """
        pulumi.set(__self__, "client_vpn_endpoint_id", client_vpn_endpoint_id)
        pulumi.set(__self__, "target_network_cidr", target_network_cidr)
        if access_group_id is not None:
            pulumi.set(__self__, "access_group_id", access_group_id)
        if authorize_all_groups is not None:
            pulumi.set(__self__, "authorize_all_groups", authorize_all_groups)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "client_vpn_endpoint_id")

    @client_vpn_endpoint_id.setter
    def client_vpn_endpoint_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_vpn_endpoint_id", value)

    @property
    @pulumi.getter(name="targetNetworkCidr")
    def target_network_cidr(self) -> pulumi.Input[str]:
        return pulumi.get(self, "target_network_cidr")

    @target_network_cidr.setter
    def target_network_cidr(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_network_cidr", value)

    @property
    @pulumi.getter(name="accessGroupId")
    def access_group_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "access_group_id")

    @access_group_id.setter
    def access_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_group_id", value)

    @property
    @pulumi.getter(name="authorizeAllGroups")
    def authorize_all_groups(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "authorize_all_groups")

    @authorize_all_groups.setter
    def authorize_all_groups(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "authorize_all_groups", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


warnings.warn("""ClientVpnAuthorizationRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ClientVpnAuthorizationRule(pulumi.CustomResource):
    warnings.warn("""ClientVpnAuthorizationRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_group_id: Optional[pulumi.Input[str]] = None,
                 authorize_all_groups: Optional[pulumi.Input[bool]] = None,
                 client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 target_network_cidr: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::ClientVpnAuthorizationRule

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClientVpnAuthorizationRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::ClientVpnAuthorizationRule

        :param str resource_name: The name of the resource.
        :param ClientVpnAuthorizationRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClientVpnAuthorizationRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_group_id: Optional[pulumi.Input[str]] = None,
                 authorize_all_groups: Optional[pulumi.Input[bool]] = None,
                 client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 target_network_cidr: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""ClientVpnAuthorizationRule is deprecated: ClientVpnAuthorizationRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClientVpnAuthorizationRuleArgs.__new__(ClientVpnAuthorizationRuleArgs)

            __props__.__dict__["access_group_id"] = access_group_id
            __props__.__dict__["authorize_all_groups"] = authorize_all_groups
            if client_vpn_endpoint_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_vpn_endpoint_id'")
            __props__.__dict__["client_vpn_endpoint_id"] = client_vpn_endpoint_id
            __props__.__dict__["description"] = description
            if target_network_cidr is None and not opts.urn:
                raise TypeError("Missing required property 'target_network_cidr'")
            __props__.__dict__["target_network_cidr"] = target_network_cidr
        super(ClientVpnAuthorizationRule, __self__).__init__(
            'aws-native:ec2:ClientVpnAuthorizationRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ClientVpnAuthorizationRule':
        """
        Get an existing ClientVpnAuthorizationRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClientVpnAuthorizationRuleArgs.__new__(ClientVpnAuthorizationRuleArgs)

        __props__.__dict__["access_group_id"] = None
        __props__.__dict__["authorize_all_groups"] = None
        __props__.__dict__["client_vpn_endpoint_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["target_network_cidr"] = None
        return ClientVpnAuthorizationRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessGroupId")
    def access_group_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "access_group_id")

    @property
    @pulumi.getter(name="authorizeAllGroups")
    def authorize_all_groups(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "authorize_all_groups")

    @property
    @pulumi.getter(name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "client_vpn_endpoint_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="targetNetworkCidr")
    def target_network_cidr(self) -> pulumi.Output[str]:
        return pulumi.get(self, "target_network_cidr")

