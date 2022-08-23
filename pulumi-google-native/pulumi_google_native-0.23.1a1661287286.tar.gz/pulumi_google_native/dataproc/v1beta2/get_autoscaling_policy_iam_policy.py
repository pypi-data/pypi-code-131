# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetAutoscalingPolicyIamPolicyResult',
    'AwaitableGetAutoscalingPolicyIamPolicyResult',
    'get_autoscaling_policy_iam_policy',
    'get_autoscaling_policy_iam_policy_output',
]

@pulumi.output_type
class GetAutoscalingPolicyIamPolicyResult:
    def __init__(__self__, bindings=None, etag=None, version=None):
        if bindings and not isinstance(bindings, list):
            raise TypeError("Expected argument 'bindings' to be a list")
        pulumi.set(__self__, "bindings", bindings)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def bindings(self) -> Sequence['outputs.BindingResponse']:
        """
        Associates a list of members to a role. Optionally, may specify a condition that determines how and when the bindings are applied. Each of the bindings must contain at least one member.
        """
        return pulumi.get(self, "bindings")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the etag in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An etag is returned in the response to getIamPolicy, and systems are expected to put that etag in the request to setIamPolicy to ensure that their change will be applied to the same version of the policy.Important: If you use IAM Conditions, you must include the etag field whenever you call setIamPolicy. If you omit this field, then IAM allows you to overwrite a version 3 policy with a version 1 policy, and all of the conditions in the version 3 policy are lost.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        Specifies the format of the policy.Valid values are 0, 1, and 3. Requests that specify an invalid value are rejected.Any operation that affects conditional role bindings must specify version 3. This requirement applies to the following operations: Getting a policy that includes a conditional role binding Adding a conditional role binding to a policy Changing a conditional role binding in a policy Removing any role binding, with or without a condition, from a policy that includes conditionsImportant: If you use IAM Conditions, you must include the etag field whenever you call setIamPolicy. If you omit this field, then IAM allows you to overwrite a version 3 policy with a version 1 policy, and all of the conditions in the version 3 policy are lost.If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset.To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).
        """
        return pulumi.get(self, "version")


class AwaitableGetAutoscalingPolicyIamPolicyResult(GetAutoscalingPolicyIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAutoscalingPolicyIamPolicyResult(
            bindings=self.bindings,
            etag=self.etag,
            version=self.version)


def get_autoscaling_policy_iam_policy(autoscaling_policy_id: Optional[str] = None,
                                      location: Optional[str] = None,
                                      options_requested_policy_version: Optional[int] = None,
                                      project: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAutoscalingPolicyIamPolicyResult:
    """
    Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.
    """
    __args__ = dict()
    __args__['autoscalingPolicyId'] = autoscaling_policy_id
    __args__['location'] = location
    __args__['optionsRequestedPolicyVersion'] = options_requested_policy_version
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:dataproc/v1beta2:getAutoscalingPolicyIamPolicy', __args__, opts=opts, typ=GetAutoscalingPolicyIamPolicyResult).value

    return AwaitableGetAutoscalingPolicyIamPolicyResult(
        bindings=__ret__.bindings,
        etag=__ret__.etag,
        version=__ret__.version)


@_utilities.lift_output_func(get_autoscaling_policy_iam_policy)
def get_autoscaling_policy_iam_policy_output(autoscaling_policy_id: Optional[pulumi.Input[str]] = None,
                                             location: Optional[pulumi.Input[str]] = None,
                                             options_requested_policy_version: Optional[pulumi.Input[Optional[int]]] = None,
                                             project: Optional[pulumi.Input[Optional[str]]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAutoscalingPolicyIamPolicyResult]:
    """
    Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.
    """
    ...
