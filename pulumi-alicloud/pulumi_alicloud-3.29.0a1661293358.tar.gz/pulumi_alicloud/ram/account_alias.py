# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AccountAliasArgs', 'AccountAlias']

@pulumi.input_type
class AccountAliasArgs:
    def __init__(__self__, *,
                 account_alias: pulumi.Input[str]):
        """
        The set of arguments for constructing a AccountAlias resource.
        :param pulumi.Input[str] account_alias: Alias of cloud account. This name can have a string of 3 to 32 characters, must contain only alphanumeric characters or hyphens, such as "-", and must not begin with a hyphen.
        """
        pulumi.set(__self__, "account_alias", account_alias)

    @property
    @pulumi.getter(name="accountAlias")
    def account_alias(self) -> pulumi.Input[str]:
        """
        Alias of cloud account. This name can have a string of 3 to 32 characters, must contain only alphanumeric characters or hyphens, such as "-", and must not begin with a hyphen.
        """
        return pulumi.get(self, "account_alias")

    @account_alias.setter
    def account_alias(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_alias", value)


@pulumi.input_type
class _AccountAliasState:
    def __init__(__self__, *,
                 account_alias: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccountAlias resources.
        :param pulumi.Input[str] account_alias: Alias of cloud account. This name can have a string of 3 to 32 characters, must contain only alphanumeric characters or hyphens, such as "-", and must not begin with a hyphen.
        """
        if account_alias is not None:
            pulumi.set(__self__, "account_alias", account_alias)

    @property
    @pulumi.getter(name="accountAlias")
    def account_alias(self) -> Optional[pulumi.Input[str]]:
        """
        Alias of cloud account. This name can have a string of 3 to 32 characters, must contain only alphanumeric characters or hyphens, such as "-", and must not begin with a hyphen.
        """
        return pulumi.get(self, "account_alias")

    @account_alias.setter
    def account_alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_alias", value)


class AccountAlias(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_alias: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a RAM cloud account alias.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # Create a alias for cloud account.
        alias = alicloud.ram.AccountAlias("alias", account_alias="hallo")
        ```

        ## Import

        RAM account alias can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ram/accountAlias:AccountAlias example my-alias
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_alias: Alias of cloud account. This name can have a string of 3 to 32 characters, must contain only alphanumeric characters or hyphens, such as "-", and must not begin with a hyphen.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountAliasArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a RAM cloud account alias.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # Create a alias for cloud account.
        alias = alicloud.ram.AccountAlias("alias", account_alias="hallo")
        ```

        ## Import

        RAM account alias can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ram/accountAlias:AccountAlias example my-alias
        ```

        :param str resource_name: The name of the resource.
        :param AccountAliasArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountAliasArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_alias: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountAliasArgs.__new__(AccountAliasArgs)

            if account_alias is None and not opts.urn:
                raise TypeError("Missing required property 'account_alias'")
            __props__.__dict__["account_alias"] = account_alias
        super(AccountAlias, __self__).__init__(
            'alicloud:ram/accountAlias:AccountAlias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_alias: Optional[pulumi.Input[str]] = None) -> 'AccountAlias':
        """
        Get an existing AccountAlias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_alias: Alias of cloud account. This name can have a string of 3 to 32 characters, must contain only alphanumeric characters or hyphens, such as "-", and must not begin with a hyphen.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountAliasState.__new__(_AccountAliasState)

        __props__.__dict__["account_alias"] = account_alias
        return AccountAlias(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountAlias")
    def account_alias(self) -> pulumi.Output[str]:
        """
        Alias of cloud account. This name can have a string of 3 to 32 characters, must contain only alphanumeric characters or hyphens, such as "-", and must not begin with a hyphen.
        """
        return pulumi.get(self, "account_alias")

