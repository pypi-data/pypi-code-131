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

__all__ = [
    'GetGroupsResult',
    'AwaitableGetGroupsResult',
    'get_groups',
    'get_groups_output',
]

@pulumi.output_type
class GetGroupsResult:
    """
    A collection of values returned by getGroups.
    """
    def __init__(__self__, groups=None, id=None, name_regex=None, names=None, output_file=None, policy_name=None, policy_type=None, user_name=None):
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if policy_name and not isinstance(policy_name, str):
            raise TypeError("Expected argument 'policy_name' to be a str")
        pulumi.set(__self__, "policy_name", policy_name)
        if policy_type and not isinstance(policy_type, str):
            raise TypeError("Expected argument 'policy_type' to be a str")
        pulumi.set(__self__, "policy_type", policy_type)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter
    def groups(self) -> Sequence['outputs.GetGroupsGroupResult']:
        """
        A list of groups. Each element contains the following attributes:
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of ram group names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[str]:
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[str]:
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[str]:
        return pulumi.get(self, "user_name")


class AwaitableGetGroupsResult(GetGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupsResult(
            groups=self.groups,
            id=self.id,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            policy_name=self.policy_name,
            policy_type=self.policy_type,
            user_name=self.user_name)


def get_groups(name_regex: Optional[str] = None,
               output_file: Optional[str] = None,
               policy_name: Optional[str] = None,
               policy_type: Optional[str] = None,
               user_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupsResult:
    """
    This data source provides a list of RAM Groups in an Alibaba Cloud account according to the specified filters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    groups_ds = alicloud.ram.get_groups(name_regex="^group[0-9]*",
        output_file="groups.txt",
        user_name="user1")
    pulumi.export("firstGroupName", groups_ds.groups[0].name)
    ```


    :param str name_regex: A regex string to filter the returned groups by their names.
    :param str policy_name: Filter the results by a specific policy name. If you set this parameter without setting `policy_type`, it will be automatically set to `System`.
    :param str policy_type: Filter the results by a specific policy type. Valid items are `Custom` and `System`. If you set this parameter, you must set `policy_name` as well.
    :param str user_name: Filter the results by a specific the user name.
    """
    __args__ = dict()
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['policyName'] = policy_name
    __args__['policyType'] = policy_type
    __args__['userName'] = user_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:ram/getGroups:getGroups', __args__, opts=opts, typ=GetGroupsResult).value

    return AwaitableGetGroupsResult(
        groups=__ret__.groups,
        id=__ret__.id,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        policy_name=__ret__.policy_name,
        policy_type=__ret__.policy_type,
        user_name=__ret__.user_name)


@_utilities.lift_output_func(get_groups)
def get_groups_output(name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                      output_file: Optional[pulumi.Input[Optional[str]]] = None,
                      policy_name: Optional[pulumi.Input[Optional[str]]] = None,
                      policy_type: Optional[pulumi.Input[Optional[str]]] = None,
                      user_name: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGroupsResult]:
    """
    This data source provides a list of RAM Groups in an Alibaba Cloud account according to the specified filters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    groups_ds = alicloud.ram.get_groups(name_regex="^group[0-9]*",
        output_file="groups.txt",
        user_name="user1")
    pulumi.export("firstGroupName", groups_ds.groups[0].name)
    ```


    :param str name_regex: A regex string to filter the returned groups by their names.
    :param str policy_name: Filter the results by a specific policy name. If you set this parameter without setting `policy_type`, it will be automatically set to `System`.
    :param str policy_type: Filter the results by a specific policy type. Valid items are `Custom` and `System`. If you set this parameter, you must set `policy_name` as well.
    :param str user_name: Filter the results by a specific the user name.
    """
    ...
