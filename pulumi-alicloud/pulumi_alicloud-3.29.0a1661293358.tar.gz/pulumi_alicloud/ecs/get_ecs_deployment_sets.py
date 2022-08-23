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
    'GetEcsDeploymentSetsResult',
    'AwaitableGetEcsDeploymentSetsResult',
    'get_ecs_deployment_sets',
    'get_ecs_deployment_sets_output',
]

@pulumi.output_type
class GetEcsDeploymentSetsResult:
    """
    A collection of values returned by getEcsDeploymentSets.
    """
    def __init__(__self__, deployment_set_name=None, id=None, ids=None, name_regex=None, names=None, output_file=None, sets=None, strategy=None):
        if deployment_set_name and not isinstance(deployment_set_name, str):
            raise TypeError("Expected argument 'deployment_set_name' to be a str")
        pulumi.set(__self__, "deployment_set_name", deployment_set_name)
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
        if sets and not isinstance(sets, list):
            raise TypeError("Expected argument 'sets' to be a list")
        pulumi.set(__self__, "sets", sets)
        if strategy and not isinstance(strategy, str):
            raise TypeError("Expected argument 'strategy' to be a str")
        pulumi.set(__self__, "strategy", strategy)

    @property
    @pulumi.getter(name="deploymentSetName")
    def deployment_set_name(self) -> Optional[str]:
        return pulumi.get(self, "deployment_set_name")

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
    @pulumi.getter
    def sets(self) -> Sequence['outputs.GetEcsDeploymentSetsSetResult']:
        return pulumi.get(self, "sets")

    @property
    @pulumi.getter
    def strategy(self) -> Optional[str]:
        return pulumi.get(self, "strategy")


class AwaitableGetEcsDeploymentSetsResult(GetEcsDeploymentSetsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEcsDeploymentSetsResult(
            deployment_set_name=self.deployment_set_name,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            sets=self.sets,
            strategy=self.strategy)


def get_ecs_deployment_sets(deployment_set_name: Optional[str] = None,
                            ids: Optional[Sequence[str]] = None,
                            name_regex: Optional[str] = None,
                            output_file: Optional[str] = None,
                            strategy: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEcsDeploymentSetsResult:
    """
    This data source provides the Ecs Deployment Sets of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.140.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.ecs.get_ecs_deployment_sets(ids=["example_id"])
    pulumi.export("ecsDeploymentSetId1", ids.sets[0].id)
    name_regex = alicloud.ecs.get_ecs_deployment_sets(name_regex="^my-DeploymentSet")
    pulumi.export("ecsDeploymentSetId2", name_regex.sets[0].id)
    ```


    :param str deployment_set_name: The name of the deployment set.
    :param Sequence[str] ids: A list of Deployment Set IDs.
    :param str name_regex: A regex string to filter results by Deployment Set name.
    :param str strategy: The deployment strategy.
    """
    __args__ = dict()
    __args__['deploymentSetName'] = deployment_set_name
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['strategy'] = strategy
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:ecs/getEcsDeploymentSets:getEcsDeploymentSets', __args__, opts=opts, typ=GetEcsDeploymentSetsResult).value

    return AwaitableGetEcsDeploymentSetsResult(
        deployment_set_name=__ret__.deployment_set_name,
        id=__ret__.id,
        ids=__ret__.ids,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        sets=__ret__.sets,
        strategy=__ret__.strategy)


@_utilities.lift_output_func(get_ecs_deployment_sets)
def get_ecs_deployment_sets_output(deployment_set_name: Optional[pulumi.Input[Optional[str]]] = None,
                                   ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                   name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                   output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                   strategy: Optional[pulumi.Input[Optional[str]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEcsDeploymentSetsResult]:
    """
    This data source provides the Ecs Deployment Sets of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.140.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.ecs.get_ecs_deployment_sets(ids=["example_id"])
    pulumi.export("ecsDeploymentSetId1", ids.sets[0].id)
    name_regex = alicloud.ecs.get_ecs_deployment_sets(name_regex="^my-DeploymentSet")
    pulumi.export("ecsDeploymentSetId2", name_regex.sets[0].id)
    ```


    :param str deployment_set_name: The name of the deployment set.
    :param Sequence[str] ids: A list of Deployment Set IDs.
    :param str name_regex: A regex string to filter results by Deployment Set name.
    :param str strategy: The deployment strategy.
    """
    ...
