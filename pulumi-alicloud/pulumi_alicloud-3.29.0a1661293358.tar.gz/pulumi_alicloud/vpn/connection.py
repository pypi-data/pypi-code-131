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
from ._inputs import *

__all__ = ['ConnectionArgs', 'Connection']

@pulumi.input_type
class ConnectionArgs:
    def __init__(__self__, *,
                 customer_gateway_id: pulumi.Input[str],
                 local_subnets: pulumi.Input[Sequence[pulumi.Input[str]]],
                 remote_subnets: pulumi.Input[Sequence[pulumi.Input[str]]],
                 vpn_gateway_id: pulumi.Input[str],
                 bgp_config: Optional[pulumi.Input['ConnectionBgpConfigArgs']] = None,
                 effect_immediately: Optional[pulumi.Input[bool]] = None,
                 enable_dpd: Optional[pulumi.Input[bool]] = None,
                 enable_nat_traversal: Optional[pulumi.Input[bool]] = None,
                 health_check_config: Optional[pulumi.Input['ConnectionHealthCheckConfigArgs']] = None,
                 ike_config: Optional[pulumi.Input['ConnectionIkeConfigArgs']] = None,
                 ipsec_config: Optional[pulumi.Input['ConnectionIpsecConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Connection resource.
        :param pulumi.Input[str] customer_gateway_id: The ID of the customer gateway.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] local_subnets: The CIDR block of the VPC to be connected with the local data center. This parameter is used for phase-two negotiation.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] remote_subnets: The CIDR block of the local data center. This parameter is used for phase-two negotiation.
        :param pulumi.Input[str] vpn_gateway_id: The ID of the VPN gateway.
        :param pulumi.Input['ConnectionBgpConfigArgs'] bgp_config: The configurations of the BGP routing protocol. See the following `Block bgp_config`.
        :param pulumi.Input[bool] effect_immediately: Whether to delete a successfully negotiated IPsec tunnel and initiate a negotiation again. Valid value:true,false.
        :param pulumi.Input[bool] enable_dpd: Whether to enable NAT traversal.
        :param pulumi.Input[bool] enable_nat_traversal: Whether to enable NAT traversal.
        :param pulumi.Input['ConnectionHealthCheckConfigArgs'] health_check_config: The health check configurations. See the following `Block health_check_config`.
        :param pulumi.Input['ConnectionIkeConfigArgs'] ike_config: The configurations of phase-one negotiation. See the following `Block ike_config`.
        :param pulumi.Input['ConnectionIpsecConfigArgs'] ipsec_config: The configurations of phase-two negotiation. See the following `Block ipsec_config`.
        :param pulumi.Input[str] name: The name of the IPsec connection.
        """
        pulumi.set(__self__, "customer_gateway_id", customer_gateway_id)
        pulumi.set(__self__, "local_subnets", local_subnets)
        pulumi.set(__self__, "remote_subnets", remote_subnets)
        pulumi.set(__self__, "vpn_gateway_id", vpn_gateway_id)
        if bgp_config is not None:
            pulumi.set(__self__, "bgp_config", bgp_config)
        if effect_immediately is not None:
            pulumi.set(__self__, "effect_immediately", effect_immediately)
        if enable_dpd is not None:
            pulumi.set(__self__, "enable_dpd", enable_dpd)
        if enable_nat_traversal is not None:
            pulumi.set(__self__, "enable_nat_traversal", enable_nat_traversal)
        if health_check_config is not None:
            pulumi.set(__self__, "health_check_config", health_check_config)
        if ike_config is not None:
            pulumi.set(__self__, "ike_config", ike_config)
        if ipsec_config is not None:
            pulumi.set(__self__, "ipsec_config", ipsec_config)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="customerGatewayId")
    def customer_gateway_id(self) -> pulumi.Input[str]:
        """
        The ID of the customer gateway.
        """
        return pulumi.get(self, "customer_gateway_id")

    @customer_gateway_id.setter
    def customer_gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "customer_gateway_id", value)

    @property
    @pulumi.getter(name="localSubnets")
    def local_subnets(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The CIDR block of the VPC to be connected with the local data center. This parameter is used for phase-two negotiation.
        """
        return pulumi.get(self, "local_subnets")

    @local_subnets.setter
    def local_subnets(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "local_subnets", value)

    @property
    @pulumi.getter(name="remoteSubnets")
    def remote_subnets(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The CIDR block of the local data center. This parameter is used for phase-two negotiation.
        """
        return pulumi.get(self, "remote_subnets")

    @remote_subnets.setter
    def remote_subnets(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "remote_subnets", value)

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> pulumi.Input[str]:
        """
        The ID of the VPN gateway.
        """
        return pulumi.get(self, "vpn_gateway_id")

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpn_gateway_id", value)

    @property
    @pulumi.getter(name="bgpConfig")
    def bgp_config(self) -> Optional[pulumi.Input['ConnectionBgpConfigArgs']]:
        """
        The configurations of the BGP routing protocol. See the following `Block bgp_config`.
        """
        return pulumi.get(self, "bgp_config")

    @bgp_config.setter
    def bgp_config(self, value: Optional[pulumi.Input['ConnectionBgpConfigArgs']]):
        pulumi.set(self, "bgp_config", value)

    @property
    @pulumi.getter(name="effectImmediately")
    def effect_immediately(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to delete a successfully negotiated IPsec tunnel and initiate a negotiation again. Valid value:true,false.
        """
        return pulumi.get(self, "effect_immediately")

    @effect_immediately.setter
    def effect_immediately(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "effect_immediately", value)

    @property
    @pulumi.getter(name="enableDpd")
    def enable_dpd(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable NAT traversal.
        """
        return pulumi.get(self, "enable_dpd")

    @enable_dpd.setter
    def enable_dpd(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_dpd", value)

    @property
    @pulumi.getter(name="enableNatTraversal")
    def enable_nat_traversal(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable NAT traversal.
        """
        return pulumi.get(self, "enable_nat_traversal")

    @enable_nat_traversal.setter
    def enable_nat_traversal(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_nat_traversal", value)

    @property
    @pulumi.getter(name="healthCheckConfig")
    def health_check_config(self) -> Optional[pulumi.Input['ConnectionHealthCheckConfigArgs']]:
        """
        The health check configurations. See the following `Block health_check_config`.
        """
        return pulumi.get(self, "health_check_config")

    @health_check_config.setter
    def health_check_config(self, value: Optional[pulumi.Input['ConnectionHealthCheckConfigArgs']]):
        pulumi.set(self, "health_check_config", value)

    @property
    @pulumi.getter(name="ikeConfig")
    def ike_config(self) -> Optional[pulumi.Input['ConnectionIkeConfigArgs']]:
        """
        The configurations of phase-one negotiation. See the following `Block ike_config`.
        """
        return pulumi.get(self, "ike_config")

    @ike_config.setter
    def ike_config(self, value: Optional[pulumi.Input['ConnectionIkeConfigArgs']]):
        pulumi.set(self, "ike_config", value)

    @property
    @pulumi.getter(name="ipsecConfig")
    def ipsec_config(self) -> Optional[pulumi.Input['ConnectionIpsecConfigArgs']]:
        """
        The configurations of phase-two negotiation. See the following `Block ipsec_config`.
        """
        return pulumi.get(self, "ipsec_config")

    @ipsec_config.setter
    def ipsec_config(self, value: Optional[pulumi.Input['ConnectionIpsecConfigArgs']]):
        pulumi.set(self, "ipsec_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the IPsec connection.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ConnectionState:
    def __init__(__self__, *,
                 bgp_config: Optional[pulumi.Input['ConnectionBgpConfigArgs']] = None,
                 customer_gateway_id: Optional[pulumi.Input[str]] = None,
                 effect_immediately: Optional[pulumi.Input[bool]] = None,
                 enable_dpd: Optional[pulumi.Input[bool]] = None,
                 enable_nat_traversal: Optional[pulumi.Input[bool]] = None,
                 health_check_config: Optional[pulumi.Input['ConnectionHealthCheckConfigArgs']] = None,
                 ike_config: Optional[pulumi.Input['ConnectionIkeConfigArgs']] = None,
                 ipsec_config: Optional[pulumi.Input['ConnectionIpsecConfigArgs']] = None,
                 local_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remote_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 vpn_gateway_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Connection resources.
        :param pulumi.Input['ConnectionBgpConfigArgs'] bgp_config: The configurations of the BGP routing protocol. See the following `Block bgp_config`.
        :param pulumi.Input[str] customer_gateway_id: The ID of the customer gateway.
        :param pulumi.Input[bool] effect_immediately: Whether to delete a successfully negotiated IPsec tunnel and initiate a negotiation again. Valid value:true,false.
        :param pulumi.Input[bool] enable_dpd: Whether to enable NAT traversal.
        :param pulumi.Input[bool] enable_nat_traversal: Whether to enable NAT traversal.
        :param pulumi.Input['ConnectionHealthCheckConfigArgs'] health_check_config: The health check configurations. See the following `Block health_check_config`.
        :param pulumi.Input['ConnectionIkeConfigArgs'] ike_config: The configurations of phase-one negotiation. See the following `Block ike_config`.
        :param pulumi.Input['ConnectionIpsecConfigArgs'] ipsec_config: The configurations of phase-two negotiation. See the following `Block ipsec_config`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] local_subnets: The CIDR block of the VPC to be connected with the local data center. This parameter is used for phase-two negotiation.
        :param pulumi.Input[str] name: The name of the IPsec connection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] remote_subnets: The CIDR block of the local data center. This parameter is used for phase-two negotiation.
        :param pulumi.Input[str] status: The status of VPN connection.
        :param pulumi.Input[str] vpn_gateway_id: The ID of the VPN gateway.
        """
        if bgp_config is not None:
            pulumi.set(__self__, "bgp_config", bgp_config)
        if customer_gateway_id is not None:
            pulumi.set(__self__, "customer_gateway_id", customer_gateway_id)
        if effect_immediately is not None:
            pulumi.set(__self__, "effect_immediately", effect_immediately)
        if enable_dpd is not None:
            pulumi.set(__self__, "enable_dpd", enable_dpd)
        if enable_nat_traversal is not None:
            pulumi.set(__self__, "enable_nat_traversal", enable_nat_traversal)
        if health_check_config is not None:
            pulumi.set(__self__, "health_check_config", health_check_config)
        if ike_config is not None:
            pulumi.set(__self__, "ike_config", ike_config)
        if ipsec_config is not None:
            pulumi.set(__self__, "ipsec_config", ipsec_config)
        if local_subnets is not None:
            pulumi.set(__self__, "local_subnets", local_subnets)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if remote_subnets is not None:
            pulumi.set(__self__, "remote_subnets", remote_subnets)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if vpn_gateway_id is not None:
            pulumi.set(__self__, "vpn_gateway_id", vpn_gateway_id)

    @property
    @pulumi.getter(name="bgpConfig")
    def bgp_config(self) -> Optional[pulumi.Input['ConnectionBgpConfigArgs']]:
        """
        The configurations of the BGP routing protocol. See the following `Block bgp_config`.
        """
        return pulumi.get(self, "bgp_config")

    @bgp_config.setter
    def bgp_config(self, value: Optional[pulumi.Input['ConnectionBgpConfigArgs']]):
        pulumi.set(self, "bgp_config", value)

    @property
    @pulumi.getter(name="customerGatewayId")
    def customer_gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the customer gateway.
        """
        return pulumi.get(self, "customer_gateway_id")

    @customer_gateway_id.setter
    def customer_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_gateway_id", value)

    @property
    @pulumi.getter(name="effectImmediately")
    def effect_immediately(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to delete a successfully negotiated IPsec tunnel and initiate a negotiation again. Valid value:true,false.
        """
        return pulumi.get(self, "effect_immediately")

    @effect_immediately.setter
    def effect_immediately(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "effect_immediately", value)

    @property
    @pulumi.getter(name="enableDpd")
    def enable_dpd(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable NAT traversal.
        """
        return pulumi.get(self, "enable_dpd")

    @enable_dpd.setter
    def enable_dpd(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_dpd", value)

    @property
    @pulumi.getter(name="enableNatTraversal")
    def enable_nat_traversal(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable NAT traversal.
        """
        return pulumi.get(self, "enable_nat_traversal")

    @enable_nat_traversal.setter
    def enable_nat_traversal(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_nat_traversal", value)

    @property
    @pulumi.getter(name="healthCheckConfig")
    def health_check_config(self) -> Optional[pulumi.Input['ConnectionHealthCheckConfigArgs']]:
        """
        The health check configurations. See the following `Block health_check_config`.
        """
        return pulumi.get(self, "health_check_config")

    @health_check_config.setter
    def health_check_config(self, value: Optional[pulumi.Input['ConnectionHealthCheckConfigArgs']]):
        pulumi.set(self, "health_check_config", value)

    @property
    @pulumi.getter(name="ikeConfig")
    def ike_config(self) -> Optional[pulumi.Input['ConnectionIkeConfigArgs']]:
        """
        The configurations of phase-one negotiation. See the following `Block ike_config`.
        """
        return pulumi.get(self, "ike_config")

    @ike_config.setter
    def ike_config(self, value: Optional[pulumi.Input['ConnectionIkeConfigArgs']]):
        pulumi.set(self, "ike_config", value)

    @property
    @pulumi.getter(name="ipsecConfig")
    def ipsec_config(self) -> Optional[pulumi.Input['ConnectionIpsecConfigArgs']]:
        """
        The configurations of phase-two negotiation. See the following `Block ipsec_config`.
        """
        return pulumi.get(self, "ipsec_config")

    @ipsec_config.setter
    def ipsec_config(self, value: Optional[pulumi.Input['ConnectionIpsecConfigArgs']]):
        pulumi.set(self, "ipsec_config", value)

    @property
    @pulumi.getter(name="localSubnets")
    def local_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The CIDR block of the VPC to be connected with the local data center. This parameter is used for phase-two negotiation.
        """
        return pulumi.get(self, "local_subnets")

    @local_subnets.setter
    def local_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "local_subnets", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the IPsec connection.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="remoteSubnets")
    def remote_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The CIDR block of the local data center. This parameter is used for phase-two negotiation.
        """
        return pulumi.get(self, "remote_subnets")

    @remote_subnets.setter
    def remote_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "remote_subnets", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of VPN connection.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the VPN gateway.
        """
        return pulumi.get(self, "vpn_gateway_id")

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpn_gateway_id", value)


class Connection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_config: Optional[pulumi.Input[pulumi.InputType['ConnectionBgpConfigArgs']]] = None,
                 customer_gateway_id: Optional[pulumi.Input[str]] = None,
                 effect_immediately: Optional[pulumi.Input[bool]] = None,
                 enable_dpd: Optional[pulumi.Input[bool]] = None,
                 enable_nat_traversal: Optional[pulumi.Input[bool]] = None,
                 health_check_config: Optional[pulumi.Input[pulumi.InputType['ConnectionHealthCheckConfigArgs']]] = None,
                 ike_config: Optional[pulumi.Input[pulumi.InputType['ConnectionIkeConfigArgs']]] = None,
                 ipsec_config: Optional[pulumi.Input[pulumi.InputType['ConnectionIpsecConfigArgs']]] = None,
                 local_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remote_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpn_gateway_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        foo_gateway = alicloud.vpn.Gateway("fooGateway",
            vpc_id="vpc-fake-id",
            bandwidth=10,
            enable_ssl=True,
            instance_charge_type="PostPaid",
            description="test_create_description")
        foo_customer_gateway = alicloud.vpn.CustomerGateway("fooCustomerGateway",
            ip_address="42.104.22.228",
            description="testAccVpnCgwDesc")
        foo_connection = alicloud.vpn.Connection("fooConnection",
            vpn_gateway_id=foo_gateway.id,
            customer_gateway_id=foo_customer_gateway.id,
            local_subnets=[
                "172.16.0.0/24",
                "172.16.1.0/24",
            ],
            remote_subnets=[
                "10.0.0.0/24",
                "10.0.1.0/24",
            ],
            effect_immediately=True,
            ike_config=alicloud.vpn.ConnectionIkeConfigArgs(
                ike_auth_alg="md5",
                ike_enc_alg="des",
                ike_version="ikev1",
                ike_mode="main",
                ike_lifetime=86400,
                psk="tf-testvpn2",
                ike_pfs="group1",
                ike_remote_id="testbob2",
                ike_local_id="testalice2",
            ),
            ipsec_config=alicloud.vpn.ConnectionIpsecConfigArgs(
                ipsec_pfs="group5",
                ipsec_enc_alg="des",
                ipsec_auth_alg="md5",
                ipsec_lifetime=8640,
            ))
        ```

        ## Import

        VPN connection can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:vpn/connection:Connection example vco-abc123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ConnectionBgpConfigArgs']] bgp_config: The configurations of the BGP routing protocol. See the following `Block bgp_config`.
        :param pulumi.Input[str] customer_gateway_id: The ID of the customer gateway.
        :param pulumi.Input[bool] effect_immediately: Whether to delete a successfully negotiated IPsec tunnel and initiate a negotiation again. Valid value:true,false.
        :param pulumi.Input[bool] enable_dpd: Whether to enable NAT traversal.
        :param pulumi.Input[bool] enable_nat_traversal: Whether to enable NAT traversal.
        :param pulumi.Input[pulumi.InputType['ConnectionHealthCheckConfigArgs']] health_check_config: The health check configurations. See the following `Block health_check_config`.
        :param pulumi.Input[pulumi.InputType['ConnectionIkeConfigArgs']] ike_config: The configurations of phase-one negotiation. See the following `Block ike_config`.
        :param pulumi.Input[pulumi.InputType['ConnectionIpsecConfigArgs']] ipsec_config: The configurations of phase-two negotiation. See the following `Block ipsec_config`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] local_subnets: The CIDR block of the VPC to be connected with the local data center. This parameter is used for phase-two negotiation.
        :param pulumi.Input[str] name: The name of the IPsec connection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] remote_subnets: The CIDR block of the local data center. This parameter is used for phase-two negotiation.
        :param pulumi.Input[str] vpn_gateway_id: The ID of the VPN gateway.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        foo_gateway = alicloud.vpn.Gateway("fooGateway",
            vpc_id="vpc-fake-id",
            bandwidth=10,
            enable_ssl=True,
            instance_charge_type="PostPaid",
            description="test_create_description")
        foo_customer_gateway = alicloud.vpn.CustomerGateway("fooCustomerGateway",
            ip_address="42.104.22.228",
            description="testAccVpnCgwDesc")
        foo_connection = alicloud.vpn.Connection("fooConnection",
            vpn_gateway_id=foo_gateway.id,
            customer_gateway_id=foo_customer_gateway.id,
            local_subnets=[
                "172.16.0.0/24",
                "172.16.1.0/24",
            ],
            remote_subnets=[
                "10.0.0.0/24",
                "10.0.1.0/24",
            ],
            effect_immediately=True,
            ike_config=alicloud.vpn.ConnectionIkeConfigArgs(
                ike_auth_alg="md5",
                ike_enc_alg="des",
                ike_version="ikev1",
                ike_mode="main",
                ike_lifetime=86400,
                psk="tf-testvpn2",
                ike_pfs="group1",
                ike_remote_id="testbob2",
                ike_local_id="testalice2",
            ),
            ipsec_config=alicloud.vpn.ConnectionIpsecConfigArgs(
                ipsec_pfs="group5",
                ipsec_enc_alg="des",
                ipsec_auth_alg="md5",
                ipsec_lifetime=8640,
            ))
        ```

        ## Import

        VPN connection can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:vpn/connection:Connection example vco-abc123456
        ```

        :param str resource_name: The name of the resource.
        :param ConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_config: Optional[pulumi.Input[pulumi.InputType['ConnectionBgpConfigArgs']]] = None,
                 customer_gateway_id: Optional[pulumi.Input[str]] = None,
                 effect_immediately: Optional[pulumi.Input[bool]] = None,
                 enable_dpd: Optional[pulumi.Input[bool]] = None,
                 enable_nat_traversal: Optional[pulumi.Input[bool]] = None,
                 health_check_config: Optional[pulumi.Input[pulumi.InputType['ConnectionHealthCheckConfigArgs']]] = None,
                 ike_config: Optional[pulumi.Input[pulumi.InputType['ConnectionIkeConfigArgs']]] = None,
                 ipsec_config: Optional[pulumi.Input[pulumi.InputType['ConnectionIpsecConfigArgs']]] = None,
                 local_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remote_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpn_gateway_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectionArgs.__new__(ConnectionArgs)

            __props__.__dict__["bgp_config"] = bgp_config
            if customer_gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'customer_gateway_id'")
            __props__.__dict__["customer_gateway_id"] = customer_gateway_id
            __props__.__dict__["effect_immediately"] = effect_immediately
            __props__.__dict__["enable_dpd"] = enable_dpd
            __props__.__dict__["enable_nat_traversal"] = enable_nat_traversal
            __props__.__dict__["health_check_config"] = health_check_config
            __props__.__dict__["ike_config"] = ike_config
            __props__.__dict__["ipsec_config"] = ipsec_config
            if local_subnets is None and not opts.urn:
                raise TypeError("Missing required property 'local_subnets'")
            __props__.__dict__["local_subnets"] = local_subnets
            __props__.__dict__["name"] = name
            if remote_subnets is None and not opts.urn:
                raise TypeError("Missing required property 'remote_subnets'")
            __props__.__dict__["remote_subnets"] = remote_subnets
            if vpn_gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpn_gateway_id'")
            __props__.__dict__["vpn_gateway_id"] = vpn_gateway_id
            __props__.__dict__["status"] = None
        super(Connection, __self__).__init__(
            'alicloud:vpn/connection:Connection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bgp_config: Optional[pulumi.Input[pulumi.InputType['ConnectionBgpConfigArgs']]] = None,
            customer_gateway_id: Optional[pulumi.Input[str]] = None,
            effect_immediately: Optional[pulumi.Input[bool]] = None,
            enable_dpd: Optional[pulumi.Input[bool]] = None,
            enable_nat_traversal: Optional[pulumi.Input[bool]] = None,
            health_check_config: Optional[pulumi.Input[pulumi.InputType['ConnectionHealthCheckConfigArgs']]] = None,
            ike_config: Optional[pulumi.Input[pulumi.InputType['ConnectionIkeConfigArgs']]] = None,
            ipsec_config: Optional[pulumi.Input[pulumi.InputType['ConnectionIpsecConfigArgs']]] = None,
            local_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            remote_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            status: Optional[pulumi.Input[str]] = None,
            vpn_gateway_id: Optional[pulumi.Input[str]] = None) -> 'Connection':
        """
        Get an existing Connection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ConnectionBgpConfigArgs']] bgp_config: The configurations of the BGP routing protocol. See the following `Block bgp_config`.
        :param pulumi.Input[str] customer_gateway_id: The ID of the customer gateway.
        :param pulumi.Input[bool] effect_immediately: Whether to delete a successfully negotiated IPsec tunnel and initiate a negotiation again. Valid value:true,false.
        :param pulumi.Input[bool] enable_dpd: Whether to enable NAT traversal.
        :param pulumi.Input[bool] enable_nat_traversal: Whether to enable NAT traversal.
        :param pulumi.Input[pulumi.InputType['ConnectionHealthCheckConfigArgs']] health_check_config: The health check configurations. See the following `Block health_check_config`.
        :param pulumi.Input[pulumi.InputType['ConnectionIkeConfigArgs']] ike_config: The configurations of phase-one negotiation. See the following `Block ike_config`.
        :param pulumi.Input[pulumi.InputType['ConnectionIpsecConfigArgs']] ipsec_config: The configurations of phase-two negotiation. See the following `Block ipsec_config`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] local_subnets: The CIDR block of the VPC to be connected with the local data center. This parameter is used for phase-two negotiation.
        :param pulumi.Input[str] name: The name of the IPsec connection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] remote_subnets: The CIDR block of the local data center. This parameter is used for phase-two negotiation.
        :param pulumi.Input[str] status: The status of VPN connection.
        :param pulumi.Input[str] vpn_gateway_id: The ID of the VPN gateway.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConnectionState.__new__(_ConnectionState)

        __props__.__dict__["bgp_config"] = bgp_config
        __props__.__dict__["customer_gateway_id"] = customer_gateway_id
        __props__.__dict__["effect_immediately"] = effect_immediately
        __props__.__dict__["enable_dpd"] = enable_dpd
        __props__.__dict__["enable_nat_traversal"] = enable_nat_traversal
        __props__.__dict__["health_check_config"] = health_check_config
        __props__.__dict__["ike_config"] = ike_config
        __props__.__dict__["ipsec_config"] = ipsec_config
        __props__.__dict__["local_subnets"] = local_subnets
        __props__.__dict__["name"] = name
        __props__.__dict__["remote_subnets"] = remote_subnets
        __props__.__dict__["status"] = status
        __props__.__dict__["vpn_gateway_id"] = vpn_gateway_id
        return Connection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bgpConfig")
    def bgp_config(self) -> pulumi.Output['outputs.ConnectionBgpConfig']:
        """
        The configurations of the BGP routing protocol. See the following `Block bgp_config`.
        """
        return pulumi.get(self, "bgp_config")

    @property
    @pulumi.getter(name="customerGatewayId")
    def customer_gateway_id(self) -> pulumi.Output[str]:
        """
        The ID of the customer gateway.
        """
        return pulumi.get(self, "customer_gateway_id")

    @property
    @pulumi.getter(name="effectImmediately")
    def effect_immediately(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to delete a successfully negotiated IPsec tunnel and initiate a negotiation again. Valid value:true,false.
        """
        return pulumi.get(self, "effect_immediately")

    @property
    @pulumi.getter(name="enableDpd")
    def enable_dpd(self) -> pulumi.Output[bool]:
        """
        Whether to enable NAT traversal.
        """
        return pulumi.get(self, "enable_dpd")

    @property
    @pulumi.getter(name="enableNatTraversal")
    def enable_nat_traversal(self) -> pulumi.Output[bool]:
        """
        Whether to enable NAT traversal.
        """
        return pulumi.get(self, "enable_nat_traversal")

    @property
    @pulumi.getter(name="healthCheckConfig")
    def health_check_config(self) -> pulumi.Output['outputs.ConnectionHealthCheckConfig']:
        """
        The health check configurations. See the following `Block health_check_config`.
        """
        return pulumi.get(self, "health_check_config")

    @property
    @pulumi.getter(name="ikeConfig")
    def ike_config(self) -> pulumi.Output['outputs.ConnectionIkeConfig']:
        """
        The configurations of phase-one negotiation. See the following `Block ike_config`.
        """
        return pulumi.get(self, "ike_config")

    @property
    @pulumi.getter(name="ipsecConfig")
    def ipsec_config(self) -> pulumi.Output['outputs.ConnectionIpsecConfig']:
        """
        The configurations of phase-two negotiation. See the following `Block ipsec_config`.
        """
        return pulumi.get(self, "ipsec_config")

    @property
    @pulumi.getter(name="localSubnets")
    def local_subnets(self) -> pulumi.Output[Sequence[str]]:
        """
        The CIDR block of the VPC to be connected with the local data center. This parameter is used for phase-two negotiation.
        """
        return pulumi.get(self, "local_subnets")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the IPsec connection.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="remoteSubnets")
    def remote_subnets(self) -> pulumi.Output[Sequence[str]]:
        """
        The CIDR block of the local data center. This parameter is used for phase-two negotiation.
        """
        return pulumi.get(self, "remote_subnets")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of VPN connection.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPN gateway.
        """
        return pulumi.get(self, "vpn_gateway_id")

