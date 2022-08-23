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

__all__ = [
    'GetTemplateResult',
    'AwaitableGetTemplateResult',
    'get_template',
    'get_template_output',
]

@pulumi.output_type
class GetTemplateResult:
    def __init__(__self__, arn=None, name=None, permissions=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        <p>The Amazon Resource Name (ARN) of the template.</p>
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        <p>A display name for the template.</p>
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence['outputs.TemplateResourcePermission']]:
        """
        <p>A list of resource permissions to be set on the template. </p>
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.TemplateTag']]:
        """
        <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.</p>
        """
        return pulumi.get(self, "tags")


class AwaitableGetTemplateResult(GetTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTemplateResult(
            arn=self.arn,
            name=self.name,
            permissions=self.permissions,
            tags=self.tags)


def get_template(aws_account_id: Optional[str] = None,
                 template_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTemplateResult:
    """
    Definition of the AWS::QuickSight::Template Resource Type.
    """
    __args__ = dict()
    __args__['awsAccountId'] = aws_account_id
    __args__['templateId'] = template_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:quicksight:getTemplate', __args__, opts=opts, typ=GetTemplateResult).value

    return AwaitableGetTemplateResult(
        arn=__ret__.arn,
        name=__ret__.name,
        permissions=__ret__.permissions,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_template)
def get_template_output(aws_account_id: Optional[pulumi.Input[str]] = None,
                        template_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTemplateResult]:
    """
    Definition of the AWS::QuickSight::Template Resource Type.
    """
    ...
