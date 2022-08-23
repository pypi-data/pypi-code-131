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
from ._enums import *
from ._inputs import *

__all__ = ['LocationFSxOpenZFSArgs', 'LocationFSxOpenZFS']

@pulumi.input_type
class LocationFSxOpenZFSArgs:
    def __init__(__self__, *,
                 fsx_filesystem_arn: pulumi.Input[str],
                 protocol: pulumi.Input['LocationFSxOpenZFSProtocolArgs'],
                 security_group_arns: pulumi.Input[Sequence[pulumi.Input[str]]],
                 subdirectory: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['LocationFSxOpenZFSTagArgs']]]] = None):
        """
        The set of arguments for constructing a LocationFSxOpenZFS resource.
        :param pulumi.Input[str] fsx_filesystem_arn: The Amazon Resource Name (ARN) for the FSx OpenZFS file system.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_arns: The ARNs of the security groups that are to use to configure the FSx OpenZFS file system.
        :param pulumi.Input[str] subdirectory: A subdirectory in the location's path.
        :param pulumi.Input[Sequence[pulumi.Input['LocationFSxOpenZFSTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "fsx_filesystem_arn", fsx_filesystem_arn)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "security_group_arns", security_group_arns)
        if subdirectory is not None:
            pulumi.set(__self__, "subdirectory", subdirectory)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="fsxFilesystemArn")
    def fsx_filesystem_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) for the FSx OpenZFS file system.
        """
        return pulumi.get(self, "fsx_filesystem_arn")

    @fsx_filesystem_arn.setter
    def fsx_filesystem_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "fsx_filesystem_arn", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input['LocationFSxOpenZFSProtocolArgs']:
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input['LocationFSxOpenZFSProtocolArgs']):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The ARNs of the security groups that are to use to configure the FSx OpenZFS file system.
        """
        return pulumi.get(self, "security_group_arns")

    @security_group_arns.setter
    def security_group_arns(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "security_group_arns", value)

    @property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[str]]:
        """
        A subdirectory in the location's path.
        """
        return pulumi.get(self, "subdirectory")

    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subdirectory", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocationFSxOpenZFSTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocationFSxOpenZFSTagArgs']]]]):
        pulumi.set(self, "tags", value)


class LocationFSxOpenZFS(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fsx_filesystem_arn: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[pulumi.InputType['LocationFSxOpenZFSProtocolArgs']]] = None,
                 security_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subdirectory: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocationFSxOpenZFSTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::DataSync::LocationFSxOpenZFS.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fsx_filesystem_arn: The Amazon Resource Name (ARN) for the FSx OpenZFS file system.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_arns: The ARNs of the security groups that are to use to configure the FSx OpenZFS file system.
        :param pulumi.Input[str] subdirectory: A subdirectory in the location's path.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocationFSxOpenZFSTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocationFSxOpenZFSArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::DataSync::LocationFSxOpenZFS.

        :param str resource_name: The name of the resource.
        :param LocationFSxOpenZFSArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocationFSxOpenZFSArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fsx_filesystem_arn: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[pulumi.InputType['LocationFSxOpenZFSProtocolArgs']]] = None,
                 security_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subdirectory: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocationFSxOpenZFSTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocationFSxOpenZFSArgs.__new__(LocationFSxOpenZFSArgs)

            if fsx_filesystem_arn is None and not opts.urn:
                raise TypeError("Missing required property 'fsx_filesystem_arn'")
            __props__.__dict__["fsx_filesystem_arn"] = fsx_filesystem_arn
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            if security_group_arns is None and not opts.urn:
                raise TypeError("Missing required property 'security_group_arns'")
            __props__.__dict__["security_group_arns"] = security_group_arns
            __props__.__dict__["subdirectory"] = subdirectory
            __props__.__dict__["tags"] = tags
            __props__.__dict__["location_arn"] = None
            __props__.__dict__["location_uri"] = None
        super(LocationFSxOpenZFS, __self__).__init__(
            'aws-native:datasync:LocationFSxOpenZFS',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LocationFSxOpenZFS':
        """
        Get an existing LocationFSxOpenZFS resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LocationFSxOpenZFSArgs.__new__(LocationFSxOpenZFSArgs)

        __props__.__dict__["fsx_filesystem_arn"] = None
        __props__.__dict__["location_arn"] = None
        __props__.__dict__["location_uri"] = None
        __props__.__dict__["protocol"] = None
        __props__.__dict__["security_group_arns"] = None
        __props__.__dict__["subdirectory"] = None
        __props__.__dict__["tags"] = None
        return LocationFSxOpenZFS(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="fsxFilesystemArn")
    def fsx_filesystem_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) for the FSx OpenZFS file system.
        """
        return pulumi.get(self, "fsx_filesystem_arn")

    @property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the Amazon FSx OpenZFS file system location that is created.
        """
        return pulumi.get(self, "location_arn")

    @property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> pulumi.Output[str]:
        """
        The URL of the FSx OpenZFS that was described.
        """
        return pulumi.get(self, "location_uri")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output['outputs.LocationFSxOpenZFSProtocol']:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> pulumi.Output[Sequence[str]]:
        """
        The ARNs of the security groups that are to use to configure the FSx OpenZFS file system.
        """
        return pulumi.get(self, "security_group_arns")

    @property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[Optional[str]]:
        """
        A subdirectory in the location's path.
        """
        return pulumi.get(self, "subdirectory")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.LocationFSxOpenZFSTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

