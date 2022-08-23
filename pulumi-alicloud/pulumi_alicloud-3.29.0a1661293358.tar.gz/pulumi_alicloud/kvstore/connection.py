# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ConnectionArgs', 'Connection']

@pulumi.input_type
class ConnectionArgs:
    def __init__(__self__, *,
                 connection_string_prefix: pulumi.Input[str],
                 instance_id: pulumi.Input[str],
                 port: pulumi.Input[str]):
        """
        The set of arguments for constructing a Connection resource.
        :param pulumi.Input[str] connection_string_prefix: The prefix of the public endpoint. The prefix can be 8 to 64 characters in length, and can contain lowercase letters and digits. It must start with a lowercase letter.
        :param pulumi.Input[str] instance_id: The ID of the instance.
        :param pulumi.Input[str] port: The service port number of the instance.
        """
        pulumi.set(__self__, "connection_string_prefix", connection_string_prefix)
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter(name="connectionStringPrefix")
    def connection_string_prefix(self) -> pulumi.Input[str]:
        """
        The prefix of the public endpoint. The prefix can be 8 to 64 characters in length, and can contain lowercase letters and digits. It must start with a lowercase letter.
        """
        return pulumi.get(self, "connection_string_prefix")

    @connection_string_prefix.setter
    def connection_string_prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "connection_string_prefix", value)

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
    @pulumi.getter
    def port(self) -> pulumi.Input[str]:
        """
        The service port number of the instance.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[str]):
        pulumi.set(self, "port", value)


@pulumi.input_type
class _ConnectionState:
    def __init__(__self__, *,
                 connection_string: Optional[pulumi.Input[str]] = None,
                 connection_string_prefix: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Connection resources.
        :param pulumi.Input[str] connection_string: The public connection string of KVStore DBInstance.
        :param pulumi.Input[str] connection_string_prefix: The prefix of the public endpoint. The prefix can be 8 to 64 characters in length, and can contain lowercase letters and digits. It must start with a lowercase letter.
        :param pulumi.Input[str] instance_id: The ID of the instance.
        :param pulumi.Input[str] port: The service port number of the instance.
        """
        if connection_string is not None:
            pulumi.set(__self__, "connection_string", connection_string)
        if connection_string_prefix is not None:
            pulumi.set(__self__, "connection_string_prefix", connection_string_prefix)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        The public connection string of KVStore DBInstance.
        """
        return pulumi.get(self, "connection_string")

    @connection_string.setter
    def connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_string", value)

    @property
    @pulumi.getter(name="connectionStringPrefix")
    def connection_string_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The prefix of the public endpoint. The prefix can be 8 to 64 characters in length, and can contain lowercase letters and digits. It must start with a lowercase letter.
        """
        return pulumi.get(self, "connection_string_prefix")

    @connection_string_prefix.setter
    def connection_string_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_string_prefix", value)

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
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[str]]:
        """
        The service port number of the instance.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port", value)


class Connection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_string_prefix: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Operate the public network ip of the specified resource. How to use it, see [What is Resource Alicloud KVStore Connection](https://www.alibabacloud.com/help/doc-detail/125795.htm).

        > **NOTE:** Available in v1.101.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.kvstore.Connection("default",
            connection_string_prefix="allocatetestupdate",
            instance_id="r-abc123456",
            port="6370")
        ```

        ## Import

        KVStore connection can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:kvstore/connection:Connection example r-abc12345678
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_string_prefix: The prefix of the public endpoint. The prefix can be 8 to 64 characters in length, and can contain lowercase letters and digits. It must start with a lowercase letter.
        :param pulumi.Input[str] instance_id: The ID of the instance.
        :param pulumi.Input[str] port: The service port number of the instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Operate the public network ip of the specified resource. How to use it, see [What is Resource Alicloud KVStore Connection](https://www.alibabacloud.com/help/doc-detail/125795.htm).

        > **NOTE:** Available in v1.101.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.kvstore.Connection("default",
            connection_string_prefix="allocatetestupdate",
            instance_id="r-abc123456",
            port="6370")
        ```

        ## Import

        KVStore connection can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:kvstore/connection:Connection example r-abc12345678
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
                 connection_string_prefix: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectionArgs.__new__(ConnectionArgs)

            if connection_string_prefix is None and not opts.urn:
                raise TypeError("Missing required property 'connection_string_prefix'")
            __props__.__dict__["connection_string_prefix"] = connection_string_prefix
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if port is None and not opts.urn:
                raise TypeError("Missing required property 'port'")
            __props__.__dict__["port"] = port
            __props__.__dict__["connection_string"] = None
        super(Connection, __self__).__init__(
            'alicloud:kvstore/connection:Connection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connection_string: Optional[pulumi.Input[str]] = None,
            connection_string_prefix: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[str]] = None) -> 'Connection':
        """
        Get an existing Connection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_string: The public connection string of KVStore DBInstance.
        :param pulumi.Input[str] connection_string_prefix: The prefix of the public endpoint. The prefix can be 8 to 64 characters in length, and can contain lowercase letters and digits. It must start with a lowercase letter.
        :param pulumi.Input[str] instance_id: The ID of the instance.
        :param pulumi.Input[str] port: The service port number of the instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConnectionState.__new__(_ConnectionState)

        __props__.__dict__["connection_string"] = connection_string
        __props__.__dict__["connection_string_prefix"] = connection_string_prefix
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["port"] = port
        return Connection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Output[str]:
        """
        The public connection string of KVStore DBInstance.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter(name="connectionStringPrefix")
    def connection_string_prefix(self) -> pulumi.Output[str]:
        """
        The prefix of the public endpoint. The prefix can be 8 to 64 characters in length, and can contain lowercase letters and digits. It must start with a lowercase letter.
        """
        return pulumi.get(self, "connection_string_prefix")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[str]:
        """
        The service port number of the instance.
        """
        return pulumi.get(self, "port")

