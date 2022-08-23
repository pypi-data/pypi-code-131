# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SslVpnServerArgs', 'SslVpnServer']

@pulumi.input_type
class SslVpnServerArgs:
    def __init__(__self__, *,
                 client_ip_pool: pulumi.Input[str],
                 local_subnet: pulumi.Input[str],
                 vpn_gateway_id: pulumi.Input[str],
                 cipher: Optional[pulumi.Input[str]] = None,
                 compress: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SslVpnServer resource.
        :param pulumi.Input[str] client_ip_pool: The CIDR block from which access addresses are allocated to the virtual network interface card of the client.
        :param pulumi.Input[str] local_subnet: The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like `10.0.1.0/24,10.0.2.0/24,10.0.3.0/24`.
        :param pulumi.Input[str] vpn_gateway_id: The ID of the VPN gateway.
        :param pulumi.Input[str] cipher: The encryption algorithm that is used in the SSL-VPN connection. Valid values: `AES-128-CBC`,`AES-192-CBC`,`AES-256-CBC`,`none`. Default value: `AES-128-CBC`.
               * `AES-128-CBC` - the AES-128-CBC algorithm.
               * `AES-192-CBC` - the AES-192-CBC algorithm.
               * `AES-256-CBC` - the AES-256-CBC algorithm.
        :param pulumi.Input[bool] compress: Specifies whether to enable data compression. Valid values: `true`,`false`. Default value: `false`
        :param pulumi.Input[str] name: The name of the SSL-VPN server.
        :param pulumi.Input[int] port: The port used by the SSL-VPN server. The default value is `1194`.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].
        :param pulumi.Input[str] protocol: The protocol used by the SSL-VPN server. Valid value: UDP(default) |TCP
        """
        pulumi.set(__self__, "client_ip_pool", client_ip_pool)
        pulumi.set(__self__, "local_subnet", local_subnet)
        pulumi.set(__self__, "vpn_gateway_id", vpn_gateway_id)
        if cipher is not None:
            pulumi.set(__self__, "cipher", cipher)
        if compress is not None:
            pulumi.set(__self__, "compress", compress)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="clientIpPool")
    def client_ip_pool(self) -> pulumi.Input[str]:
        """
        The CIDR block from which access addresses are allocated to the virtual network interface card of the client.
        """
        return pulumi.get(self, "client_ip_pool")

    @client_ip_pool.setter
    def client_ip_pool(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_ip_pool", value)

    @property
    @pulumi.getter(name="localSubnet")
    def local_subnet(self) -> pulumi.Input[str]:
        """
        The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like `10.0.1.0/24,10.0.2.0/24,10.0.3.0/24`.
        """
        return pulumi.get(self, "local_subnet")

    @local_subnet.setter
    def local_subnet(self, value: pulumi.Input[str]):
        pulumi.set(self, "local_subnet", value)

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
    @pulumi.getter
    def cipher(self) -> Optional[pulumi.Input[str]]:
        """
        The encryption algorithm that is used in the SSL-VPN connection. Valid values: `AES-128-CBC`,`AES-192-CBC`,`AES-256-CBC`,`none`. Default value: `AES-128-CBC`.
        * `AES-128-CBC` - the AES-128-CBC algorithm.
        * `AES-192-CBC` - the AES-192-CBC algorithm.
        * `AES-256-CBC` - the AES-256-CBC algorithm.
        """
        return pulumi.get(self, "cipher")

    @cipher.setter
    def cipher(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cipher", value)

    @property
    @pulumi.getter
    def compress(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to enable data compression. Valid values: `true`,`false`. Default value: `false`
        """
        return pulumi.get(self, "compress")

    @compress.setter
    def compress(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "compress", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the SSL-VPN server.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The port used by the SSL-VPN server. The default value is `1194`.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol used by the SSL-VPN server. Valid value: UDP(default) |TCP
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)


