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
    'GetDBParameterGroupResult',
    'AwaitableGetDBParameterGroupResult',
    'get_db_parameter_group',
    'get_db_parameter_group_output',
]

@pulumi.output_type
class GetDBParameterGroupResult:
    def __init__(__self__, description=None, family=None, id=None, parameters=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if family and not isinstance(family, str):
            raise TypeError("Expected argument 'family' to be a str")
        pulumi.set(__self__, "family", family)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def family(self) -> Optional[str]:
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DBParameterGroupTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetDBParameterGroupResult(GetDBParameterGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDBParameterGroupResult(
            description=self.description,
            family=self.family,
            id=self.id,
            parameters=self.parameters,
            tags=self.tags)


def get_db_parameter_group(id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDBParameterGroupResult:
    """
    Resource Type definition for AWS::RDS::DBParameterGroup
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:rds:getDBParameterGroup', __args__, opts=opts, typ=GetDBParameterGroupResult).value

    return AwaitableGetDBParameterGroupResult(
        description=__ret__.description,
        family=__ret__.family,
        id=__ret__.id,
        parameters=__ret__.parameters,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_db_parameter_group)
def get_db_parameter_group_output(id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDBParameterGroupResult]:
    """
    Resource Type definition for AWS::RDS::DBParameterGroup
    """
    ...
