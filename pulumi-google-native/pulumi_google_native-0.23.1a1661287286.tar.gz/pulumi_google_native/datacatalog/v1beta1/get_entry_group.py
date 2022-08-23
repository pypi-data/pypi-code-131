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
    'GetEntryGroupResult',
    'AwaitableGetEntryGroupResult',
    'get_entry_group',
    'get_entry_group_output',
]

@pulumi.output_type
class GetEntryGroupResult:
    def __init__(__self__, data_catalog_timestamps=None, description=None, display_name=None, name=None):
        if data_catalog_timestamps and not isinstance(data_catalog_timestamps, dict):
            raise TypeError("Expected argument 'data_catalog_timestamps' to be a dict")
        pulumi.set(__self__, "data_catalog_timestamps", data_catalog_timestamps)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="dataCatalogTimestamps")
    def data_catalog_timestamps(self) -> 'outputs.GoogleCloudDatacatalogV1beta1SystemTimestampsResponse':
        """
        Timestamps about this EntryGroup. Default value is empty timestamps.
        """
        return pulumi.get(self, "data_catalog_timestamps")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Entry group description, which can consist of several sentences or paragraphs that describe entry group contents. Default value is an empty string.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A short name to identify the entry group, for example, "analytics data - jan 2011". Default value is an empty string.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the entry group in URL format. Example: * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id} Note that this EntryGroup and its child resources may not actually be stored in the location in this name.
        """
        return pulumi.get(self, "name")


class AwaitableGetEntryGroupResult(GetEntryGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEntryGroupResult(
            data_catalog_timestamps=self.data_catalog_timestamps,
            description=self.description,
            display_name=self.display_name,
            name=self.name)


def get_entry_group(entry_group_id: Optional[str] = None,
                    location: Optional[str] = None,
                    project: Optional[str] = None,
                    read_mask: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEntryGroupResult:
    """
    Gets an EntryGroup.
    """
    __args__ = dict()
    __args__['entryGroupId'] = entry_group_id
    __args__['location'] = location
    __args__['project'] = project
    __args__['readMask'] = read_mask
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:datacatalog/v1beta1:getEntryGroup', __args__, opts=opts, typ=GetEntryGroupResult).value

    return AwaitableGetEntryGroupResult(
        data_catalog_timestamps=__ret__.data_catalog_timestamps,
        description=__ret__.description,
        display_name=__ret__.display_name,
        name=__ret__.name)


@_utilities.lift_output_func(get_entry_group)
def get_entry_group_output(entry_group_id: Optional[pulumi.Input[str]] = None,
                           location: Optional[pulumi.Input[str]] = None,
                           project: Optional[pulumi.Input[Optional[str]]] = None,
                           read_mask: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEntryGroupResult]:
    """
    Gets an EntryGroup.
    """
    ...
