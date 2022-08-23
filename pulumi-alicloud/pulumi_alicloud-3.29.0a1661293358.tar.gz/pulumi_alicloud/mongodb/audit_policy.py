# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AuditPolicyArgs', 'AuditPolicy']

@pulumi.input_type
class AuditPolicyArgs:
    def __init__(__self__, *,
                 audit_status: pulumi.Input[str],
                 db_instance_id: pulumi.Input[str],
                 storage_period: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a AuditPolicy resource.
        :param pulumi.Input[str] audit_status: The status of the audit log. Valid values: `disabled`, `enable`.
        :param pulumi.Input[str] db_instance_id: The ID of the instance.
        :param pulumi.Input[int] storage_period: The retention period of audit logs. Valid values: `1` to `30`. Default value: `30`.
        """
        pulumi.set(__self__, "audit_status", audit_status)
        pulumi.set(__self__, "db_instance_id", db_instance_id)
        if storage_period is not None:
            pulumi.set(__self__, "storage_period", storage_period)

    @property
    @pulumi.getter(name="auditStatus")
    def audit_status(self) -> pulumi.Input[str]:
        """
        The status of the audit log. Valid values: `disabled`, `enable`.
        """
        return pulumi.get(self, "audit_status")

    @audit_status.setter
    def audit_status(self, value: pulumi.Input[str]):
        pulumi.set(self, "audit_status", value)

    @property
    @pulumi.getter(name="dbInstanceId")
    def db_instance_id(self) -> pulumi.Input[str]:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "db_instance_id")

    @db_instance_id.setter
    def db_instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "db_instance_id", value)

    @property
    @pulumi.getter(name="storagePeriod")
    def storage_period(self) -> Optional[pulumi.Input[int]]:
        """
        The retention period of audit logs. Valid values: `1` to `30`. Default value: `30`.
        """
        return pulumi.get(self, "storage_period")

    @storage_period.setter
    def storage_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage_period", value)


@pulumi.input_type
class _AuditPolicyState:
    def __init__(__self__, *,
                 audit_status: Optional[pulumi.Input[str]] = None,
                 db_instance_id: Optional[pulumi.Input[str]] = None,
                 storage_period: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering AuditPolicy resources.
        :param pulumi.Input[str] audit_status: The status of the audit log. Valid values: `disabled`, `enable`.
        :param pulumi.Input[str] db_instance_id: The ID of the instance.
        :param pulumi.Input[int] storage_period: The retention period of audit logs. Valid values: `1` to `30`. Default value: `30`.
        """
        if audit_status is not None:
            pulumi.set(__self__, "audit_status", audit_status)
        if db_instance_id is not None:
            pulumi.set(__self__, "db_instance_id", db_instance_id)
        if storage_period is not None:
            pulumi.set(__self__, "storage_period", storage_period)

    @property
    @pulumi.getter(name="auditStatus")
    def audit_status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the audit log. Valid values: `disabled`, `enable`.
        """
        return pulumi.get(self, "audit_status")

    @audit_status.setter
    def audit_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "audit_status", value)

    @property
    @pulumi.getter(name="dbInstanceId")
    def db_instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "db_instance_id")

    @db_instance_id.setter
    def db_instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_instance_id", value)

    @property
    @pulumi.getter(name="storagePeriod")
    def storage_period(self) -> Optional[pulumi.Input[int]]:
        """
        The retention period of audit logs. Valid values: `1` to `30`. Default value: `30`.
        """
        return pulumi.get(self, "storage_period")

    @storage_period.setter
    def storage_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage_period", value)


class AuditPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_status: Optional[pulumi.Input[str]] = None,
                 db_instance_id: Optional[pulumi.Input[str]] = None,
                 storage_period: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides a MongoDB Audit Policy resource.

        For information about MongoDB Audit Policy and how to use it, see [What is Audit Policy](https://www.alibabacloud.com/help/doc-detail/131941.html).

        > **NOTE:** Available in v1.148.0+.

        ## Import

        MongoDB Audit Policy can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:mongodb/auditPolicy:AuditPolicy example <db_instance_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] audit_status: The status of the audit log. Valid values: `disabled`, `enable`.
        :param pulumi.Input[str] db_instance_id: The ID of the instance.
        :param pulumi.Input[int] storage_period: The retention period of audit logs. Valid values: `1` to `30`. Default value: `30`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AuditPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a MongoDB Audit Policy resource.

        For information about MongoDB Audit Policy and how to use it, see [What is Audit Policy](https://www.alibabacloud.com/help/doc-detail/131941.html).

        > **NOTE:** Available in v1.148.0+.

        ## Import

        MongoDB Audit Policy can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:mongodb/auditPolicy:AuditPolicy example <db_instance_id>
        ```

        :param str resource_name: The name of the resource.
        :param AuditPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuditPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_status: Optional[pulumi.Input[str]] = None,
                 db_instance_id: Optional[pulumi.Input[str]] = None,
                 storage_period: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AuditPolicyArgs.__new__(AuditPolicyArgs)

            if audit_status is None and not opts.urn:
                raise TypeError("Missing required property 'audit_status'")
            __props__.__dict__["audit_status"] = audit_status
            if db_instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'db_instance_id'")
            __props__.__dict__["db_instance_id"] = db_instance_id
            __props__.__dict__["storage_period"] = storage_period
        super(AuditPolicy, __self__).__init__(
            'alicloud:mongodb/auditPolicy:AuditPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            audit_status: Optional[pulumi.Input[str]] = None,
            db_instance_id: Optional[pulumi.Input[str]] = None,
            storage_period: Optional[pulumi.Input[int]] = None) -> 'AuditPolicy':
        """
        Get an existing AuditPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] audit_status: The status of the audit log. Valid values: `disabled`, `enable`.
        :param pulumi.Input[str] db_instance_id: The ID of the instance.
        :param pulumi.Input[int] storage_period: The retention period of audit logs. Valid values: `1` to `30`. Default value: `30`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AuditPolicyState.__new__(_AuditPolicyState)

        __props__.__dict__["audit_status"] = audit_status
        __props__.__dict__["db_instance_id"] = db_instance_id
        __props__.__dict__["storage_period"] = storage_period
        return AuditPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="auditStatus")
    def audit_status(self) -> pulumi.Output[str]:
        """
        The status of the audit log. Valid values: `disabled`, `enable`.
        """
        return pulumi.get(self, "audit_status")

    @property
    @pulumi.getter(name="dbInstanceId")
    def db_instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "db_instance_id")

    @property
    @pulumi.getter(name="storagePeriod")
    def storage_period(self) -> pulumi.Output[Optional[int]]:
        """
        The retention period of audit logs. Valid values: `1` to `30`. Default value: `30`.
        """
        return pulumi.get(self, "storage_period")

