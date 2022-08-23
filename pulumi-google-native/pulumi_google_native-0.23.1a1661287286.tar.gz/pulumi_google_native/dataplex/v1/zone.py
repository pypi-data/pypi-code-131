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

__all__ = ['ZoneArgs', 'Zone']

@pulumi.input_type
class ZoneArgs:
    def __init__(__self__, *,
                 lake_id: pulumi.Input[str],
                 resource_spec: pulumi.Input['GoogleCloudDataplexV1ZoneResourceSpecArgs'],
                 type: pulumi.Input['ZoneType'],
                 zone_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 discovery_spec: Optional[pulumi.Input['GoogleCloudDataplexV1ZoneDiscoverySpecArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 validate_only: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Zone resource.
        :param pulumi.Input['GoogleCloudDataplexV1ZoneResourceSpecArgs'] resource_spec: Specification of the resources that are referenced by the assets within this zone.
        :param pulumi.Input['ZoneType'] type: Immutable. The type of the zone.
        :param pulumi.Input[str] zone_id: Required. Zone identifier. This ID will be used to generate names such as database and dataset names when publishing metadata to Hive Metastore and BigQuery. * Must contain only lowercase letters, numbers and hyphens. * Must start with a letter. * Must end with a number or a letter. * Must be between 1-63 characters. * Must be unique across all lakes from all locations in a project. * Must not be one of the reserved IDs (i.e. "default", "global-temp")
        :param pulumi.Input[str] description: Optional. Description of the zone.
        :param pulumi.Input['GoogleCloudDataplexV1ZoneDiscoverySpecArgs'] discovery_spec: Optional. Specification of the discovery feature applied to data in this zone.
        :param pulumi.Input[str] display_name: Optional. User friendly display name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. User defined labels for the zone.
        :param pulumi.Input[bool] validate_only: Optional. Only validate the request, but do not perform mutations. The default is false.
        """
        pulumi.set(__self__, "lake_id", lake_id)
        pulumi.set(__self__, "resource_spec", resource_spec)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "zone_id", zone_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if discovery_spec is not None:
            pulumi.set(__self__, "discovery_spec", discovery_spec)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if validate_only is not None:
            pulumi.set(__self__, "validate_only", validate_only)

    @property
    @pulumi.getter(name="lakeId")
    def lake_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "lake_id")

    @lake_id.setter
    def lake_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "lake_id", value)

    @property
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> pulumi.Input['GoogleCloudDataplexV1ZoneResourceSpecArgs']:
        """
        Specification of the resources that are referenced by the assets within this zone.
        """
        return pulumi.get(self, "resource_spec")

    @resource_spec.setter
    def resource_spec(self, value: pulumi.Input['GoogleCloudDataplexV1ZoneResourceSpecArgs']):
        pulumi.set(self, "resource_spec", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['ZoneType']:
        """
        Immutable. The type of the zone.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['ZoneType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        Required. Zone identifier. This ID will be used to generate names such as database and dataset names when publishing metadata to Hive Metastore and BigQuery. * Must contain only lowercase letters, numbers and hyphens. * Must start with a letter. * Must end with a number or a letter. * Must be between 1-63 characters. * Must be unique across all lakes from all locations in a project. * Must not be one of the reserved IDs (i.e. "default", "global-temp")
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Description of the zone.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="discoverySpec")
    def discovery_spec(self) -> Optional[pulumi.Input['GoogleCloudDataplexV1ZoneDiscoverySpecArgs']]:
        """
        Optional. Specification of the discovery feature applied to data in this zone.
        """
        return pulumi.get(self, "discovery_spec")

    @discovery_spec.setter
    def discovery_spec(self, value: Optional[pulumi.Input['GoogleCloudDataplexV1ZoneDiscoverySpecArgs']]):
        pulumi.set(self, "discovery_spec", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. User friendly display name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. User defined labels for the zone.
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
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="validateOnly")
    def validate_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional. Only validate the request, but do not perform mutations. The default is false.
        """
        return pulumi.get(self, "validate_only")

    @validate_only.setter
    def validate_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "validate_only", value)


class Zone(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 discovery_spec: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1ZoneDiscoverySpecArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 lake_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 resource_spec: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1ZoneResourceSpecArgs']]] = None,
                 type: Optional[pulumi.Input['ZoneType']] = None,
                 validate_only: Optional[pulumi.Input[bool]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a zone resource within a lake.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Optional. Description of the zone.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1ZoneDiscoverySpecArgs']] discovery_spec: Optional. Specification of the discovery feature applied to data in this zone.
        :param pulumi.Input[str] display_name: Optional. User friendly display name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. User defined labels for the zone.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1ZoneResourceSpecArgs']] resource_spec: Specification of the resources that are referenced by the assets within this zone.
        :param pulumi.Input['ZoneType'] type: Immutable. The type of the zone.
        :param pulumi.Input[bool] validate_only: Optional. Only validate the request, but do not perform mutations. The default is false.
        :param pulumi.Input[str] zone_id: Required. Zone identifier. This ID will be used to generate names such as database and dataset names when publishing metadata to Hive Metastore and BigQuery. * Must contain only lowercase letters, numbers and hyphens. * Must start with a letter. * Must end with a number or a letter. * Must be between 1-63 characters. * Must be unique across all lakes from all locations in a project. * Must not be one of the reserved IDs (i.e. "default", "global-temp")
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZoneArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a zone resource within a lake.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param ZoneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZoneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 discovery_spec: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1ZoneDiscoverySpecArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 lake_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 resource_spec: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1ZoneResourceSpecArgs']]] = None,
                 type: Optional[pulumi.Input['ZoneType']] = None,
                 validate_only: Optional[pulumi.Input[bool]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZoneArgs.__new__(ZoneArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["discovery_spec"] = discovery_spec
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["labels"] = labels
            if lake_id is None and not opts.urn:
                raise TypeError("Missing required property 'lake_id'")
            __props__.__dict__["lake_id"] = lake_id
            __props__.__dict__["location"] = location
            __props__.__dict__["project"] = project
            if resource_spec is None and not opts.urn:
                raise TypeError("Missing required property 'resource_spec'")
            __props__.__dict__["resource_spec"] = resource_spec
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["validate_only"] = validate_only
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
            __props__.__dict__["asset_status"] = None
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["uid"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["lake_id", "location", "project", "zone_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Zone, __self__).__init__(
            'google-native:dataplex/v1:Zone',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Zone':
        """
        Get an existing Zone resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ZoneArgs.__new__(ZoneArgs)

        __props__.__dict__["asset_status"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["discovery_spec"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["lake_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["resource_spec"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uid"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["validate_only"] = None
        __props__.__dict__["zone_id"] = None
        return Zone(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assetStatus")
    def asset_status(self) -> pulumi.Output['outputs.GoogleCloudDataplexV1AssetStatusResponse']:
        """
        Aggregated status of the underlying assets of the zone.
        """
        return pulumi.get(self, "asset_status")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the zone was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. Description of the zone.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="discoverySpec")
    def discovery_spec(self) -> pulumi.Output['outputs.GoogleCloudDataplexV1ZoneDiscoverySpecResponse']:
        """
        Optional. Specification of the discovery feature applied to data in this zone.
        """
        return pulumi.get(self, "discovery_spec")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Optional. User friendly display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. User defined labels for the zone.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="lakeId")
    def lake_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "lake_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The relative resource name of the zone, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> pulumi.Output['outputs.GoogleCloudDataplexV1ZoneResourceSpecResponse']:
        """
        Specification of the resources that are referenced by the assets within this zone.
        """
        return pulumi.get(self, "resource_spec")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Current state of the zone.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Immutable. The type of the zone.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        System generated globally unique ID for the zone. This ID will be different if the zone is deleted and re-created with the same name.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time when the zone was last updated.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="validateOnly")
    def validate_only(self) -> pulumi.Output[Optional[bool]]:
        """
        Optional. Only validate the request, but do not perform mutations. The default is false.
        """
        return pulumi.get(self, "validate_only")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        Required. Zone identifier. This ID will be used to generate names such as database and dataset names when publishing metadata to Hive Metastore and BigQuery. * Must contain only lowercase letters, numbers and hyphens. * Must start with a letter. * Must end with a number or a letter. * Must be between 1-63 characters. * Must be unique across all lakes from all locations in a project. * Must not be one of the reserved IDs (i.e. "default", "global-temp")
        """
        return pulumi.get(self, "zone_id")

