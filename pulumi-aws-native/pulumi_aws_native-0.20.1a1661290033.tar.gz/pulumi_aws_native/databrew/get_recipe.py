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
    'GetRecipeResult',
    'AwaitableGetRecipeResult',
    'get_recipe',
    'get_recipe_output',
]

@pulumi.output_type
class GetRecipeResult:
    def __init__(__self__, description=None, steps=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if steps and not isinstance(steps, list):
            raise TypeError("Expected argument 'steps' to be a list")
        pulumi.set(__self__, "steps", steps)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the recipe
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def steps(self) -> Optional[Sequence['outputs.RecipeStep']]:
        return pulumi.get(self, "steps")


class AwaitableGetRecipeResult(GetRecipeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRecipeResult(
            description=self.description,
            steps=self.steps)


def get_recipe(name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRecipeResult:
    """
    Resource schema for AWS::DataBrew::Recipe.


    :param str name: Recipe name
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:databrew:getRecipe', __args__, opts=opts, typ=GetRecipeResult).value

    return AwaitableGetRecipeResult(
        description=__ret__.description,
        steps=__ret__.steps)


@_utilities.lift_output_func(get_recipe)
def get_recipe_output(name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRecipeResult]:
    """
    Resource schema for AWS::DataBrew::Recipe.


    :param str name: Recipe name
    """
    ...
