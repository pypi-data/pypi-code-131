# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ConfigMapArgs', 'ConfigMap']

@pulumi.input_type
class ConfigMapArgs:
    def __init__(__self__, *,
                 data: pulumi.Input[str],
                 namespace_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConfigMap resource.
        :param pulumi.Input[str] data: ConfigMap instance data.
        :param pulumi.Input[str] namespace_id: The NamespaceId of ConfigMap.It can contain 2 to 32 lowercase characters.The value is in format `{RegionId}:{namespace}`
        :param pulumi.Input[str] description: The Description of ConfigMap.
        :param pulumi.Input[str] name: ConfigMap instance name.
        """
        pulumi.set(__self__, "data", data)
        pulumi.set(__self__, "namespace_id", namespace_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def data(self) -> pulumi.Input[str]:
        """
        ConfigMap instance data.
        """
        return pulumi.get(self, "data")

    @data.setter
    def data(self, value: pulumi.Input[str]):
        pulumi.set(self, "data", value)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Input[str]:
        """
        The NamespaceId of ConfigMap.It can contain 2 to 32 lowercase characters.The value is in format `{RegionId}:{namespace}`
        """
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The Description of ConfigMap.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        ConfigMap instance name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ConfigMapState:
    def __init__(__self__, *,
                 data: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ConfigMap resources.
        :param pulumi.Input[str] data: ConfigMap instance data.
        :param pulumi.Input[str] description: The Description of ConfigMap.
        :param pulumi.Input[str] name: ConfigMap instance name.
        :param pulumi.Input[str] namespace_id: The NamespaceId of ConfigMap.It can contain 2 to 32 lowercase characters.The value is in format `{RegionId}:{namespace}`
        """
        if data is not None:
            pulumi.set(__self__, "data", data)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace_id is not None:
            pulumi.set(__self__, "namespace_id", namespace_id)

    @property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[str]]:
        """
        ConfigMap instance data.
        """
        return pulumi.get(self, "data")

    @data.setter
    def data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The Description of ConfigMap.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        ConfigMap instance name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The NamespaceId of ConfigMap.It can contain 2 to 32 lowercase characters.The value is in format `{RegionId}:{namespace}`
        """
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_id", value)


class ConfigMap(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Serverless App Engine (SAE) Config Map resource.

        For information about Serverless App Engine (SAE) Config Map and how to use it, see [What is Config Map](https://help.aliyun.com/document_detail/97792.html).

        > **NOTE:** Available in v1.130.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import json
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        config_map_name = config.get("configMapName")
        if config_map_name is None:
            config_map_name = "examplename"
        example_namespace = alicloud.sae.Namespace("exampleNamespace",
            namespace_id="cn-hangzhou:yourname",
            namespace_name="example_value",
            namespace_description="your_description")
        example_config_map = alicloud.sae.ConfigMap("exampleConfigMap",
            data=json.dumps({
                "env.home": "/root",
                "env.shell": "/bin/sh",
            }),
            namespace_id=example_namespace.namespace_id)
        ```

        ## Import

        Serverless App Engine (SAE) Config Map can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:sae/configMap:ConfigMap example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data: ConfigMap instance data.
        :param pulumi.Input[str] description: The Description of ConfigMap.
        :param pulumi.Input[str] name: ConfigMap instance name.
        :param pulumi.Input[str] namespace_id: The NamespaceId of ConfigMap.It can contain 2 to 32 lowercase characters.The value is in format `{RegionId}:{namespace}`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigMapArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Serverless App Engine (SAE) Config Map resource.

        For information about Serverless App Engine (SAE) Config Map and how to use it, see [What is Config Map](https://help.aliyun.com/document_detail/97792.html).

        > **NOTE:** Available in v1.130.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import json
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        config_map_name = config.get("configMapName")
        if config_map_name is None:
            config_map_name = "examplename"
        example_namespace = alicloud.sae.Namespace("exampleNamespace",
            namespace_id="cn-hangzhou:yourname",
            namespace_name="example_value",
            namespace_description="your_description")
        example_config_map = alicloud.sae.ConfigMap("exampleConfigMap",
            data=json.dumps({
                "env.home": "/root",
                "env.shell": "/bin/sh",
            }),
            namespace_id=example_namespace.namespace_id)
        ```

        ## Import

        Serverless App Engine (SAE) Config Map can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:sae/configMap:ConfigMap example <id>
        ```

        :param str resource_name: The name of the resource.
        :param ConfigMapArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigMapArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigMapArgs.__new__(ConfigMapArgs)

            if data is None and not opts.urn:
                raise TypeError("Missing required property 'data'")
            __props__.__dict__["data"] = data
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if namespace_id is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_id'")
            __props__.__dict__["namespace_id"] = namespace_id
        super(ConfigMap, __self__).__init__(
            'alicloud:sae/configMap:ConfigMap',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            data: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace_id: Optional[pulumi.Input[str]] = None) -> 'ConfigMap':
        """
        Get an existing ConfigMap resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data: ConfigMap instance data.
        :param pulumi.Input[str] description: The Description of ConfigMap.
        :param pulumi.Input[str] name: ConfigMap instance name.
        :param pulumi.Input[str] namespace_id: The NamespaceId of ConfigMap.It can contain 2 to 32 lowercase characters.The value is in format `{RegionId}:{namespace}`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConfigMapState.__new__(_ConfigMapState)

        __props__.__dict__["data"] = data
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace_id"] = namespace_id
        return ConfigMap(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def data(self) -> pulumi.Output[str]:
        """
        ConfigMap instance data.
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The Description of ConfigMap.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        ConfigMap instance name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Output[str]:
        """
        The NamespaceId of ConfigMap.It can contain 2 to 32 lowercase characters.The value is in format `{RegionId}:{namespace}`
        """
        return pulumi.get(self, "namespace_id")

