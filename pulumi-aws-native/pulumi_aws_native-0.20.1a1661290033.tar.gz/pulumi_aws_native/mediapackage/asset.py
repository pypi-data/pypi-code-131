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
from ._inputs import *

__all__ = ['AssetArgs', 'Asset']

@pulumi.input_type
class AssetArgs:
    def __init__(__self__, *,
                 packaging_group_id: pulumi.Input[str],
                 source_arn: pulumi.Input[str],
                 source_role_arn: pulumi.Input[str],
                 resource_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['AssetTagArgs']]]] = None):
        """
        The set of arguments for constructing a Asset resource.
        :param pulumi.Input[str] packaging_group_id: The ID of the PackagingGroup for the Asset.
        :param pulumi.Input[str] source_arn: ARN of the source object in S3.
        :param pulumi.Input[str] source_role_arn: The IAM role_arn used to access the source S3 bucket.
        :param pulumi.Input[str] resource_id: The resource ID to include in SPEKE key requests.
        :param pulumi.Input[Sequence[pulumi.Input['AssetTagArgs']]] tags: A collection of tags associated with a resource
        """
        pulumi.set(__self__, "packaging_group_id", packaging_group_id)
        pulumi.set(__self__, "source_arn", source_arn)
        pulumi.set(__self__, "source_role_arn", source_role_arn)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="packagingGroupId")
    def packaging_group_id(self) -> pulumi.Input[str]:
        """
        The ID of the PackagingGroup for the Asset.
        """
        return pulumi.get(self, "packaging_group_id")

    @packaging_group_id.setter
    def packaging_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "packaging_group_id", value)

    @property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> pulumi.Input[str]:
        """
        ARN of the source object in S3.
        """
        return pulumi.get(self, "source_arn")

    @source_arn.setter
    def source_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_arn", value)

    @property
    @pulumi.getter(name="sourceRoleArn")
    def source_role_arn(self) -> pulumi.Input[str]:
        """
        The IAM role_arn used to access the source S3 bucket.
        """
        return pulumi.get(self, "source_role_arn")

    @source_role_arn.setter
    def source_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_role_arn", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID to include in SPEKE key requests.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssetTagArgs']]]]:
        """
        A collection of tags associated with a resource
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssetTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Asset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 packaging_group_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 source_arn: Optional[pulumi.Input[str]] = None,
                 source_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::MediaPackage::Asset

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] packaging_group_id: The ID of the PackagingGroup for the Asset.
        :param pulumi.Input[str] resource_id: The resource ID to include in SPEKE key requests.
        :param pulumi.Input[str] source_arn: ARN of the source object in S3.
        :param pulumi.Input[str] source_role_arn: The IAM role_arn used to access the source S3 bucket.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetTagArgs']]]] tags: A collection of tags associated with a resource
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::MediaPackage::Asset

        :param str resource_name: The name of the resource.
        :param AssetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 packaging_group_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 source_arn: Optional[pulumi.Input[str]] = None,
                 source_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssetArgs.__new__(AssetArgs)

            if packaging_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'packaging_group_id'")
            __props__.__dict__["packaging_group_id"] = packaging_group_id
            __props__.__dict__["resource_id"] = resource_id
            if source_arn is None and not opts.urn:
                raise TypeError("Missing required property 'source_arn'")
            __props__.__dict__["source_arn"] = source_arn
            if source_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'source_role_arn'")
            __props__.__dict__["source_role_arn"] = source_role_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["egress_endpoints"] = None
        super(Asset, __self__).__init__(
            'aws-native:mediapackage:Asset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Asset':
        """
        Get an existing Asset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssetArgs.__new__(AssetArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["egress_endpoints"] = None
        __props__.__dict__["packaging_group_id"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["source_arn"] = None
        __props__.__dict__["source_role_arn"] = None
        __props__.__dict__["tags"] = None
        return Asset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Asset.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time the Asset was initially submitted for Ingest.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="egressEndpoints")
    def egress_endpoints(self) -> pulumi.Output[Sequence['outputs.AssetEgressEndpoint']]:
        """
        The list of egress endpoints available for the Asset.
        """
        return pulumi.get(self, "egress_endpoints")

    @property
    @pulumi.getter(name="packagingGroupId")
    def packaging_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the PackagingGroup for the Asset.
        """
        return pulumi.get(self, "packaging_group_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource ID to include in SPEKE key requests.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> pulumi.Output[str]:
        """
        ARN of the source object in S3.
        """
        return pulumi.get(self, "source_arn")

    @property
    @pulumi.getter(name="sourceRoleArn")
    def source_role_arn(self) -> pulumi.Output[str]:
        """
        The IAM role_arn used to access the source S3 bucket.
        """
        return pulumi.get(self, "source_role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.AssetTag']]]:
        """
        A collection of tags associated with a resource
        """
        return pulumi.get(self, "tags")

