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
from ._inputs import *

__all__ = ['EnvironmentArgs', 'Environment']

@pulumi.input_type
class EnvironmentArgs:
    def __init__(__self__, *,
                 agent_id: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 version_configs: pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3EnvironmentVersionConfigArgs']]],
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 test_cases_config: Optional[pulumi.Input['GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigArgs']] = None,
                 webhook_config: Optional[pulumi.Input['GoogleCloudDialogflowCxV3EnvironmentWebhookConfigArgs']] = None):
        """
        The set of arguments for constructing a Environment resource.
        :param pulumi.Input[str] display_name: The human-readable name of the environment (unique in an agent). Limit of 64 characters.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3EnvironmentVersionConfigArgs']]] version_configs: A list of configurations for flow versions. You should include version configs for all flows that are reachable from `Start Flow` in the agent. Otherwise, an error will be returned.
        :param pulumi.Input[str] description: The human-readable description of the environment. The maximum length is 500 characters. If exceeded, the request is rejected.
        :param pulumi.Input[str] name: The name of the environment. Format: `projects//locations//agents//environments/`.
        :param pulumi.Input['GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigArgs'] test_cases_config: The test cases config for continuous tests of this environment.
        :param pulumi.Input['GoogleCloudDialogflowCxV3EnvironmentWebhookConfigArgs'] webhook_config: The webhook configuration for this environment.
        """
        pulumi.set(__self__, "agent_id", agent_id)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "version_configs", version_configs)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if test_cases_config is not None:
            pulumi.set(__self__, "test_cases_config", test_cases_config)
        if webhook_config is not None:
            pulumi.set(__self__, "webhook_config", webhook_config)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The human-readable name of the environment (unique in an agent). Limit of 64 characters.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="versionConfigs")
    def version_configs(self) -> pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3EnvironmentVersionConfigArgs']]]:
        """
        A list of configurations for flow versions. You should include version configs for all flows that are reachable from `Start Flow` in the agent. Otherwise, an error will be returned.
        """
        return pulumi.get(self, "version_configs")

    @version_configs.setter
    def version_configs(self, value: pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3EnvironmentVersionConfigArgs']]]):
        pulumi.set(self, "version_configs", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The human-readable description of the environment. The maximum length is 500 characters. If exceeded, the request is rejected.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the environment. Format: `projects//locations//agents//environments/`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="testCasesConfig")
    def test_cases_config(self) -> Optional[pulumi.Input['GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigArgs']]:
        """
        The test cases config for continuous tests of this environment.
        """
        return pulumi.get(self, "test_cases_config")

    @test_cases_config.setter
    def test_cases_config(self, value: Optional[pulumi.Input['GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigArgs']]):
        pulumi.set(self, "test_cases_config", value)

    @property
    @pulumi.getter(name="webhookConfig")
    def webhook_config(self) -> Optional[pulumi.Input['GoogleCloudDialogflowCxV3EnvironmentWebhookConfigArgs']]:
        """
        The webhook configuration for this environment.
        """
        return pulumi.get(self, "webhook_config")

    @webhook_config.setter
    def webhook_config(self, value: Optional[pulumi.Input['GoogleCloudDialogflowCxV3EnvironmentWebhookConfigArgs']]):
        pulumi.set(self, "webhook_config", value)


class Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 test_cases_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigArgs']]] = None,
                 version_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3EnvironmentVersionConfigArgs']]]]] = None,
                 webhook_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3EnvironmentWebhookConfigArgs']]] = None,
                 __props__=None):
        """
        Creates an Environment in the specified Agent. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: Environment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The human-readable description of the environment. The maximum length is 500 characters. If exceeded, the request is rejected.
        :param pulumi.Input[str] display_name: The human-readable name of the environment (unique in an agent). Limit of 64 characters.
        :param pulumi.Input[str] name: The name of the environment. Format: `projects//locations//agents//environments/`.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigArgs']] test_cases_config: The test cases config for continuous tests of this environment.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3EnvironmentVersionConfigArgs']]]] version_configs: A list of configurations for flow versions. You should include version configs for all flows that are reachable from `Start Flow` in the agent. Otherwise, an error will be returned.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3EnvironmentWebhookConfigArgs']] webhook_config: The webhook configuration for this environment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an Environment in the specified Agent. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: Environment

        :param str resource_name: The name of the resource.
        :param EnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 test_cases_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigArgs']]] = None,
                 version_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3EnvironmentVersionConfigArgs']]]]] = None,
                 webhook_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3EnvironmentWebhookConfigArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

            if agent_id is None and not opts.urn:
                raise TypeError("Missing required property 'agent_id'")
            __props__.__dict__["agent_id"] = agent_id
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["test_cases_config"] = test_cases_config
            if version_configs is None and not opts.urn:
                raise TypeError("Missing required property 'version_configs'")
            __props__.__dict__["version_configs"] = version_configs
            __props__.__dict__["webhook_config"] = webhook_config
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["agent_id", "location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Environment, __self__).__init__(
            'google-native:dialogflow/v3:Environment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Environment':
        """
        Get an existing Environment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

        __props__.__dict__["agent_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["test_cases_config"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["version_configs"] = None
        __props__.__dict__["webhook_config"] = None
        return Environment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "agent_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The human-readable description of the environment. The maximum length is 500 characters. If exceeded, the request is rejected.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The human-readable name of the environment (unique in an agent). Limit of 64 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the environment. Format: `projects//locations//agents//environments/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="testCasesConfig")
    def test_cases_config(self) -> pulumi.Output['outputs.GoogleCloudDialogflowCxV3EnvironmentTestCasesConfigResponse']:
        """
        The test cases config for continuous tests of this environment.
        """
        return pulumi.get(self, "test_cases_config")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Update time of this environment.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="versionConfigs")
    def version_configs(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowCxV3EnvironmentVersionConfigResponse']]:
        """
        A list of configurations for flow versions. You should include version configs for all flows that are reachable from `Start Flow` in the agent. Otherwise, an error will be returned.
        """
        return pulumi.get(self, "version_configs")

    @property
    @pulumi.getter(name="webhookConfig")
    def webhook_config(self) -> pulumi.Output['outputs.GoogleCloudDialogflowCxV3EnvironmentWebhookConfigResponse']:
        """
        The webhook configuration for this environment.
        """
        return pulumi.get(self, "webhook_config")

