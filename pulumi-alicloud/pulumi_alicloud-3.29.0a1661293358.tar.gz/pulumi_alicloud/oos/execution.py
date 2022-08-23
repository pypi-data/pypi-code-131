# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ExecutionArgs', 'Execution']

@pulumi.input_type
class ExecutionArgs:
    def __init__(__self__, *,
                 template_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 loop_mode: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[str]] = None,
                 parent_execution_id: Optional[pulumi.Input[str]] = None,
                 safety_check: Optional[pulumi.Input[str]] = None,
                 template_content: Optional[pulumi.Input[str]] = None,
                 template_version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Execution resource.
        :param pulumi.Input[str] template_name: The name of execution template.
        :param pulumi.Input[str] description: The description of OOS Execution.
        :param pulumi.Input[str] loop_mode: The loop mode of OOS Execution.
        :param pulumi.Input[str] mode: The mode of OOS Execution. Valid: `Automatic`, `Debug`. Default to `Automatic`.
        :param pulumi.Input[str] parameters: The parameters required by the template. Default to `{}`.
        :param pulumi.Input[str] parent_execution_id: The id of parent execution.
        :param pulumi.Input[str] safety_check: The mode of safety check.
        :param pulumi.Input[str] template_content: The content of template. When the user selects an existing template to create and execute a task, it is not necessary to pass in this field.
        :param pulumi.Input[str] template_version: The version of execution template.
        """
        pulumi.set(__self__, "template_name", template_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if loop_mode is not None:
            pulumi.set(__self__, "loop_mode", loop_mode)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if parent_execution_id is not None:
            pulumi.set(__self__, "parent_execution_id", parent_execution_id)
        if safety_check is not None:
            pulumi.set(__self__, "safety_check", safety_check)
        if template_content is not None:
            pulumi.set(__self__, "template_content", template_content)
        if template_version is not None:
            pulumi.set(__self__, "template_version", template_version)

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Input[str]:
        """
        The name of execution template.
        """
        return pulumi.get(self, "template_name")

    @template_name.setter
    def template_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "template_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of OOS Execution.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="loopMode")
    def loop_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The loop mode of OOS Execution.
        """
        return pulumi.get(self, "loop_mode")

    @loop_mode.setter
    def loop_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "loop_mode", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of OOS Execution. Valid: `Automatic`, `Debug`. Default to `Automatic`.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[str]]:
        """
        The parameters required by the template. Default to `{}`.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="parentExecutionId")
    def parent_execution_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of parent execution.
        """
        return pulumi.get(self, "parent_execution_id")

    @parent_execution_id.setter
    def parent_execution_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_execution_id", value)

    @property
    @pulumi.getter(name="safetyCheck")
    def safety_check(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of safety check.
        """
        return pulumi.get(self, "safety_check")

    @safety_check.setter
    def safety_check(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "safety_check", value)

    @property
    @pulumi.getter(name="templateContent")
    def template_content(self) -> Optional[pulumi.Input[str]]:
        """
        The content of template. When the user selects an existing template to create and execute a task, it is not necessary to pass in this field.
        """
        return pulumi.get(self, "template_content")

    @template_content.setter
    def template_content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_content", value)

    @property
    @pulumi.getter(name="templateVersion")
    def template_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of execution template.
        """
        return pulumi.get(self, "template_version")

    @template_version.setter
    def template_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_version", value)


@pulumi.input_type
class _ExecutionState:
    def __init__(__self__, *,
                 counters: Optional[pulumi.Input[str]] = None,
                 create_date: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 executed_by: Optional[pulumi.Input[str]] = None,
                 is_parent: Optional[pulumi.Input[bool]] = None,
                 loop_mode: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 outputs: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[str]] = None,
                 parent_execution_id: Optional[pulumi.Input[str]] = None,
                 ram_role: Optional[pulumi.Input[str]] = None,
                 safety_check: Optional[pulumi.Input[str]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 status_message: Optional[pulumi.Input[str]] = None,
                 template_content: Optional[pulumi.Input[str]] = None,
                 template_id: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 template_version: Optional[pulumi.Input[str]] = None,
                 update_date: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Execution resources.
        :param pulumi.Input[str] counters: The counters of OOS Execution.
        :param pulumi.Input[str] create_date: The time when the execution was created.
        :param pulumi.Input[str] description: The description of OOS Execution.
        :param pulumi.Input[str] end_date: The time when the execution was ended.
        :param pulumi.Input[str] executed_by: The user who execute the template.
        :param pulumi.Input[bool] is_parent: Whether to include subtasks.
        :param pulumi.Input[str] loop_mode: The loop mode of OOS Execution.
        :param pulumi.Input[str] mode: The mode of OOS Execution. Valid: `Automatic`, `Debug`. Default to `Automatic`.
        :param pulumi.Input[str] outputs: The outputs of OOS Execution.
        :param pulumi.Input[str] parameters: The parameters required by the template. Default to `{}`.
        :param pulumi.Input[str] parent_execution_id: The id of parent execution.
        :param pulumi.Input[str] ram_role: The role that executes the current template.
        :param pulumi.Input[str] safety_check: The mode of safety check.
        :param pulumi.Input[str] start_date: The time when the execution was started.
        :param pulumi.Input[str] status: The status of OOS Execution.
        :param pulumi.Input[str] status_message: The message of status.
        :param pulumi.Input[str] template_content: The content of template. When the user selects an existing template to create and execute a task, it is not necessary to pass in this field.
        :param pulumi.Input[str] template_id: The id of template.
        :param pulumi.Input[str] template_name: The name of execution template.
        :param pulumi.Input[str] template_version: The version of execution template.
        :param pulumi.Input[str] update_date: The time when the execution was updated.
        """
        if counters is not None:
            pulumi.set(__self__, "counters", counters)
        if create_date is not None:
            pulumi.set(__self__, "create_date", create_date)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if end_date is not None:
            pulumi.set(__self__, "end_date", end_date)
        if executed_by is not None:
            pulumi.set(__self__, "executed_by", executed_by)
        if is_parent is not None:
            pulumi.set(__self__, "is_parent", is_parent)
        if loop_mode is not None:
            pulumi.set(__self__, "loop_mode", loop_mode)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if outputs is not None:
            pulumi.set(__self__, "outputs", outputs)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if parent_execution_id is not None:
            pulumi.set(__self__, "parent_execution_id", parent_execution_id)
        if ram_role is not None:
            pulumi.set(__self__, "ram_role", ram_role)
        if safety_check is not None:
            pulumi.set(__self__, "safety_check", safety_check)
        if start_date is not None:
            pulumi.set(__self__, "start_date", start_date)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if status_message is not None:
            pulumi.set(__self__, "status_message", status_message)
        if template_content is not None:
            pulumi.set(__self__, "template_content", template_content)
        if template_id is not None:
            pulumi.set(__self__, "template_id", template_id)
        if template_name is not None:
            pulumi.set(__self__, "template_name", template_name)
        if template_version is not None:
            pulumi.set(__self__, "template_version", template_version)
        if update_date is not None:
            pulumi.set(__self__, "update_date", update_date)

    @property
    @pulumi.getter
    def counters(self) -> Optional[pulumi.Input[str]]:
        """
        The counters of OOS Execution.
        """
        return pulumi.get(self, "counters")

    @counters.setter
    def counters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "counters", value)

    @property
    @pulumi.getter(name="createDate")
    def create_date(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the execution was created.
        """
        return pulumi.get(self, "create_date")

    @create_date.setter
    def create_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_date", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of OOS Execution.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the execution was ended.
        """
        return pulumi.get(self, "end_date")

    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_date", value)

    @property
    @pulumi.getter(name="executedBy")
    def executed_by(self) -> Optional[pulumi.Input[str]]:
        """
        The user who execute the template.
        """
        return pulumi.get(self, "executed_by")

    @executed_by.setter
    def executed_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "executed_by", value)

    @property
    @pulumi.getter(name="isParent")
    def is_parent(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to include subtasks.
        """
        return pulumi.get(self, "is_parent")

    @is_parent.setter
    def is_parent(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_parent", value)

    @property
    @pulumi.getter(name="loopMode")
    def loop_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The loop mode of OOS Execution.
        """
        return pulumi.get(self, "loop_mode")

    @loop_mode.setter
    def loop_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "loop_mode", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of OOS Execution. Valid: `Automatic`, `Debug`. Default to `Automatic`.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def outputs(self) -> Optional[pulumi.Input[str]]:
        """
        The outputs of OOS Execution.
        """
        return pulumi.get(self, "outputs")

    @outputs.setter
    def outputs(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "outputs", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[str]]:
        """
        The parameters required by the template. Default to `{}`.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="parentExecutionId")
    def parent_execution_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of parent execution.
        """
        return pulumi.get(self, "parent_execution_id")

    @parent_execution_id.setter
    def parent_execution_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_execution_id", value)

    @property
    @pulumi.getter(name="ramRole")
    def ram_role(self) -> Optional[pulumi.Input[str]]:
        """
        The role that executes the current template.
        """
        return pulumi.get(self, "ram_role")

    @ram_role.setter
    def ram_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ram_role", value)

    @property
    @pulumi.getter(name="safetyCheck")
    def safety_check(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of safety check.
        """
        return pulumi.get(self, "safety_check")

    @safety_check.setter
    def safety_check(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "safety_check", value)

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the execution was started.
        """
        return pulumi.get(self, "start_date")

    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_date", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of OOS Execution.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[pulumi.Input[str]]:
        """
        The message of status.
        """
        return pulumi.get(self, "status_message")

    @status_message.setter
    def status_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status_message", value)

    @property
    @pulumi.getter(name="templateContent")
    def template_content(self) -> Optional[pulumi.Input[str]]:
        """
        The content of template. When the user selects an existing template to create and execute a task, it is not necessary to pass in this field.
        """
        return pulumi.get(self, "template_content")

    @template_content.setter
    def template_content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_content", value)

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of template.
        """
        return pulumi.get(self, "template_id")

    @template_id.setter
    def template_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_id", value)

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of execution template.
        """
        return pulumi.get(self, "template_name")

    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_name", value)

    @property
    @pulumi.getter(name="templateVersion")
    def template_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of execution template.
        """
        return pulumi.get(self, "template_version")

    @template_version.setter
    def template_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_version", value)

    @property
    @pulumi.getter(name="updateDate")
    def update_date(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the execution was updated.
        """
        return pulumi.get(self, "update_date")

    @update_date.setter
    def update_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_date", value)


class Execution(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 loop_mode: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[str]] = None,
                 parent_execution_id: Optional[pulumi.Input[str]] = None,
                 safety_check: Optional[pulumi.Input[str]] = None,
                 template_content: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 template_version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a OOS Execution resource. For information about Alicloud OOS Execution and how to use it, see [What is Resource Alicloud OOS Execution](https://www.alibabacloud.com/help/doc-detail/120771.htm).

        > **NOTE:** Available in 1.93.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.oos.Template("default",
            content=\"\"\"  {
            "FormatVersion": "OOS-2019-06-01",
            "Description": "Update Describe instances of given status",
            "Parameters":{
              "Status":{
                "Type": "String",
                "Description": "(Required) The status of the Ecs instance."
              }
            },
            "Tasks": [
              {
                "Properties" :{
                  "Parameters":{
                    "Status": "{{ Status }}"
                  },
                  "API": "DescribeInstances",
                  "Service": "Ecs"
                },
                "Name": "foo",
                "Action": "ACS::ExecuteApi"
              }]
          }
        \"\"\",
            template_name="test-name",
            version_name="test",
            tags={
                "Created": "TF",
                "For": "acceptance Test",
            })
        example = alicloud.oos.Execution("example",
            template_name=default.template_name,
            description="From TF Test",
            parameters="				{\\"Status\\":\\"Running\\"}\\n")
        ```

        ## Import

        OOS Execution can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:oos/execution:Execution example exec-ef6xxxx
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of OOS Execution.
        :param pulumi.Input[str] loop_mode: The loop mode of OOS Execution.
        :param pulumi.Input[str] mode: The mode of OOS Execution. Valid: `Automatic`, `Debug`. Default to `Automatic`.
        :param pulumi.Input[str] parameters: The parameters required by the template. Default to `{}`.
        :param pulumi.Input[str] parent_execution_id: The id of parent execution.
        :param pulumi.Input[str] safety_check: The mode of safety check.
        :param pulumi.Input[str] template_content: The content of template. When the user selects an existing template to create and execute a task, it is not necessary to pass in this field.
        :param pulumi.Input[str] template_name: The name of execution template.
        :param pulumi.Input[str] template_version: The version of execution template.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExecutionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a OOS Execution resource. For information about Alicloud OOS Execution and how to use it, see [What is Resource Alicloud OOS Execution](https://www.alibabacloud.com/help/doc-detail/120771.htm).

        > **NOTE:** Available in 1.93.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.oos.Template("default",
            content=\"\"\"  {
            "FormatVersion": "OOS-2019-06-01",
            "Description": "Update Describe instances of given status",
            "Parameters":{
              "Status":{
                "Type": "String",
                "Description": "(Required) The status of the Ecs instance."
              }
            },
            "Tasks": [
              {
                "Properties" :{
                  "Parameters":{
                    "Status": "{{ Status }}"
                  },
                  "API": "DescribeInstances",
                  "Service": "Ecs"
                },
                "Name": "foo",
                "Action": "ACS::ExecuteApi"
              }]
          }
        \"\"\",
            template_name="test-name",
            version_name="test",
            tags={
                "Created": "TF",
                "For": "acceptance Test",
            })
        example = alicloud.oos.Execution("example",
            template_name=default.template_name,
            description="From TF Test",
            parameters="				{\\"Status\\":\\"Running\\"}\\n")
        ```

        ## Import

        OOS Execution can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:oos/execution:Execution example exec-ef6xxxx
        ```

        :param str resource_name: The name of the resource.
        :param ExecutionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExecutionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 loop_mode: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[str]] = None,
                 parent_execution_id: Optional[pulumi.Input[str]] = None,
                 safety_check: Optional[pulumi.Input[str]] = None,
                 template_content: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 template_version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExecutionArgs.__new__(ExecutionArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["loop_mode"] = loop_mode
            __props__.__dict__["mode"] = mode
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["parent_execution_id"] = parent_execution_id
            __props__.__dict__["safety_check"] = safety_check
            __props__.__dict__["template_content"] = template_content
            if template_name is None and not opts.urn:
                raise TypeError("Missing required property 'template_name'")
            __props__.__dict__["template_name"] = template_name
            __props__.__dict__["template_version"] = template_version
            __props__.__dict__["counters"] = None
            __props__.__dict__["create_date"] = None
            __props__.__dict__["end_date"] = None
            __props__.__dict__["executed_by"] = None
            __props__.__dict__["is_parent"] = None
            __props__.__dict__["outputs"] = None
            __props__.__dict__["ram_role"] = None
            __props__.__dict__["start_date"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_message"] = None
            __props__.__dict__["template_id"] = None
            __props__.__dict__["update_date"] = None
        super(Execution, __self__).__init__(
            'alicloud:oos/execution:Execution',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            counters: Optional[pulumi.Input[str]] = None,
            create_date: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            end_date: Optional[pulumi.Input[str]] = None,
            executed_by: Optional[pulumi.Input[str]] = None,
            is_parent: Optional[pulumi.Input[bool]] = None,
            loop_mode: Optional[pulumi.Input[str]] = None,
            mode: Optional[pulumi.Input[str]] = None,
            outputs: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[str]] = None,
            parent_execution_id: Optional[pulumi.Input[str]] = None,
            ram_role: Optional[pulumi.Input[str]] = None,
            safety_check: Optional[pulumi.Input[str]] = None,
            start_date: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            status_message: Optional[pulumi.Input[str]] = None,
            template_content: Optional[pulumi.Input[str]] = None,
            template_id: Optional[pulumi.Input[str]] = None,
            template_name: Optional[pulumi.Input[str]] = None,
            template_version: Optional[pulumi.Input[str]] = None,
            update_date: Optional[pulumi.Input[str]] = None) -> 'Execution':
        """
        Get an existing Execution resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] counters: The counters of OOS Execution.
        :param pulumi.Input[str] create_date: The time when the execution was created.
        :param pulumi.Input[str] description: The description of OOS Execution.
        :param pulumi.Input[str] end_date: The time when the execution was ended.
        :param pulumi.Input[str] executed_by: The user who execute the template.
        :param pulumi.Input[bool] is_parent: Whether to include subtasks.
        :param pulumi.Input[str] loop_mode: The loop mode of OOS Execution.
        :param pulumi.Input[str] mode: The mode of OOS Execution. Valid: `Automatic`, `Debug`. Default to `Automatic`.
        :param pulumi.Input[str] outputs: The outputs of OOS Execution.
        :param pulumi.Input[str] parameters: The parameters required by the template. Default to `{}`.
        :param pulumi.Input[str] parent_execution_id: The id of parent execution.
        :param pulumi.Input[str] ram_role: The role that executes the current template.
        :param pulumi.Input[str] safety_check: The mode of safety check.
        :param pulumi.Input[str] start_date: The time when the execution was started.
        :param pulumi.Input[str] status: The status of OOS Execution.
        :param pulumi.Input[str] status_message: The message of status.
        :param pulumi.Input[str] template_content: The content of template. When the user selects an existing template to create and execute a task, it is not necessary to pass in this field.
        :param pulumi.Input[str] template_id: The id of template.
        :param pulumi.Input[str] template_name: The name of execution template.
        :param pulumi.Input[str] template_version: The version of execution template.
        :param pulumi.Input[str] update_date: The time when the execution was updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExecutionState.__new__(_ExecutionState)

        __props__.__dict__["counters"] = counters
        __props__.__dict__["create_date"] = create_date
        __props__.__dict__["description"] = description
        __props__.__dict__["end_date"] = end_date
        __props__.__dict__["executed_by"] = executed_by
        __props__.__dict__["is_parent"] = is_parent
        __props__.__dict__["loop_mode"] = loop_mode
        __props__.__dict__["mode"] = mode
        __props__.__dict__["outputs"] = outputs
        __props__.__dict__["parameters"] = parameters
        __props__.__dict__["parent_execution_id"] = parent_execution_id
        __props__.__dict__["ram_role"] = ram_role
        __props__.__dict__["safety_check"] = safety_check
        __props__.__dict__["start_date"] = start_date
        __props__.__dict__["status"] = status
        __props__.__dict__["status_message"] = status_message
        __props__.__dict__["template_content"] = template_content
        __props__.__dict__["template_id"] = template_id
        __props__.__dict__["template_name"] = template_name
        __props__.__dict__["template_version"] = template_version
        __props__.__dict__["update_date"] = update_date
        return Execution(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def counters(self) -> pulumi.Output[str]:
        """
        The counters of OOS Execution.
        """
        return pulumi.get(self, "counters")

    @property
    @pulumi.getter(name="createDate")
    def create_date(self) -> pulumi.Output[str]:
        """
        The time when the execution was created.
        """
        return pulumi.get(self, "create_date")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of OOS Execution.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[str]:
        """
        The time when the execution was ended.
        """
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter(name="executedBy")
    def executed_by(self) -> pulumi.Output[str]:
        """
        The user who execute the template.
        """
        return pulumi.get(self, "executed_by")

    @property
    @pulumi.getter(name="isParent")
    def is_parent(self) -> pulumi.Output[bool]:
        """
        Whether to include subtasks.
        """
        return pulumi.get(self, "is_parent")

    @property
    @pulumi.getter(name="loopMode")
    def loop_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The loop mode of OOS Execution.
        """
        return pulumi.get(self, "loop_mode")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[str]]:
        """
        The mode of OOS Execution. Valid: `Automatic`, `Debug`. Default to `Automatic`.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def outputs(self) -> pulumi.Output[str]:
        """
        The outputs of OOS Execution.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[str]]:
        """
        The parameters required by the template. Default to `{}`.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="parentExecutionId")
    def parent_execution_id(self) -> pulumi.Output[Optional[str]]:
        """
        The id of parent execution.
        """
        return pulumi.get(self, "parent_execution_id")

    @property
    @pulumi.getter(name="ramRole")
    def ram_role(self) -> pulumi.Output[str]:
        """
        The role that executes the current template.
        """
        return pulumi.get(self, "ram_role")

    @property
    @pulumi.getter(name="safetyCheck")
    def safety_check(self) -> pulumi.Output[Optional[str]]:
        """
        The mode of safety check.
        """
        return pulumi.get(self, "safety_check")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[str]:
        """
        The time when the execution was started.
        """
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of OOS Execution.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[str]:
        """
        The message of status.
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter(name="templateContent")
    def template_content(self) -> pulumi.Output[Optional[str]]:
        """
        The content of template. When the user selects an existing template to create and execute a task, it is not necessary to pass in this field.
        """
        return pulumi.get(self, "template_content")

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> pulumi.Output[str]:
        """
        The id of template.
        """
        return pulumi.get(self, "template_id")

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Output[str]:
        """
        The name of execution template.
        """
        return pulumi.get(self, "template_name")

    @property
    @pulumi.getter(name="templateVersion")
    def template_version(self) -> pulumi.Output[str]:
        """
        The version of execution template.
        """
        return pulumi.get(self, "template_version")

    @property
    @pulumi.getter(name="updateDate")
    def update_date(self) -> pulumi.Output[str]:
        """
        The time when the execution was updated.
        """
        return pulumi.get(self, "update_date")

