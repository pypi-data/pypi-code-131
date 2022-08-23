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

__all__ = ['PermissionSetArgs', 'PermissionSet']

@pulumi.input_type
class PermissionSetArgs:
    def __init__(__self__, *,
                 instance_arn: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 inline_policy: Optional[Any] = None,
                 managed_policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 relay_state_type: Optional[pulumi.Input[str]] = None,
                 session_duration: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionSetTagArgs']]]] = None):
        """
        The set of arguments for constructing a PermissionSet resource.
        :param pulumi.Input[str] instance_arn: The sso instance arn that the permission set is owned.
        :param pulumi.Input[str] description: The permission set description.
        :param Any inline_policy: The inline policy to put in permission set.
        :param pulumi.Input[str] name: The name you want to assign to this permission set.
        :param pulumi.Input[str] relay_state_type: The relay state URL that redirect links to any service in the AWS Management Console.
        :param pulumi.Input[str] session_duration: The length of time that a user can be signed in to an AWS account.
        """
        pulumi.set(__self__, "instance_arn", instance_arn)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if inline_policy is not None:
            pulumi.set(__self__, "inline_policy", inline_policy)
        if managed_policies is not None:
            pulumi.set(__self__, "managed_policies", managed_policies)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if relay_state_type is not None:
            pulumi.set(__self__, "relay_state_type", relay_state_type)
        if session_duration is not None:
            pulumi.set(__self__, "session_duration", session_duration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[str]:
        """
        The sso instance arn that the permission set is owned.
        """
        return pulumi.get(self, "instance_arn")

    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_arn", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The permission set description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="inlinePolicy")
    def inline_policy(self) -> Optional[Any]:
        """
        The inline policy to put in permission set.
        """
        return pulumi.get(self, "inline_policy")

    @inline_policy.setter
    def inline_policy(self, value: Optional[Any]):
        pulumi.set(self, "inline_policy", value)

    @property
    @pulumi.getter(name="managedPolicies")
    def managed_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "managed_policies")

    @managed_policies.setter
    def managed_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "managed_policies", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name you want to assign to this permission set.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="relayStateType")
    def relay_state_type(self) -> Optional[pulumi.Input[str]]:
        """
        The relay state URL that redirect links to any service in the AWS Management Console.
        """
        return pulumi.get(self, "relay_state_type")

    @relay_state_type.setter
    def relay_state_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "relay_state_type", value)

    @property
    @pulumi.getter(name="sessionDuration")
    def session_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The length of time that a user can be signed in to an AWS account.
        """
        return pulumi.get(self, "session_duration")

    @session_duration.setter
    def session_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "session_duration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PermissionSetTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionSetTagArgs']]]]):
        pulumi.set(self, "tags", value)


class PermissionSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 inline_policy: Optional[Any] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 managed_policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 relay_state_type: Optional[pulumi.Input[str]] = None,
                 session_duration: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionSetTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for SSO PermissionSet

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The permission set description.
        :param Any inline_policy: The inline policy to put in permission set.
        :param pulumi.Input[str] instance_arn: The sso instance arn that the permission set is owned.
        :param pulumi.Input[str] name: The name you want to assign to this permission set.
        :param pulumi.Input[str] relay_state_type: The relay state URL that redirect links to any service in the AWS Management Console.
        :param pulumi.Input[str] session_duration: The length of time that a user can be signed in to an AWS account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PermissionSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for SSO PermissionSet

        :param str resource_name: The name of the resource.
        :param PermissionSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PermissionSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 inline_policy: Optional[Any] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 managed_policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 relay_state_type: Optional[pulumi.Input[str]] = None,
                 session_duration: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionSetTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PermissionSetArgs.__new__(PermissionSetArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["inline_policy"] = inline_policy
            if instance_arn is None and not opts.urn:
                raise TypeError("Missing required property 'instance_arn'")
            __props__.__dict__["instance_arn"] = instance_arn
            __props__.__dict__["managed_policies"] = managed_policies
            __props__.__dict__["name"] = name
            __props__.__dict__["relay_state_type"] = relay_state_type
            __props__.__dict__["session_duration"] = session_duration
            __props__.__dict__["tags"] = tags
            __props__.__dict__["permission_set_arn"] = None
        super(PermissionSet, __self__).__init__(
            'aws-native:sso:PermissionSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PermissionSet':
        """
        Get an existing PermissionSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PermissionSetArgs.__new__(PermissionSetArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["inline_policy"] = None
        __props__.__dict__["instance_arn"] = None
        __props__.__dict__["managed_policies"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["permission_set_arn"] = None
        __props__.__dict__["relay_state_type"] = None
        __props__.__dict__["session_duration"] = None
        __props__.__dict__["tags"] = None
        return PermissionSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The permission set description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="inlinePolicy")
    def inline_policy(self) -> pulumi.Output[Optional[Any]]:
        """
        The inline policy to put in permission set.
        """
        return pulumi.get(self, "inline_policy")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[str]:
        """
        The sso instance arn that the permission set is owned.
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter(name="managedPolicies")
    def managed_policies(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "managed_policies")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name you want to assign to this permission set.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Output[str]:
        """
        The permission set that the policy will be attached to
        """
        return pulumi.get(self, "permission_set_arn")

    @property
    @pulumi.getter(name="relayStateType")
    def relay_state_type(self) -> pulumi.Output[Optional[str]]:
        """
        The relay state URL that redirect links to any service in the AWS Management Console.
        """
        return pulumi.get(self, "relay_state_type")

    @property
    @pulumi.getter(name="sessionDuration")
    def session_duration(self) -> pulumi.Output[Optional[str]]:
        """
        The length of time that a user can be signed in to an AWS account.
        """
        return pulumi.get(self, "session_duration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.PermissionSetTag']]]:
        return pulumi.get(self, "tags")

