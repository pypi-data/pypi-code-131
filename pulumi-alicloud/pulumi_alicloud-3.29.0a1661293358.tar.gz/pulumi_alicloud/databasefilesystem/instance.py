# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 instance_name: pulumi.Input[str],
                 size: pulumi.Input[int],
                 zone_id: pulumi.Input[str],
                 category: Optional[pulumi.Input[str]] = None,
                 delete_snapshot: Optional[pulumi.Input[bool]] = None,
                 ecs_lists: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceEcsListArgs']]]] = None,
                 enable_raid: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input[bool]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 performance_level: Optional[pulumi.Input[str]] = None,
                 raid_stripe_unit_number: Optional[pulumi.Input[str]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input[str] instance_name: The name of the Database file system.
        :param pulumi.Input[int] size: The size Of the Database file system. Unit: GiB.
        :param pulumi.Input[str] zone_id: The Zone ID of the Database file system.
        :param pulumi.Input[str] category: The type of the Database file system. Valid values: `standard`.
        :param pulumi.Input[bool] delete_snapshot: Whether to delete the original snapshot after the DBFS is created using the snapshot. Valid values : `true` anf `false`.
        :param pulumi.Input[Sequence[pulumi.Input['InstanceEcsListArgs']]] ecs_lists: The collection of ECS instances mounted to the Database file system. See the following `Block ecs_list`. **NOTE:** Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.
        :param pulumi.Input[bool] enable_raid: Whether to create the Database file system in RAID way. Valid values : `true` anf `false`.
        :param pulumi.Input[bool] encryption: Whether to encrypt the database file system. Valid values: `true` and `false`.
        :param pulumi.Input[str] kms_key_id: The KMS key ID of the Database file system used. This parameter is valid When `encryption` parameter is set to `true`.
        :param pulumi.Input[str] performance_level: The performance level of the Database file system. Valid values: `PL0`, `PL1`, `PL2`, `PL3`.
        :param pulumi.Input[str] raid_stripe_unit_number: The number of strip. This parameter is valid When `enable_raid` parameter is set to `true`.
        :param pulumi.Input[str] snapshot_id: The snapshot id of the Database file system.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        """
        pulumi.set(__self__, "instance_name", instance_name)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "zone_id", zone_id)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if delete_snapshot is not None:
            pulumi.set(__self__, "delete_snapshot", delete_snapshot)
        if ecs_lists is not None:
            warnings.warn("""Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.""", DeprecationWarning)
            pulumi.log.warn("""ecs_lists is deprecated: Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.""")
        if ecs_lists is not None:
            pulumi.set(__self__, "ecs_lists", ecs_lists)
        if enable_raid is not None:
            pulumi.set(__self__, "enable_raid", enable_raid)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if performance_level is not None:
            pulumi.set(__self__, "performance_level", performance_level)
        if raid_stripe_unit_number is not None:
            pulumi.set(__self__, "raid_stripe_unit_number", raid_stripe_unit_number)
        if snapshot_id is not None:
            pulumi.set(__self__, "snapshot_id", snapshot_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Input[str]:
        """
        The name of the Database file system.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[int]:
        """
        The size Of the Database file system. Unit: GiB.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[int]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        The Zone ID of the Database file system.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the Database file system. Valid values: `standard`.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter(name="deleteSnapshot")
    def delete_snapshot(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to delete the original snapshot after the DBFS is created using the snapshot. Valid values : `true` anf `false`.
        """
        return pulumi.get(self, "delete_snapshot")

    @delete_snapshot.setter
    def delete_snapshot(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_snapshot", value)

    @property
    @pulumi.getter(name="ecsLists")
    def ecs_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceEcsListArgs']]]]:
        """
        The collection of ECS instances mounted to the Database file system. See the following `Block ecs_list`. **NOTE:** Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.
        """
        return pulumi.get(self, "ecs_lists")

    @ecs_lists.setter
    def ecs_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceEcsListArgs']]]]):
        pulumi.set(self, "ecs_lists", value)

    @property
    @pulumi.getter(name="enableRaid")
    def enable_raid(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to create the Database file system in RAID way. Valid values : `true` anf `false`.
        """
        return pulumi.get(self, "enable_raid")

    @enable_raid.setter
    def enable_raid(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_raid", value)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to encrypt the database file system. Valid values: `true` and `false`.
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The KMS key ID of the Database file system used. This parameter is valid When `encryption` parameter is set to `true`.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="performanceLevel")
    def performance_level(self) -> Optional[pulumi.Input[str]]:
        """
        The performance level of the Database file system. Valid values: `PL0`, `PL1`, `PL2`, `PL3`.
        """
        return pulumi.get(self, "performance_level")

    @performance_level.setter
    def performance_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "performance_level", value)

    @property
    @pulumi.getter(name="raidStripeUnitNumber")
    def raid_stripe_unit_number(self) -> Optional[pulumi.Input[str]]:
        """
        The number of strip. This parameter is valid When `enable_raid` parameter is set to `true`.
        """
        return pulumi.get(self, "raid_stripe_unit_number")

    @raid_stripe_unit_number.setter
    def raid_stripe_unit_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "raid_stripe_unit_number", value)

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[str]]:
        """
        The snapshot id of the Database file system.
        """
        return pulumi.get(self, "snapshot_id")

    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *,
                 category: Optional[pulumi.Input[str]] = None,
                 delete_snapshot: Optional[pulumi.Input[bool]] = None,
                 ecs_lists: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceEcsListArgs']]]] = None,
                 enable_raid: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 performance_level: Optional[pulumi.Input[str]] = None,
                 raid_stripe_unit_number: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Instance resources.
        :param pulumi.Input[str] category: The type of the Database file system. Valid values: `standard`.
        :param pulumi.Input[bool] delete_snapshot: Whether to delete the original snapshot after the DBFS is created using the snapshot. Valid values : `true` anf `false`.
        :param pulumi.Input[Sequence[pulumi.Input['InstanceEcsListArgs']]] ecs_lists: The collection of ECS instances mounted to the Database file system. See the following `Block ecs_list`. **NOTE:** Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.
        :param pulumi.Input[bool] enable_raid: Whether to create the Database file system in RAID way. Valid values : `true` anf `false`.
        :param pulumi.Input[bool] encryption: Whether to encrypt the database file system. Valid values: `true` and `false`.
        :param pulumi.Input[str] instance_name: The name of the Database file system.
        :param pulumi.Input[str] kms_key_id: The KMS key ID of the Database file system used. This parameter is valid When `encryption` parameter is set to `true`.
        :param pulumi.Input[str] performance_level: The performance level of the Database file system. Valid values: `PL0`, `PL1`, `PL2`, `PL3`.
        :param pulumi.Input[str] raid_stripe_unit_number: The number of strip. This parameter is valid When `enable_raid` parameter is set to `true`.
        :param pulumi.Input[int] size: The size Of the Database file system. Unit: GiB.
        :param pulumi.Input[str] snapshot_id: The snapshot id of the Database file system.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zone_id: The Zone ID of the Database file system.
        """
        if category is not None:
            pulumi.set(__self__, "category", category)
        if delete_snapshot is not None:
            pulumi.set(__self__, "delete_snapshot", delete_snapshot)
        if ecs_lists is not None:
            warnings.warn("""Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.""", DeprecationWarning)
            pulumi.log.warn("""ecs_lists is deprecated: Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.""")
        if ecs_lists is not None:
            pulumi.set(__self__, "ecs_lists", ecs_lists)
        if enable_raid is not None:
            pulumi.set(__self__, "enable_raid", enable_raid)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if instance_name is not None:
            pulumi.set(__self__, "instance_name", instance_name)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if performance_level is not None:
            pulumi.set(__self__, "performance_level", performance_level)
        if raid_stripe_unit_number is not None:
            pulumi.set(__self__, "raid_stripe_unit_number", raid_stripe_unit_number)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if snapshot_id is not None:
            pulumi.set(__self__, "snapshot_id", snapshot_id)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the Database file system. Valid values: `standard`.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter(name="deleteSnapshot")
    def delete_snapshot(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to delete the original snapshot after the DBFS is created using the snapshot. Valid values : `true` anf `false`.
        """
        return pulumi.get(self, "delete_snapshot")

    @delete_snapshot.setter
    def delete_snapshot(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_snapshot", value)

    @property
    @pulumi.getter(name="ecsLists")
    def ecs_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceEcsListArgs']]]]:
        """
        The collection of ECS instances mounted to the Database file system. See the following `Block ecs_list`. **NOTE:** Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.
        """
        return pulumi.get(self, "ecs_lists")

    @ecs_lists.setter
    def ecs_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceEcsListArgs']]]]):
        pulumi.set(self, "ecs_lists", value)

    @property
    @pulumi.getter(name="enableRaid")
    def enable_raid(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to create the Database file system in RAID way. Valid values : `true` anf `false`.
        """
        return pulumi.get(self, "enable_raid")

    @enable_raid.setter
    def enable_raid(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_raid", value)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to encrypt the database file system. Valid values: `true` and `false`.
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Database file system.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The KMS key ID of the Database file system used. This parameter is valid When `encryption` parameter is set to `true`.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="performanceLevel")
    def performance_level(self) -> Optional[pulumi.Input[str]]:
        """
        The performance level of the Database file system. Valid values: `PL0`, `PL1`, `PL2`, `PL3`.
        """
        return pulumi.get(self, "performance_level")

    @performance_level.setter
    def performance_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "performance_level", value)

    @property
    @pulumi.getter(name="raidStripeUnitNumber")
    def raid_stripe_unit_number(self) -> Optional[pulumi.Input[str]]:
        """
        The number of strip. This parameter is valid When `enable_raid` parameter is set to `true`.
        """
        return pulumi.get(self, "raid_stripe_unit_number")

    @raid_stripe_unit_number.setter
    def raid_stripe_unit_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "raid_stripe_unit_number", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        The size Of the Database file system. Unit: GiB.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[str]]:
        """
        The snapshot id of the Database file system.
        """
        return pulumi.get(self, "snapshot_id")

    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Zone ID of the Database file system.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 delete_snapshot: Optional[pulumi.Input[bool]] = None,
                 ecs_lists: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEcsListArgs']]]]] = None,
                 enable_raid: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 performance_level: Optional[pulumi.Input[str]] = None,
                 raid_stripe_unit_number: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a DBFS Instance resource.

        For information about DBFS Instance and how to use it, see [What is Instance](https://help.aliyun.com/document_detail/149726.html).

        > **NOTE:** Available in v1.136.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.databasefilesystem.Instance("example",
            category="standard",
            instance_name="example_value",
            size=1,
            zone_id="example_value")
        ```

        ## Import

        DBFS Instance can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:databasefilesystem/instance:Instance example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category: The type of the Database file system. Valid values: `standard`.
        :param pulumi.Input[bool] delete_snapshot: Whether to delete the original snapshot after the DBFS is created using the snapshot. Valid values : `true` anf `false`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEcsListArgs']]]] ecs_lists: The collection of ECS instances mounted to the Database file system. See the following `Block ecs_list`. **NOTE:** Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.
        :param pulumi.Input[bool] enable_raid: Whether to create the Database file system in RAID way. Valid values : `true` anf `false`.
        :param pulumi.Input[bool] encryption: Whether to encrypt the database file system. Valid values: `true` and `false`.
        :param pulumi.Input[str] instance_name: The name of the Database file system.
        :param pulumi.Input[str] kms_key_id: The KMS key ID of the Database file system used. This parameter is valid When `encryption` parameter is set to `true`.
        :param pulumi.Input[str] performance_level: The performance level of the Database file system. Valid values: `PL0`, `PL1`, `PL2`, `PL3`.
        :param pulumi.Input[str] raid_stripe_unit_number: The number of strip. This parameter is valid When `enable_raid` parameter is set to `true`.
        :param pulumi.Input[int] size: The size Of the Database file system. Unit: GiB.
        :param pulumi.Input[str] snapshot_id: The snapshot id of the Database file system.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zone_id: The Zone ID of the Database file system.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DBFS Instance resource.

        For information about DBFS Instance and how to use it, see [What is Instance](https://help.aliyun.com/document_detail/149726.html).

        > **NOTE:** Available in v1.136.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.databasefilesystem.Instance("example",
            category="standard",
            instance_name="example_value",
            size=1,
            zone_id="example_value")
        ```

        ## Import

        DBFS Instance can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:databasefilesystem/instance:Instance example <id>
        ```

        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 delete_snapshot: Optional[pulumi.Input[bool]] = None,
                 ecs_lists: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEcsListArgs']]]]] = None,
                 enable_raid: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 performance_level: Optional[pulumi.Input[str]] = None,
                 raid_stripe_unit_number: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceArgs.__new__(InstanceArgs)

            __props__.__dict__["category"] = category
            __props__.__dict__["delete_snapshot"] = delete_snapshot
            if ecs_lists is not None and not opts.urn:
                warnings.warn("""Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.""", DeprecationWarning)
                pulumi.log.warn("""ecs_lists is deprecated: Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.""")
            __props__.__dict__["ecs_lists"] = ecs_lists
            __props__.__dict__["enable_raid"] = enable_raid
            __props__.__dict__["encryption"] = encryption
            if instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'instance_name'")
            __props__.__dict__["instance_name"] = instance_name
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["performance_level"] = performance_level
            __props__.__dict__["raid_stripe_unit_number"] = raid_stripe_unit_number
            if size is None and not opts.urn:
                raise TypeError("Missing required property 'size'")
            __props__.__dict__["size"] = size
            __props__.__dict__["snapshot_id"] = snapshot_id
            __props__.__dict__["tags"] = tags
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
            __props__.__dict__["status"] = None
        super(Instance, __self__).__init__(
            'alicloud:databasefilesystem/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            category: Optional[pulumi.Input[str]] = None,
            delete_snapshot: Optional[pulumi.Input[bool]] = None,
            ecs_lists: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEcsListArgs']]]]] = None,
            enable_raid: Optional[pulumi.Input[bool]] = None,
            encryption: Optional[pulumi.Input[bool]] = None,
            instance_name: Optional[pulumi.Input[str]] = None,
            kms_key_id: Optional[pulumi.Input[str]] = None,
            performance_level: Optional[pulumi.Input[str]] = None,
            raid_stripe_unit_number: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            snapshot_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category: The type of the Database file system. Valid values: `standard`.
        :param pulumi.Input[bool] delete_snapshot: Whether to delete the original snapshot after the DBFS is created using the snapshot. Valid values : `true` anf `false`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEcsListArgs']]]] ecs_lists: The collection of ECS instances mounted to the Database file system. See the following `Block ecs_list`. **NOTE:** Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.
        :param pulumi.Input[bool] enable_raid: Whether to create the Database file system in RAID way. Valid values : `true` anf `false`.
        :param pulumi.Input[bool] encryption: Whether to encrypt the database file system. Valid values: `true` and `false`.
        :param pulumi.Input[str] instance_name: The name of the Database file system.
        :param pulumi.Input[str] kms_key_id: The KMS key ID of the Database file system used. This parameter is valid When `encryption` parameter is set to `true`.
        :param pulumi.Input[str] performance_level: The performance level of the Database file system. Valid values: `PL0`, `PL1`, `PL2`, `PL3`.
        :param pulumi.Input[str] raid_stripe_unit_number: The number of strip. This parameter is valid When `enable_raid` parameter is set to `true`.
        :param pulumi.Input[int] size: The size Of the Database file system. Unit: GiB.
        :param pulumi.Input[str] snapshot_id: The snapshot id of the Database file system.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zone_id: The Zone ID of the Database file system.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceState.__new__(_InstanceState)

        __props__.__dict__["category"] = category
        __props__.__dict__["delete_snapshot"] = delete_snapshot
        __props__.__dict__["ecs_lists"] = ecs_lists
        __props__.__dict__["enable_raid"] = enable_raid
        __props__.__dict__["encryption"] = encryption
        __props__.__dict__["instance_name"] = instance_name
        __props__.__dict__["kms_key_id"] = kms_key_id
        __props__.__dict__["performance_level"] = performance_level
        __props__.__dict__["raid_stripe_unit_number"] = raid_stripe_unit_number
        __props__.__dict__["size"] = size
        __props__.__dict__["snapshot_id"] = snapshot_id
        __props__.__dict__["status"] = status
        __props__.__dict__["tags"] = tags
        __props__.__dict__["zone_id"] = zone_id
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[str]:
        """
        The type of the Database file system. Valid values: `standard`.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="deleteSnapshot")
    def delete_snapshot(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to delete the original snapshot after the DBFS is created using the snapshot. Valid values : `true` anf `false`.
        """
        return pulumi.get(self, "delete_snapshot")

    @property
    @pulumi.getter(name="ecsLists")
    def ecs_lists(self) -> pulumi.Output[Optional[Sequence['outputs.InstanceEcsList']]]:
        """
        The collection of ECS instances mounted to the Database file system. See the following `Block ecs_list`. **NOTE:** Field 'ecs_list' has been deprecated from provider version 1.156.0 and it will be removed in the future version. Please use the new resource 'alicloud_dbfs_instance_attachment' to attach ECS and DBFS.
        """
        return pulumi.get(self, "ecs_lists")

    @property
    @pulumi.getter(name="enableRaid")
    def enable_raid(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to create the Database file system in RAID way. Valid values : `true` anf `false`.
        """
        return pulumi.get(self, "enable_raid")

    @property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to encrypt the database file system. Valid values: `true` and `false`.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[str]:
        """
        The name of the Database file system.
        """
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        The KMS key ID of the Database file system used. This parameter is valid When `encryption` parameter is set to `true`.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="performanceLevel")
    def performance_level(self) -> pulumi.Output[str]:
        """
        The performance level of the Database file system. Valid values: `PL0`, `PL1`, `PL2`, `PL3`.
        """
        return pulumi.get(self, "performance_level")

    @property
    @pulumi.getter(name="raidStripeUnitNumber")
    def raid_stripe_unit_number(self) -> pulumi.Output[Optional[str]]:
        """
        The number of strip. This parameter is valid When `enable_raid` parameter is set to `true`.
        """
        return pulumi.get(self, "raid_stripe_unit_number")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        The size Of the Database file system. Unit: GiB.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> pulumi.Output[Optional[str]]:
        """
        The snapshot id of the Database file system.
        """
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The Zone ID of the Database file system.
        """
        return pulumi.get(self, "zone_id")

