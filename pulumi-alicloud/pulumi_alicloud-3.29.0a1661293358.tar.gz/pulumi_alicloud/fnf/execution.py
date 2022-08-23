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
                 execution_name: pulumi.Input[str],
                 flow_name: pulumi.Input[str],
                 input: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Execution resource.
        :param pulumi.Input[str] execution_name: The name of the execution.
        :param pulumi.Input[str] flow_name: The name of the flow.
        :param pulumi.Input[str] input: The Input information for this execution.
        :param pulumi.Input[str] status: The status of the resource. Valid values: `Stopped`.
        """
        pulumi.set(__self__, "execution_name", execution_name)
        pulumi.set(__self__, "flow_name", flow_name)
        if input is not None:
            pulumi.set(__self__, "input", input)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="executionName")
    def execution_name(self) -> pulumi.Input[str]:
        """
        The name of the execution.
        """
        return pulumi.get(self, "execution_name")

    @execution_name.setter
    def execution_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "execution_name", value)

    @property
    @pulumi.getter(name="flowName")
    def flow_name(self) -> pulumi.Input[str]:
        """
        The name of the flow.
        """
        return pulumi.get(self, "flow_name")

    @flow_name.setter
    def flow_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "flow_name", value)

    @property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[str]]:
        """
        The Input information for this execution.
        """
        return pulumi.get(self, "input")

    @input.setter
    def input(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the resource. Valid values: `Stopped`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _ExecutionState:
    def __init__(__self__, *,
                 execution_name: Optional[pulumi.Input[str]] = None,
                 flow_name: Optional[pulumi.Input[str]] = None,
                 input: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Execution resources.
        :param pulumi.Input[str] execution_name: The name of the execution.
        :param pulumi.Input[str] flow_name: The name of the flow.
        :param pulumi.Input[str] input: The Input information for this execution.
        :param pulumi.Input[str] status: The status of the resource. Valid values: `Stopped`.
        """
        if execution_name is not None:
            pulumi.set(__self__, "execution_name", execution_name)
        if flow_name is not None:
            pulumi.set(__self__, "flow_name", flow_name)
        if input is not None:
            pulumi.set(__self__, "input", input)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="executionName")
    def execution_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the execution.
        """
        return pulumi.get(self, "execution_name")

    @execution_name.setter
    def execution_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "execution_name", value)

    @property
    @pulumi.getter(name="flowName")
    def flow_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the flow.
        """
        return pulumi.get(self, "flow_name")

    @flow_name.setter
    def flow_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "flow_name", value)

    @property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[str]]:
        """
        The Input information for this execution.
        """
        return pulumi.get(self, "input")

    @input.setter
    def input(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the resource. Valid values: `Stopped`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class Execution(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 execution_name: Optional[pulumi.Input[str]] = None,
                 flow_name: Optional[pulumi.Input[str]] = None,
                 input: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Serverless Workflow Execution resource.

        For information about Serverless Workflow Execution and how to use it, see [What is Execution](https://www.alibabacloud.com/help/en/doc-detail/122628.html).

        > **NOTE:** Available in v1.149.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-testacc-fnfflow"
        default_role = alicloud.ram.Role("defaultRole", document=\"\"\"  {
            "Statement": [
              {
                "Action": "sts:AssumeRole",
                "Effect": "Allow",
                "Principal": {
                  "Service": [
                    "fnf.aliyuncs.com"
                  ]
                }
              }
            ],
            "Version": "1"
          }
        \"\"\")
        default_flow = alicloud.fnf.Flow("defaultFlow",
            definition=\"\"\"  version: v1beta1
          type: flow
          steps:
            - type: wait
              name: custom_wait
              duration: $.wait
        \"\"\",
            role_arn=default_role.arn,
            description="Test for terraform fnf_flow.",
            type="FDL")
        default_execution = alicloud.fnf.Execution("defaultExecution",
            execution_name=name,
            flow_name=default_flow.name,
            input="{\\"wait\\": 600}")
        ```

        ## Import

        Serverless Workflow Execution can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:fnf/execution:Execution example <flow_name>:<execution_name>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] execution_name: The name of the execution.
        :param pulumi.Input[str] flow_name: The name of the flow.
        :param pulumi.Input[str] input: The Input information for this execution.
        :param pulumi.Input[str] status: The status of the resource. Valid values: `Stopped`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExecutionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Serverless Workflow Execution resource.

        For information about Serverless Workflow Execution and how to use it, see [What is Execution](https://www.alibabacloud.com/help/en/doc-detail/122628.html).

        > **NOTE:** Available in v1.149.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-testacc-fnfflow"
        default_role = alicloud.ram.Role("defaultRole", document=\"\"\"  {
            "Statement": [
              {
                "Action": "sts:AssumeRole",
                "Effect": "Allow",
                "Principal": {
                  "Service": [
                    "fnf.aliyuncs.com"
                  ]
                }
              }
            ],
            "Version": "1"
          }
        \"\"\")
        default_flow = alicloud.fnf.Flow("defaultFlow",
            definition=\"\"\"  version: v1beta1
          type: flow
          steps:
            - type: wait
              name: custom_wait
              duration: $.wait
        \"\"\",
            role_arn=default_role.arn,
            description="Test for terraform fnf_flow.",
            type="FDL")
        default_execution = alicloud.fnf.Execution("defaultExecution",
            execution_name=name,
            flow_name=default_flow.name,
            input="{\\"wait\\": 600}")
        ```

        ## Import

        Serverless Workflow Execution can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:fnf/execution:Execution example <flow_name>:<execution_name>
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
                 execution_name: Optional[pulumi.Input[str]] = None,
                 flow_name: Optional[pulumi.Input[str]] = None,
                 input: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExecutionArgs.__new__(ExecutionArgs)

            if execution_name is None and not opts.urn:
                raise TypeError("Missing required property 'execution_name'")
            __props__.__dict__["execution_name"] = execution_name
            if flow_name is None and not opts.urn:
                raise TypeError("Missing required property 'flow_name'")
            __props__.__dict__["flow_name"] = flow_name
            __props__.__dict__["input"] = input
            __props__.__dict__["status"] = status
        super(Execution, __self__).__init__(
            'alicloud:fnf/execution:Execution',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            execution_name: Optional[pulumi.Input[str]] = None,
            flow_name: Optional[pulumi.Input[str]] = None,
            input: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'Execution':
        """
        Get an existing Execution resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] execution_name: The name of the execution.
        :param pulumi.Input[str] flow_name: The name of the flow.
        :param pulumi.Input[str] input: The Input information for this execution.
        :param pulumi.Input[str] status: The status of the resource. Valid values: `Stopped`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExecutionState.__new__(_ExecutionState)

        __props__.__dict__["execution_name"] = execution_name
        __props__.__dict__["flow_name"] = flow_name
        __props__.__dict__["input"] = input
        __props__.__dict__["status"] = status
        return Execution(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="executionName")
    def execution_name(self) -> pulumi.Output[str]:
        """
        The name of the execution.
        """
        return pulumi.get(self, "execution_name")

    @property
    @pulumi.getter(name="flowName")
    def flow_name(self) -> pulumi.Output[str]:
        """
        The name of the flow.
        """
        return pulumi.get(self, "flow_name")

    @property
    @pulumi.getter
    def input(self) -> pulumi.Output[Optional[str]]:
        """
        The Input information for this execution.
        """
        return pulumi.get(self, "input")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the resource. Valid values: `Stopped`.
        """
        return pulumi.get(self, "status")

