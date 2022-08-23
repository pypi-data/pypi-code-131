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
    'GetTaskResult',
    'AwaitableGetTaskResult',
    'get_task',
    'get_task_output',
]

@pulumi.output_type
class GetTaskResult:
    def __init__(__self__, create_time=None, description=None, display_name=None, execution_spec=None, execution_status=None, labels=None, name=None, spark=None, state=None, trigger_spec=None, uid=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if execution_spec and not isinstance(execution_spec, dict):
            raise TypeError("Expected argument 'execution_spec' to be a dict")
        pulumi.set(__self__, "execution_spec", execution_spec)
        if execution_status and not isinstance(execution_status, dict):
            raise TypeError("Expected argument 'execution_status' to be a dict")
        pulumi.set(__self__, "execution_status", execution_status)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if spark and not isinstance(spark, dict):
            raise TypeError("Expected argument 'spark' to be a dict")
        pulumi.set(__self__, "spark", spark)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if trigger_spec and not isinstance(trigger_spec, dict):
            raise TypeError("Expected argument 'trigger_spec' to be a dict")
        pulumi.set(__self__, "trigger_spec", trigger_spec)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time when the task was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional. Description of the task.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Optional. User friendly display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="executionSpec")
    def execution_spec(self) -> 'outputs.GoogleCloudDataplexV1TaskExecutionSpecResponse':
        """
        Spec related to how a task is executed.
        """
        return pulumi.get(self, "execution_spec")

    @property
    @pulumi.getter(name="executionStatus")
    def execution_status(self) -> 'outputs.GoogleCloudDataplexV1TaskExecutionStatusResponse':
        """
        Status of the latest task executions.
        """
        return pulumi.get(self, "execution_status")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Optional. User-defined labels for the task.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The relative resource name of the task, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/ tasks/{task_id}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def spark(self) -> 'outputs.GoogleCloudDataplexV1TaskSparkTaskConfigResponse':
        """
        Config related to running custom Spark tasks.
        """
        return pulumi.get(self, "spark")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Current state of the task.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="triggerSpec")
    def trigger_spec(self) -> 'outputs.GoogleCloudDataplexV1TaskTriggerSpecResponse':
        """
        Spec related to how often and when a task should be triggered.
        """
        return pulumi.get(self, "trigger_spec")

    @property
    @pulumi.getter
    def uid(self) -> str:
        """
        System generated globally unique ID for the task. This ID will be different if the task is deleted and re-created with the same name.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time when the task was last updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetTaskResult(GetTaskResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTaskResult(
            create_time=self.create_time,
            description=self.description,
            display_name=self.display_name,
            execution_spec=self.execution_spec,
            execution_status=self.execution_status,
            labels=self.labels,
            name=self.name,
            spark=self.spark,
            state=self.state,
            trigger_spec=self.trigger_spec,
            uid=self.uid,
            update_time=self.update_time)


def get_task(lake_id: Optional[str] = None,
             location: Optional[str] = None,
             project: Optional[str] = None,
             task_id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTaskResult:
    """
    Get task resource.
    """
    __args__ = dict()
    __args__['lakeId'] = lake_id
    __args__['location'] = location
    __args__['project'] = project
    __args__['taskId'] = task_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:dataplex/v1:getTask', __args__, opts=opts, typ=GetTaskResult).value

    return AwaitableGetTaskResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        display_name=__ret__.display_name,
        execution_spec=__ret__.execution_spec,
        execution_status=__ret__.execution_status,
        labels=__ret__.labels,
        name=__ret__.name,
        spark=__ret__.spark,
        state=__ret__.state,
        trigger_spec=__ret__.trigger_spec,
        uid=__ret__.uid,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_task)
def get_task_output(lake_id: Optional[pulumi.Input[str]] = None,
                    location: Optional[pulumi.Input[str]] = None,
                    project: Optional[pulumi.Input[Optional[str]]] = None,
                    task_id: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTaskResult]:
    """
    Get task resource.
    """
    ...
