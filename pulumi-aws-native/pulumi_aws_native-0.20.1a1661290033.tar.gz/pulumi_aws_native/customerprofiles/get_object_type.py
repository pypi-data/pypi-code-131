# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'GetObjectTypeResult',
    'AwaitableGetObjectTypeResult',
    'get_object_type',
    'get_object_type_output',
]

@pulumi.output_type
class GetObjectTypeResult:
    def __init__(__self__, allow_profile_creation=None, created_at=None, description=None, encryption_key=None, expiration_days=None, fields=None, keys=None, last_updated_at=None, tags=None, template_id=None):
        if allow_profile_creation and not isinstance(allow_profile_creation, bool):
            raise TypeError("Expected argument 'allow_profile_creation' to be a bool")
        pulumi.set(__self__, "allow_profile_creation", allow_profile_creation)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if encryption_key and not isinstance(encryption_key, str):
            raise TypeError("Expected argument 'encryption_key' to be a str")
        pulumi.set(__self__, "encryption_key", encryption_key)
        if expiration_days and not isinstance(expiration_days, int):
            raise TypeError("Expected argument 'expiration_days' to be a int")
        pulumi.set(__self__, "expiration_days", expiration_days)
        if fields and not isinstance(fields, list):
            raise TypeError("Expected argument 'fields' to be a list")
        pulumi.set(__self__, "fields", fields)
        if keys and not isinstance(keys, list):
            raise TypeError("Expected argument 'keys' to be a list")
        pulumi.set(__self__, "keys", keys)
        if last_updated_at and not isinstance(last_updated_at, str):
            raise TypeError("Expected argument 'last_updated_at' to be a str")
        pulumi.set(__self__, "last_updated_at", last_updated_at)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if template_id and not isinstance(template_id, str):
            raise TypeError("Expected argument 'template_id' to be a str")
        pulumi.set(__self__, "template_id", template_id)

    @property
    @pulumi.getter(name="allowProfileCreation")
    def allow_profile_creation(self) -> Optional[bool]:
        """
        Indicates whether a profile should be created when data is received.
        """
        return pulumi.get(self, "allow_profile_creation")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The time of this integration got created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the profile object type.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[str]:
        """
        The default encryption key
        """
        return pulumi.get(self, "encryption_key")

    @property
    @pulumi.getter(name="expirationDays")
    def expiration_days(self) -> Optional[int]:
        """
        The default number of days until the data within the domain expires.
        """
        return pulumi.get(self, "expiration_days")

    @property
    @pulumi.getter
    def fields(self) -> Optional[Sequence['outputs.ObjectTypeFieldMap']]:
        """
        A list of the name and ObjectType field.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def keys(self) -> Optional[Sequence['outputs.ObjectTypeKeyMap']]:
        """
        A list of unique keys that can be used to map data to the profile.
        """
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> Optional[str]:
        """
        The time of this integration got last updated at.
        """
        return pulumi.get(self, "last_updated_at")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ObjectTypeTag']]:
        """
        The tags (keys and values) associated with the integration.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[str]:
        """
        A unique identifier for the object template.
        """
        return pulumi.get(self, "template_id")


class AwaitableGetObjectTypeResult(GetObjectTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetObjectTypeResult(
            allow_profile_creation=self.allow_profile_creation,
            created_at=self.created_at,
            description=self.description,
            encryption_key=self.encryption_key,
            expiration_days=self.expiration_days,
            fields=self.fields,
            keys=self.keys,
            last_updated_at=self.last_updated_at,
            tags=self.tags,
            template_id=self.template_id)


def get_object_type(domain_name: Optional[str] = None,
                    object_type_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetObjectTypeResult:
    """
    An ObjectType resource of Amazon Connect Customer Profiles


    :param str domain_name: The unique name of the domain.
    :param str object_type_name: The name of the profile object type.
    """
    __args__ = dict()
    __args__['domainName'] = domain_name
    __args__['objectTypeName'] = object_type_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:customerprofiles:getObjectType', __args__, opts=opts, typ=GetObjectTypeResult).value

    return AwaitableGetObjectTypeResult(
        allow_profile_creation=__ret__.allow_profile_creation,
        created_at=__ret__.created_at,
        description=__ret__.description,
        encryption_key=__ret__.encryption_key,
        expiration_days=__ret__.expiration_days,
        fields=__ret__.fields,
        keys=__ret__.keys,
        last_updated_at=__ret__.last_updated_at,
        tags=__ret__.tags,
        template_id=__ret__.template_id)


@_utilities.lift_output_func(get_object_type)
def get_object_type_output(domain_name: Optional[pulumi.Input[str]] = None,
                           object_type_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetObjectTypeResult]:
    """
    An ObjectType resource of Amazon Connect Customer Profiles


    :param str domain_name: The unique name of the domain.
    :param str object_type_name: The name of the profile object type.
    """
    ...
