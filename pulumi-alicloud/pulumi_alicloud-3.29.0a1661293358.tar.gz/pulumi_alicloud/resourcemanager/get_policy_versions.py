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
    'GetPolicyVersionsResult',
    'AwaitableGetPolicyVersionsResult',
    'get_policy_versions',
    'get_policy_versions_output',
]

@pulumi.output_type
class GetPolicyVersionsResult:
    """
    A collection of values returned by getPolicyVersions.
    """
    def __init__(__self__, enable_details=None, id=None, ids=None, output_file=None, policy_name=None, policy_type=None, versions=None):
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if policy_name and not isinstance(policy_name, str):
            raise TypeError("Expected argument 'policy_name' to be a str")
        pulumi.set(__self__, "policy_name", policy_name)
        if policy_type and not isinstance(policy_type, str):
            raise TypeError("Expected argument 'policy_type' to be a str")
        pulumi.set(__self__, "policy_type", policy_type)
        if versions and not isinstance(versions, list):
            raise TypeError("Expected argument 'versions' to be a list")
        pulumi.set(__self__, "versions", versions)

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
        """
        A list of policy version IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> str:
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> str:
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter
    def versions(self) -> Sequence['outputs.GetPolicyVersionsVersionResult']:
        """
        A list of policy versions. Each element contains the following attributes:
        """
        return pulumi.get(self, "versions")


class AwaitableGetPolicyVersionsResult(GetPolicyVersionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyVersionsResult(
            enable_details=self.enable_details,
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            policy_name=self.policy_name,
            policy_type=self.policy_type,
            versions=self.versions)


def get_policy_versions(enable_details: Optional[bool] = None,
                        ids: Optional[Sequence[str]] = None,
                        output_file: Optional[str] = None,
                        policy_name: Optional[str] = None,
                        policy_type: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPolicyVersionsResult:
    """
    This data source provides the Resource Manager Policy Versions of the current Alibaba Cloud user.

    > **NOTE:**  Available in 1.85.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.resourcemanager.get_policy_versions(policy_name="tftest",
        policy_type="Custom")
    pulumi.export("firstPolicyVersionId", default.versions[0].id)
    ```


    :param bool enable_details: -(Optional, Available in v1.114.0+) Default to `false`. Set it to true can output more details.
    :param Sequence[str] ids: A list of policy version IDs.
    :param str policy_name: The name of the policy.
    :param str policy_type: The type of the policy. Valid values:`Custom` and `System`.
    """
    __args__ = dict()
    __args__['enableDetails'] = enable_details
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    __args__['policyName'] = policy_name
    __args__['policyType'] = policy_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:resourcemanager/getPolicyVersions:getPolicyVersions', __args__, opts=opts, typ=GetPolicyVersionsResult).value

    return AwaitableGetPolicyVersionsResult(
        enable_details=__ret__.enable_details,
        id=__ret__.id,
        ids=__ret__.ids,
        output_file=__ret__.output_file,
        policy_name=__ret__.policy_name,
        policy_type=__ret__.policy_type,
        versions=__ret__.versions)


@_utilities.lift_output_func(get_policy_versions)
def get_policy_versions_output(enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                               ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                               output_file: Optional[pulumi.Input[Optional[str]]] = None,
                               policy_name: Optional[pulumi.Input[str]] = None,
                               policy_type: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPolicyVersionsResult]:
    """
    This data source provides the Resource Manager Policy Versions of the current Alibaba Cloud user.

    > **NOTE:**  Available in 1.85.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.resourcemanager.get_policy_versions(policy_name="tftest",
        policy_type="Custom")
    pulumi.export("firstPolicyVersionId", default.versions[0].id)
    ```


    :param bool enable_details: -(Optional, Available in v1.114.0+) Default to `false`. Set it to true can output more details.
    :param Sequence[str] ids: A list of policy version IDs.
    :param str policy_name: The name of the policy.
    :param str policy_type: The type of the policy. Valid values:`Custom` and `System`.
    """
    ...