@pulumi.input_type
class _SslVpnServerState:
    def __init__(__self__, *,
                 cipher: Optional[pulumi.Input[str]] = None,
                 client_ip_pool: Optional[pulumi.Input[str]] = None,
                 compress: Optional[pulumi.Input[bool]] = None,
                 connections: Optional[pulumi.Input[int]] = None,
                 internet_ip: Optional[pulumi.Input[str]] = None,
                 local_subnet: Optional[pulumi.Input[str]] = None,
                 max_connections: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 vpn_gateway_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SslVpnServer resources.
        :param pulumi.Input[str] cipher: The encryption algorithm that is used in the SSL-VPN connection. Valid values: `AES-128-CBC`,`AES-192-CBC`,`AES-256-CBC`,`none`. Default value: `AES-128-CBC`.
               * `AES-128-CBC` - the AES-128-CBC algorithm.
               * `AES-192-CBC` - the AES-192-CBC algorithm.
               * `AES-256-CBC` - the AES-256-CBC algorithm.
        :param pulumi.Input[str] client_ip_pool: The CIDR block from which access addresses are allocated to the virtual network interface card of the client.
        :param pulumi.Input[bool] compress: Specifies whether to enable data compression. Valid values: `true`,`false`. Default value: `false`
        :param pulumi.Input[int] connections: The number of current connections.
        :param pulumi.Input[str] internet_ip: The internet IP of the SSL-VPN server.
        :param pulumi.Input[str] local_subnet: The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like `10.0.1.0/24,10.0.2.0/24,10.0.3.0/24`.
        :param pulumi.Input[int] max_connections: The maximum number of connections.
        :param pulumi.Input[str] name: The name of the SSL-VPN server.
        :param pulumi.Input[int] port: The port used by the SSL-VPN server. The default value is `1194`.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].
        :param pulumi.Input[str] protocol: The protocol used by the SSL-VPN server. Valid value: UDP(default) |TCP
        :param pulumi.Input[str] vpn_gateway_id: The ID of the VPN gateway.
        """
        if cipher is not None:
            pulumi.set(__self__, "cipher", cipher)
        if client_ip_pool is not None:
            pulumi.set(__self__, "client_ip_pool", client_ip_pool)
        if compress is not None:
            pulumi.set(__self__, "compress", compress)
        if connections is not None:
            pulumi.set(__self__, "connections", connections)
        if internet_ip is not None:
            pulumi.set(__self__, "internet_ip", internet_ip)
        if local_subnet is not None:
            pulumi.set(__self__, "local_subnet", local_subnet)
        if max_connections is not None:
            pulumi.set(__self__, "max_connections", max_connections)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if vpn_gateway_id is not None:
            pulumi.set(__self__, "vpn_gateway_id", vpn_gateway_id)

    @property
    @pulumi.getter
    def cipher(self) -> Optional[pulumi.Input[str]]:
        """
        The encryption algorithm that is used in the SSL-VPN connection. Valid values: `AES-128-CBC`,`AES-192-CBC`,`AES-256-CBC`,`none`. Default value: `AES-128-CBC`.
        * `AES-128-CBC` - the AES-128-CBC algorithm.
        * `AES-192-CBC` - the AES-192-CBC algorithm.
        * `AES-256-CBC` - the AES-256-CBC algorithm.
        """
        return pulumi.get(self, "cipher")

    @cipher.setter
    def cipher(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cipher", value)

    @property
    @pulumi.getter(name="clientIpPool")
    def client_ip_pool(self) -> Optional[pulumi.Input[str]]:
        """
        The CIDR block from which access addresses are allocated to the virtual network interface card of the client.
        """
        return pulumi.get(self, "client_ip_pool")

    @client_ip_pool.setter
    def client_ip_pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_ip_pool", value)

    @property
    @pulumi.getter
    def compress(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to enable data compression. Valid values: `true`,`false`. Default value: `false`
        """
        return pulumi.get(self, "compress")

    @compress.setter
    def compress(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "compress", value)

    @property
    @pulumi.getter
    def connections(self) -> Optional[pulumi.Input[int]]:
        """
        The number of current connections.
        """
        return pulumi.get(self, "connections")

    @connections.setter
    def connections(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "connections", value)

    @property
    @pulumi.getter(name="internetIp")
    def internet_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The internet IP of the SSL-VPN server.
        """
        return pulumi.get(self, "internet_ip")

    @internet_ip.setter
    def internet_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "internet_ip", value)

    @property
    @pulumi.getter(name="localSubnet")
    def local_subnet(self) -> Optional[pulumi.Input[str]]:
        """
        The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like `10.0.1.0/24,10.0.2.0/24,10.0.3.0/24`.
        """
        return pulumi.get(self, "local_subnet")

    @local_subnet.setter
    def local_subnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "local_subnet", value)

    @property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of connections.
        """
        return pulumi.get(self, "max_connections")

    @max_connections.setter
    def max_connections(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_connections", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the SSL-VPN server.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The port used by the SSL-VPN server. The default value is `1194`.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol used by the SSL-VPN server. Valid value: UDP(default) |TCP
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

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


class SslVpnServer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cipher: Optional[pulumi.Input[str]] = None,
                 client_ip_pool: Optional[pulumi.Input[str]] = None,
                 compress: Optional[pulumi.Input[bool]] = None,
                 local_subnet: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
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
        foo_ssl_vpn_server = alicloud.vpn.SslVpnServer("fooSslVpnServer",
            vpn_gateway_id=foo_gateway.id,
            client_ip_pool="192.168.0.0/16",
            local_subnet="172.16.0.0/21",
            protocol="UDP",
            cipher="AES-128-CBC",
            port=1194,
            compress=False)
        ```

        ## Import

        SSL-VPN server can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:vpn/sslVpnServer:SslVpnServer example vss-abc123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cipher: The encryption algorithm that is used in the SSL-VPN connection. Valid values: `AES-128-CBC`,`AES-192-CBC`,`AES-256-CBC`,`none`. Default value: `AES-128-CBC`.
               * `AES-128-CBC` - the AES-128-CBC algorithm.
               * `AES-192-CBC` - the AES-192-CBC algorithm.
               * `AES-256-CBC` - the AES-256-CBC algorithm.
        :param pulumi.Input[str] client_ip_pool: The CIDR block from which access addresses are allocated to the virtual network interface card of the client.
        :param pulumi.Input[bool] compress: Specifies whether to enable data compression. Valid values: `true`,`false`. Default value: `false`
        :param pulumi.Input[str] local_subnet: The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like `10.0.1.0/24,10.0.2.0/24,10.0.3.0/24`.
        :param pulumi.Input[str] name: The name of the SSL-VPN server.
        :param pulumi.Input[int] port: The port used by the SSL-VPN server. The default value is `1194`.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].
        :param pulumi.Input[str] protocol: The protocol used by the SSL-VPN server. Valid value: UDP(default) |TCP
        :param pulumi.Input[str] vpn_gateway_id: The ID of the VPN gateway.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SslVpnServerArgs,
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
        foo_ssl_vpn_server = alicloud.vpn.SslVpnServer("fooSslVpnServer",
            vpn_gateway_id=foo_gateway.id,
            client_ip_pool="192.168.0.0/16",
            local_subnet="172.16.0.0/21",
            protocol="UDP",
            cipher="AES-128-CBC",
            port=1194,
            compress=False)
        ```

        ## Import

        SSL-VPN server can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:vpn/sslVpnServer:SslVpnServer example vss-abc123456
        ```

        :param str resource_name: The name of the resource.
        :param SslVpnServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SslVpnServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cipher: Optional[pulumi.Input[str]] = None,
                 client_ip_pool: Optional[pulumi.Input[str]] = None,
                 compress: Optional[pulumi.Input[bool]] = None,
                 local_subnet: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 vpn_gateway_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SslVpnServerArgs.__new__(SslVpnServerArgs)

            __props__.__dict__["cipher"] = cipher
            if client_ip_pool is None and not opts.urn:
                raise TypeError("Missing required property 'client_ip_pool'")
            __props__.__dict__["client_ip_pool"] = client_ip_pool
            __props__.__dict__["compress"] = compress
            if local_subnet is None and not opts.urn:
                raise TypeError("Missing required property 'local_subnet'")
            __props__.__dict__["local_subnet"] = local_subnet
            __props__.__dict__["name"] = name
            __props__.__dict__["port"] = port
            __props__.__dict__["protocol"] = protocol
            if vpn_gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpn_gateway_id'")
            __props__.__dict__["vpn_gateway_id"] = vpn_gateway_id
            __props__.__dict__["connections"] = None
            __props__.__dict__["internet_ip"] = None
            __props__.__dict__["max_connections"] = None
        super(SslVpnServer, __self__).__init__(
            'alicloud:vpn/sslVpnServer:SslVpnServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cipher: Optional[pulumi.Input[str]] = None,
            client_ip_pool: Optional[pulumi.Input[str]] = None,
            compress: Optional[pulumi.Input[bool]] = None,
            connections: Optional[pulumi.Input[int]] = None,
            internet_ip: Optional[pulumi.Input[str]] = None,
            local_subnet: Optional[pulumi.Input[str]] = None,
            max_connections: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            vpn_gateway_id: Optional[pulumi.Input[str]] = None) -> 'SslVpnServer':
        """
        Get an existing SslVpnServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cipher: The encryption algorithm that is used in the SSL-VPN connection. Valid values: `AES-128-CBC`,`AES-192-CBC`,`AES-256-CBC`,`none`. Default value: `AES-128-CBC`.
               * `AES-128-CBC` - the AES-128-CBC algorithm.
               * `AES-192-CBC` - the AES-192-CBC algorithm.
               * `AES-256-CBC` - the AES-256-CBC algorithm.
        :param pulumi.Input[str] client_ip_pool: The CIDR block from which access addresses are allocated to the virtual network interface card of the client.
        :param pulumi.Input[bool] compress: Specifies whether to enable data compression. Valid values: `true`,`false`. Default value: `false`
        :param pulumi.Input[int] connections: The number of current connections.
        :param pulumi.Input[str] internet_ip: The internet IP of the SSL-VPN server.
        :param pulumi.Input[str] local_subnet: The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like `10.0.1.0/24,10.0.2.0/24,10.0.3.0/24`.
        :param pulumi.Input[int] max_connections: The maximum number of connections.
        :param pulumi.Input[str] name: The name of the SSL-VPN server.
        :param pulumi.Input[int] port: The port used by the SSL-VPN server. The default value is `1194`.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].
        :param pulumi.Input[str] protocol: The protocol used by the SSL-VPN server. Valid value: UDP(default) |TCP
        :param pulumi.Input[str] vpn_gateway_id: The ID of the VPN gateway.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SslVpnServerState.__new__(_SslVpnServerState)

        __props__.__dict__["cipher"] = cipher
        __props__.__dict__["client_ip_pool"] = client_ip_pool
        __props__.__dict__["compress"] = compress
        __props__.__dict__["connections"] = connections
        __props__.__dict__["internet_ip"] = internet_ip
        __props__.__dict__["local_subnet"] = local_subnet
        __props__.__dict__["max_connections"] = max_connections
        __props__.__dict__["name"] = name
        __props__.__dict__["port"] = port
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["vpn_gateway_id"] = vpn_gateway_id
        return SslVpnServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cipher(self) -> pulumi.Output[Optional[str]]:
        """
        The encryption algorithm that is used in the SSL-VPN connection. Valid values: `AES-128-CBC`,`AES-192-CBC`,`AES-256-CBC`,`none`. Default value: `AES-128-CBC`.
        * `AES-128-CBC` - the AES-128-CBC algorithm.
        * `AES-192-CBC` - the AES-192-CBC algorithm.
        * `AES-256-CBC` - the AES-256-CBC algorithm.
        """
        return pulumi.get(self, "cipher")

    @property
    @pulumi.getter(name="clientIpPool")
    def client_ip_pool(self) -> pulumi.Output[str]:
        """
        The CIDR block from which access addresses are allocated to the virtual network interface card of the client.
        """
        return pulumi.get(self, "client_ip_pool")

    @property
    @pulumi.getter
    def compress(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether to enable data compression. Valid values: `true`,`false`. Default value: `false`
        """
        return pulumi.get(self, "compress")

    @property
    @pulumi.getter
    def connections(self) -> pulumi.Output[int]:
        """
        The number of current connections.
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter(name="internetIp")
    def internet_ip(self) -> pulumi.Output[str]:
        """
        The internet IP of the SSL-VPN server.
        """
        return pulumi.get(self, "internet_ip")

    @property
    @pulumi.getter(name="localSubnet")
    def local_subnet(self) -> pulumi.Output[str]:
        """
        The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like `10.0.1.0/24,10.0.2.0/24,10.0.3.0/24`.
        """
        return pulumi.get(self, "local_subnet")

    @property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> pulumi.Output[int]:
        """
        The maximum number of connections.
        """
        return pulumi.get(self, "max_connections")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the SSL-VPN server.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[int]]:
        """
        The port used by the SSL-VPN server. The default value is `1194`.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[str]]:
        """
        The protocol used by the SSL-VPN server. Valid value: UDP(default) |TCP
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPN gateway.
        """
        return pulumi.get(self, "vpn_gateway_id")

