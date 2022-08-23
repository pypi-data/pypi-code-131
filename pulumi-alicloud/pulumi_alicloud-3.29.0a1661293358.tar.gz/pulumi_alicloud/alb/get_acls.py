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
    'GetAclsResult',
    'AwaitableGetAclsResult',
    'get_acls',
    'get_acls_output',
]

@pulumi.output_type
class GetAclsResult:
    """
    A collection of values returned by getAcls.
    """
    def __init__(__self__, acl_ids=None, acl_name=None, acls=None, enable_details=None, id=None, ids=None, name_regex=None, names=None, output_file=None, resource_group_id=None, status=None):
        if acl_ids and not isinstance(acl_ids, list):
            raise TypeError("Expected argument 'acl_ids' to be a list")
        pulumi.set(__self__, "acl_ids", acl_ids)
        if acl_name and not isinstance(acl_name, str):
            raise TypeError("Expected argument 'acl_name' to be a str")
        pulumi.set(__self__, "acl_name", acl_name)
        if acls and not isinstance(acls, list):
            raise TypeError("Expected argument 'acls' to be a list")
        pulumi.set(__self__, "acls", acls)
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
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
        if resource_group_id and not isinstance(resource_group_id, str):
            raise TypeError("Expected argument 'resource_group_id' to be a str")
        pulumi.set(__self__, "resource_group_id", resource_group_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="aclIds")
    def acl_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "acl_ids")

    @property
    @pulumi.getter(name="aclName")
    def acl_name(self) -> Optional[str]:
        return pulumi.get(self, "acl_name")

    @property
    @pulumi.getter
    def acls(self) -> Sequence['outputs.GetAclsAclResult']:
        return pulumi.get(self, "acls")

    @property
    @pulumi.getter(name="enableDetails")
    def enable_details(self) -> Optional[bool]:
        return pulumi.get(self, "enable_details")

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
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[str]:
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetAclsResult(GetAclsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAclsResult(
            acl_ids=self.acl_ids,
            acl_name=self.acl_name,
            acls=self.acls,
            enable_details=self.enable_details,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            resource_group_id=self.resource_group_id,
            status=self.status)


def get_acls(acl_ids: Optional[Sequence[str]] = None,
             acl_name: Optional[str] = None,
             enable_details: Optional[bool] = None,
             ids: Optional[Sequence[str]] = None,
             name_regex: Optional[str] = None,
             output_file: Optional[str] = None,
             resource_group_id: Optional[str] = None,
             status: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAclsResult:
    """
    This data source provides the Application Load Balancer (ALB) Acls of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.133.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.alb.get_acls()
    pulumi.export("albAclId1", ids.acls[0].id)
    name_regex = alicloud.alb.get_acls(name_regex="^my-Acl")
    pulumi.export("albAclId2", name_regex.acls[0].id)
    ```


    :param Sequence[str] acl_ids: The acl ids.
    :param str acl_name: The ACL Name.
    :param bool enable_details: Default to `false`. Set it to `true` can output more details about resource attributes.
    :param Sequence[str] ids: A list of Acl IDs.
    :param str name_regex: A regex string to filter results by Acl name.
    :param str resource_group_id: Resource Group to Which the Number.
    :param str status: The state of the ACL. Valid values:`Provisioning` , `Available` and `Configuring`. `Provisioning`: The ACL is being created. `Available`: The ACL is available. `Configuring`: The ACL is being configured.
    """
    __args__ = dict()
    __args__['aclIds'] = acl_ids
    __args__['aclName'] = acl_name
    __args__['enableDetails'] = enable_details
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['resourceGroupId'] = resource_group_id
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:alb/getAcls:getAcls', __args__, opts=opts, typ=GetAclsResult).value

    return AwaitableGetAclsResult(
        acl_ids=__ret__.acl_ids,
        acl_name=__ret__.acl_name,
        acls=__ret__.acls,
        enable_details=__ret__.enable_details,
        id=__ret__.id,
        ids=__ret__.ids,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        resource_group_id=__ret__.resource_group_id,
        status=__ret__.status)


@_utilities.lift_output_func(get_acls)
def get_acls_output(acl_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                    acl_name: Optional[pulumi.Input[Optional[str]]] = None,
                    enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                    ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                    name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                    output_file: Optional[pulumi.Input[Optional[str]]] = None,
                    resource_group_id: Optional[pulumi.Input[Optional[str]]] = None,
                    status: Optional[pulumi.Input[Optional[str]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAclsResult]:
    """
    This data source provides the Application Load Balancer (ALB) Acls of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.133.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.alb.get_acls()
    pulumi.export("albAclId1", ids.acls[0].id)
    name_regex = alicloud.alb.get_acls(name_regex="^my-Acl")
    pulumi.export("albAclId2", name_regex.acls[0].id)
    ```


    :param Sequence[str] acl_ids: The acl ids.
    :param str acl_name: The ACL Name.
    :param bool enable_details: Default to `false`. Set it to `true` can output more details about resource attributes.
    :param Sequence[str] ids: A list of Acl IDs.
    :param str name_regex: A regex string to filter results by Acl name.
    :param str resource_group_id: Resource Group to Which the Number.
    :param str status: The state of the ACL. Valid values:`Provisioning` , `Available` and `Configuring`. `Provisioning`: The ACL is being created. `Available`: The ACL is available. `Configuring`: The ACL is being configured.
    """
    ...
