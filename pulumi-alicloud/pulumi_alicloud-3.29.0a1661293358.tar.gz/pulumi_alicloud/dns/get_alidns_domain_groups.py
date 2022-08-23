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
    'GetAlidnsDomainGroupsResult',
    'AwaitableGetAlidnsDomainGroupsResult',
    'get_alidns_domain_groups',
    'get_alidns_domain_groups_output',
]

@pulumi.output_type
class GetAlidnsDomainGroupsResult:
    """
    A collection of values returned by getAlidnsDomainGroups.
    """
    def __init__(__self__, groups=None, id=None, ids=None, name_regex=None, names=None, output_file=None):
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)

    @property
    @pulumi.getter
    def groups(self) -> Sequence['outputs.GetAlidnsDomainGroupsGroupResult']:
        """
        A list of instances. Each element contains the following attributes:
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
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        A list of instance IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of domain group names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")


class AwaitableGetAlidnsDomainGroupsResult(GetAlidnsDomainGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAlidnsDomainGroupsResult(
            groups=self.groups,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file)


def get_alidns_domain_groups(ids: Optional[Sequence[str]] = None,
                             name_regex: Optional[str] = None,
                             output_file: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAlidnsDomainGroupsResult:
    """
    This data source provides a list of Alidns Domain Groups in an Alibaba Cloud account according to the specified filters.

    > **NOTE:**  Available in 1.85.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.dns.get_alidns_domain_groups(ids=["c5ef2bc43064445787adf182af2****"])
    pulumi.export("firstDomainGroupId", example.groups[0].id)
    ```


    :param Sequence[str] ids: A list of instance IDs.
    :param str name_regex: A regex string to filter results by the domain group name.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:dns/getAlidnsDomainGroups:getAlidnsDomainGroups', __args__, opts=opts, typ=GetAlidnsDomainGroupsResult).value

    return AwaitableGetAlidnsDomainGroupsResult(
        groups=__ret__.groups,
        id=__ret__.id,
        ids=__ret__.ids,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file)


@_utilities.lift_output_func(get_alidns_domain_groups)
def get_alidns_domain_groups_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                    name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                    output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAlidnsDomainGroupsResult]:
    """
    This data source provides a list of Alidns Domain Groups in an Alibaba Cloud account according to the specified filters.

    > **NOTE:**  Available in 1.85.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.dns.get_alidns_domain_groups(ids=["c5ef2bc43064445787adf182af2****"])
    pulumi.export("firstDomainGroupId", example.groups[0].id)
    ```


    :param Sequence[str] ids: A list of instance IDs.
    :param str name_regex: A regex string to filter results by the domain group name.
    """
    ...
