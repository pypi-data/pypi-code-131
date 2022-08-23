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
from ._enums import *
from ._inputs import *

__all__ = ['Hl7V2StoreArgs', 'Hl7V2Store']

@pulumi.input_type
class Hl7V2StoreArgs:
    def __init__(__self__, *,
                 dataset_id: pulumi.Input[str],
                 hl7_v2_store_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_config: Optional[pulumi.Input['NotificationConfigArgs']] = None,
                 notification_configs: Optional[pulumi.Input[Sequence[pulumi.Input['Hl7V2NotificationConfigArgs']]]] = None,
                 parser_config: Optional[pulumi.Input['ParserConfigArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 reject_duplicate_message: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Hl7V2Store resource.
        :param pulumi.Input[str] hl7_v2_store_id: The ID of the HL7v2 store that is being created. The string must match the following regex: `[\\p{L}\\p{N}_\\-\\.]{1,256}`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \\p{Ll}\\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        :param pulumi.Input[str] name: Resource name of the HL7v2 store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}`.
        :param pulumi.Input['NotificationConfigArgs'] notification_config: The notification destination all messages (both Ingest & Create) are published on. Only the message name is sent as part of the notification. If this is unset, no notifications are sent. Supplied by the client.
        :param pulumi.Input[Sequence[pulumi.Input['Hl7V2NotificationConfigArgs']]] notification_configs: A list of notification configs. Each configuration uses a filter to determine whether to publish a message (both Ingest & Create) on the corresponding notification destination. Only the message name is sent as part of the notification. Supplied by the client.
        :param pulumi.Input['ParserConfigArgs'] parser_config: The configuration for the parser. It determines how the server parses the messages.
        :param pulumi.Input[bool] reject_duplicate_message: Determines whether to reject duplicate messages. A duplicate message is a message with the same raw bytes as a message that has already been ingested/created in this HL7v2 store. The default value is false, meaning that the store accepts the duplicate messages and it also returns the same ACK message in the IngestMessageResponse as has been returned previously. Note that only one resource is created in the store. When this field is set to true, CreateMessage/IngestMessage requests with a duplicate message will be rejected by the store, and IngestMessageErrorDetail returns a NACK message upon rejection.
        """
        pulumi.set(__self__, "dataset_id", dataset_id)
        if hl7_v2_store_id is not None:
            pulumi.set(__self__, "hl7_v2_store_id", hl7_v2_store_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_config is not None:
            pulumi.set(__self__, "notification_config", notification_config)
        if notification_configs is not None:
            pulumi.set(__self__, "notification_configs", notification_configs)
        if parser_config is not None:
            pulumi.set(__self__, "parser_config", parser_config)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if reject_duplicate_message is not None:
            pulumi.set(__self__, "reject_duplicate_message", reject_duplicate_message)

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "dataset_id")

    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataset_id", value)

    @property
    @pulumi.getter(name="hl7V2StoreId")
    def hl7_v2_store_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HL7v2 store that is being created. The string must match the following regex: `[\\p{L}\\p{N}_\\-\\.]{1,256}`.
        """
        return pulumi.get(self, "hl7_v2_store_id")

    @hl7_v2_store_id.setter
    def hl7_v2_store_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hl7_v2_store_id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \\p{Ll}\\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

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
        Resource name of the HL7v2 store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> Optional[pulumi.Input['NotificationConfigArgs']]:
        """
        The notification destination all messages (both Ingest & Create) are published on. Only the message name is sent as part of the notification. If this is unset, no notifications are sent. Supplied by the client.
        """
        return pulumi.get(self, "notification_config")

    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input['NotificationConfigArgs']]):
        pulumi.set(self, "notification_config", value)

    @property
    @pulumi.getter(name="notificationConfigs")
    def notification_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['Hl7V2NotificationConfigArgs']]]]:
        """
        A list of notification configs. Each configuration uses a filter to determine whether to publish a message (both Ingest & Create) on the corresponding notification destination. Only the message name is sent as part of the notification. Supplied by the client.
        """
        return pulumi.get(self, "notification_configs")

    @notification_configs.setter
    def notification_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['Hl7V2NotificationConfigArgs']]]]):
        pulumi.set(self, "notification_configs", value)

    @property
    @pulumi.getter(name="parserConfig")
    def parser_config(self) -> Optional[pulumi.Input['ParserConfigArgs']]:
        """
        The configuration for the parser. It determines how the server parses the messages.
        """
        return pulumi.get(self, "parser_config")

    @parser_config.setter
    def parser_config(self, value: Optional[pulumi.Input['ParserConfigArgs']]):
        pulumi.set(self, "parser_config", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="rejectDuplicateMessage")
    def reject_duplicate_message(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines whether to reject duplicate messages. A duplicate message is a message with the same raw bytes as a message that has already been ingested/created in this HL7v2 store. The default value is false, meaning that the store accepts the duplicate messages and it also returns the same ACK message in the IngestMessageResponse as has been returned previously. Note that only one resource is created in the store. When this field is set to true, CreateMessage/IngestMessage requests with a duplicate message will be rejected by the store, and IngestMessageErrorDetail returns a NACK message upon rejection.
        """
        return pulumi.get(self, "reject_duplicate_message")

    @reject_duplicate_message.setter
    def reject_duplicate_message(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "reject_duplicate_message", value)


class Hl7V2Store(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 hl7_v2_store_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_config: Optional[pulumi.Input[pulumi.InputType['NotificationConfigArgs']]] = None,
                 notification_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Hl7V2NotificationConfigArgs']]]]] = None,
                 parser_config: Optional[pulumi.Input[pulumi.InputType['ParserConfigArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 reject_duplicate_message: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Creates a new HL7v2 store within the parent dataset.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hl7_v2_store_id: The ID of the HL7v2 store that is being created. The string must match the following regex: `[\\p{L}\\p{N}_\\-\\.]{1,256}`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \\p{Ll}\\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        :param pulumi.Input[str] name: Resource name of the HL7v2 store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}`.
        :param pulumi.Input[pulumi.InputType['NotificationConfigArgs']] notification_config: The notification destination all messages (both Ingest & Create) are published on. Only the message name is sent as part of the notification. If this is unset, no notifications are sent. Supplied by the client.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Hl7V2NotificationConfigArgs']]]] notification_configs: A list of notification configs. Each configuration uses a filter to determine whether to publish a message (both Ingest & Create) on the corresponding notification destination. Only the message name is sent as part of the notification. Supplied by the client.
        :param pulumi.Input[pulumi.InputType['ParserConfigArgs']] parser_config: The configuration for the parser. It determines how the server parses the messages.
        :param pulumi.Input[bool] reject_duplicate_message: Determines whether to reject duplicate messages. A duplicate message is a message with the same raw bytes as a message that has already been ingested/created in this HL7v2 store. The default value is false, meaning that the store accepts the duplicate messages and it also returns the same ACK message in the IngestMessageResponse as has been returned previously. Note that only one resource is created in the store. When this field is set to true, CreateMessage/IngestMessage requests with a duplicate message will be rejected by the store, and IngestMessageErrorDetail returns a NACK message upon rejection.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Hl7V2StoreArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new HL7v2 store within the parent dataset.

        :param str resource_name: The name of the resource.
        :param Hl7V2StoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(Hl7V2StoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 hl7_v2_store_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_config: Optional[pulumi.Input[pulumi.InputType['NotificationConfigArgs']]] = None,
                 notification_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Hl7V2NotificationConfigArgs']]]]] = None,
                 parser_config: Optional[pulumi.Input[pulumi.InputType['ParserConfigArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 reject_duplicate_message: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = Hl7V2StoreArgs.__new__(Hl7V2StoreArgs)

            if dataset_id is None and not opts.urn:
                raise TypeError("Missing required property 'dataset_id'")
            __props__.__dict__["dataset_id"] = dataset_id
            __props__.__dict__["hl7_v2_store_id"] = hl7_v2_store_id
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["notification_config"] = notification_config
            __props__.__dict__["notification_configs"] = notification_configs
            __props__.__dict__["parser_config"] = parser_config
            __props__.__dict__["project"] = project
            __props__.__dict__["reject_duplicate_message"] = reject_duplicate_message
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["dataset_id", "location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Hl7V2Store, __self__).__init__(
            'google-native:healthcare/v1beta1:Hl7V2Store',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Hl7V2Store':
        """
        Get an existing Hl7V2Store resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = Hl7V2StoreArgs.__new__(Hl7V2StoreArgs)

        __props__.__dict__["dataset_id"] = None
        __props__.__dict__["hl7_v2_store_id"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notification_config"] = None
        __props__.__dict__["notification_configs"] = None
        __props__.__dict__["parser_config"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["reject_duplicate_message"] = None
        return Hl7V2Store(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "dataset_id")

    @property
    @pulumi.getter(name="hl7V2StoreId")
    def hl7_v2_store_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the HL7v2 store that is being created. The string must match the following regex: `[\\p{L}\\p{N}_\\-\\.]{1,256}`.
        """
        return pulumi.get(self, "hl7_v2_store_id")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \\p{Ll}\\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of the HL7v2 store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> pulumi.Output['outputs.NotificationConfigResponse']:
        """
        The notification destination all messages (both Ingest & Create) are published on. Only the message name is sent as part of the notification. If this is unset, no notifications are sent. Supplied by the client.
        """
        return pulumi.get(self, "notification_config")

    @property
    @pulumi.getter(name="notificationConfigs")
    def notification_configs(self) -> pulumi.Output[Sequence['outputs.Hl7V2NotificationConfigResponse']]:
        """
        A list of notification configs. Each configuration uses a filter to determine whether to publish a message (both Ingest & Create) on the corresponding notification destination. Only the message name is sent as part of the notification. Supplied by the client.
        """
        return pulumi.get(self, "notification_configs")

    @property
    @pulumi.getter(name="parserConfig")
    def parser_config(self) -> pulumi.Output['outputs.ParserConfigResponse']:
        """
        The configuration for the parser. It determines how the server parses the messages.
        """
        return pulumi.get(self, "parser_config")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="rejectDuplicateMessage")
    def reject_duplicate_message(self) -> pulumi.Output[bool]:
        """
        Determines whether to reject duplicate messages. A duplicate message is a message with the same raw bytes as a message that has already been ingested/created in this HL7v2 store. The default value is false, meaning that the store accepts the duplicate messages and it also returns the same ACK message in the IngestMessageResponse as has been returned previously. Note that only one resource is created in the store. When this field is set to true, CreateMessage/IngestMessage requests with a duplicate message will be rejected by the store, and IngestMessageErrorDetail returns a NACK message upon rejection.
        """
        return pulumi.get(self, "reject_duplicate_message")

