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
    'GetExperimentResult',
    'AwaitableGetExperimentResult',
    'get_experiment',
    'get_experiment_output',
]

@pulumi.output_type
class GetExperimentResult:
    def __init__(__self__, create_time=None, definition=None, description=None, display_name=None, end_time=None, experiment_length=None, last_update_time=None, name=None, result=None, rollout_config=None, rollout_failure_reason=None, rollout_state=None, start_time=None, state=None, variants_history=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if definition and not isinstance(definition, dict):
            raise TypeError("Expected argument 'definition' to be a dict")
        pulumi.set(__self__, "definition", definition)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if end_time and not isinstance(end_time, str):
            raise TypeError("Expected argument 'end_time' to be a str")
        pulumi.set(__self__, "end_time", end_time)
        if experiment_length and not isinstance(experiment_length, str):
            raise TypeError("Expected argument 'experiment_length' to be a str")
        pulumi.set(__self__, "experiment_length", experiment_length)
        if last_update_time and not isinstance(last_update_time, str):
            raise TypeError("Expected argument 'last_update_time' to be a str")
        pulumi.set(__self__, "last_update_time", last_update_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if result and not isinstance(result, dict):
            raise TypeError("Expected argument 'result' to be a dict")
        pulumi.set(__self__, "result", result)
        if rollout_config and not isinstance(rollout_config, dict):
            raise TypeError("Expected argument 'rollout_config' to be a dict")
        pulumi.set(__self__, "rollout_config", rollout_config)
        if rollout_failure_reason and not isinstance(rollout_failure_reason, str):
            raise TypeError("Expected argument 'rollout_failure_reason' to be a str")
        pulumi.set(__self__, "rollout_failure_reason", rollout_failure_reason)
        if rollout_state and not isinstance(rollout_state, dict):
            raise TypeError("Expected argument 'rollout_state' to be a dict")
        pulumi.set(__self__, "rollout_state", rollout_state)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if variants_history and not isinstance(variants_history, list):
            raise TypeError("Expected argument 'variants_history' to be a list")
        pulumi.set(__self__, "variants_history", variants_history)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Creation time of this experiment.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def definition(self) -> 'outputs.GoogleCloudDialogflowCxV3beta1ExperimentDefinitionResponse':
        """
        The definition of the experiment.
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The human-readable description of the experiment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The human-readable name of the experiment (unique in an environment). Limit of 64 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        End time of this experiment.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="experimentLength")
    def experiment_length(self) -> str:
        """
        Maximum number of days to run the experiment. If auto-rollout is not enabled, default value and maximum will be 30 days. If auto-rollout is enabled, default value and maximum will be 6 days.
        """
        return pulumi.get(self, "experiment_length")

    @property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> str:
        """
        Last update time of this experiment.
        """
        return pulumi.get(self, "last_update_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the experiment. Format: projects//locations//agents//environments//experiments/..
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def result(self) -> 'outputs.GoogleCloudDialogflowCxV3beta1ExperimentResultResponse':
        """
        Inference result of the experiment.
        """
        return pulumi.get(self, "result")

    @property
    @pulumi.getter(name="rolloutConfig")
    def rollout_config(self) -> 'outputs.GoogleCloudDialogflowCxV3beta1RolloutConfigResponse':
        """
        The configuration for auto rollout. If set, there should be exactly two variants in the experiment (control variant being the default version of the flow), the traffic allocation for the non-control variant will gradually increase to 100% when conditions are met, and eventually replace the control variant to become the default version of the flow.
        """
        return pulumi.get(self, "rollout_config")

    @property
    @pulumi.getter(name="rolloutFailureReason")
    def rollout_failure_reason(self) -> str:
        """
        The reason why rollout has failed. Should only be set when state is ROLLOUT_FAILED.
        """
        return pulumi.get(self, "rollout_failure_reason")

    @property
    @pulumi.getter(name="rolloutState")
    def rollout_state(self) -> 'outputs.GoogleCloudDialogflowCxV3beta1RolloutStateResponse':
        """
        State of the auto rollout process.
        """
        return pulumi.get(self, "rollout_state")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        Start time of this experiment.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the experiment. Transition triggered by Experiments.StartExperiment: DRAFT->RUNNING. Transition triggered by Experiments.CancelExperiment: DRAFT->DONE or RUNNING->DONE.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="variantsHistory")
    def variants_history(self) -> Sequence['outputs.GoogleCloudDialogflowCxV3beta1VariantsHistoryResponse']:
        """
        The history of updates to the experiment variants.
        """
        return pulumi.get(self, "variants_history")


class AwaitableGetExperimentResult(GetExperimentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExperimentResult(
            create_time=self.create_time,
            definition=self.definition,
            description=self.description,
            display_name=self.display_name,
            end_time=self.end_time,
            experiment_length=self.experiment_length,
            last_update_time=self.last_update_time,
            name=self.name,
            result=self.result,
            rollout_config=self.rollout_config,
            rollout_failure_reason=self.rollout_failure_reason,
            rollout_state=self.rollout_state,
            start_time=self.start_time,
            state=self.state,
            variants_history=self.variants_history)


def get_experiment(agent_id: Optional[str] = None,
                   environment_id: Optional[str] = None,
                   experiment_id: Optional[str] = None,
                   location: Optional[str] = None,
                   project: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExperimentResult:
    """
    Retrieves the specified Experiment.
    """
    __args__ = dict()
    __args__['agentId'] = agent_id
    __args__['environmentId'] = environment_id
    __args__['experimentId'] = experiment_id
    __args__['location'] = location
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:dialogflow/v3beta1:getExperiment', __args__, opts=opts, typ=GetExperimentResult).value

    return AwaitableGetExperimentResult(
        create_time=__ret__.create_time,
        definition=__ret__.definition,
        description=__ret__.description,
        display_name=__ret__.display_name,
        end_time=__ret__.end_time,
        experiment_length=__ret__.experiment_length,
        last_update_time=__ret__.last_update_time,
        name=__ret__.name,
        result=__ret__.result,
        rollout_config=__ret__.rollout_config,
        rollout_failure_reason=__ret__.rollout_failure_reason,
        rollout_state=__ret__.rollout_state,
        start_time=__ret__.start_time,
        state=__ret__.state,
        variants_history=__ret__.variants_history)


@_utilities.lift_output_func(get_experiment)
def get_experiment_output(agent_id: Optional[pulumi.Input[str]] = None,
                          environment_id: Optional[pulumi.Input[str]] = None,
                          experiment_id: Optional[pulumi.Input[str]] = None,
                          location: Optional[pulumi.Input[str]] = None,
                          project: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExperimentResult]:
    """
    Retrieves the specified Experiment.
    """
    ...
