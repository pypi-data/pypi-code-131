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

__all__ = ['DatabaseArgs', 'Database']

@pulumi.input_type
class DatabaseArgs:
    def __init__(__self__, *,
                 create_statement: pulumi.Input[str],
                 instance_id: pulumi.Input[str],
                 database_dialect: Optional[pulumi.Input['DatabaseDatabaseDialect']] = None,
                 encryption_config: Optional[pulumi.Input['EncryptionConfigArgs']] = None,
                 extra_statements: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Database resource.
        :param pulumi.Input[str] create_statement: A `CREATE DATABASE` statement, which specifies the ID of the new database. The database ID must conform to the regular expression `a-z*[a-z0-9]` and be between 2 and 30 characters in length. If the database ID is a reserved word or if it contains a hyphen, the database ID must be enclosed in backticks (`` ` ``).
        :param pulumi.Input['DatabaseDatabaseDialect'] database_dialect: Optional. The dialect of the Cloud Spanner Database.
        :param pulumi.Input['EncryptionConfigArgs'] encryption_config: Optional. The encryption configuration for the database. If this field is not specified, Cloud Spanner will encrypt/decrypt all data at rest using Google default encryption.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] extra_statements: Optional. A list of DDL statements to run inside the newly created database. Statements can create tables, indexes, etc. These statements execute atomically with the creation of the database: if there is an error in any statement, the database is not created.
        """
        pulumi.set(__self__, "create_statement", create_statement)
        pulumi.set(__self__, "instance_id", instance_id)
        if database_dialect is not None:
            pulumi.set(__self__, "database_dialect", database_dialect)
        if encryption_config is not None:
            pulumi.set(__self__, "encryption_config", encryption_config)
        if extra_statements is not None:
            pulumi.set(__self__, "extra_statements", extra_statements)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="createStatement")
    def create_statement(self) -> pulumi.Input[str]:
        """
        A `CREATE DATABASE` statement, which specifies the ID of the new database. The database ID must conform to the regular expression `a-z*[a-z0-9]` and be between 2 and 30 characters in length. If the database ID is a reserved word or if it contains a hyphen, the database ID must be enclosed in backticks (`` ` ``).
        """
        return pulumi.get(self, "create_statement")

    @create_statement.setter
    def create_statement(self, value: pulumi.Input[str]):
        pulumi.set(self, "create_statement", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="databaseDialect")
    def database_dialect(self) -> Optional[pulumi.Input['DatabaseDatabaseDialect']]:
        """
        Optional. The dialect of the Cloud Spanner Database.
        """
        return pulumi.get(self, "database_dialect")

    @database_dialect.setter
    def database_dialect(self, value: Optional[pulumi.Input['DatabaseDatabaseDialect']]):
        pulumi.set(self, "database_dialect", value)

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input['EncryptionConfigArgs']]:
        """
        Optional. The encryption configuration for the database. If this field is not specified, Cloud Spanner will encrypt/decrypt all data at rest using Google default encryption.
        """
        return pulumi.get(self, "encryption_config")

    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input['EncryptionConfigArgs']]):
        pulumi.set(self, "encryption_config", value)

    @property
    @pulumi.getter(name="extraStatements")
    def extra_statements(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Optional. A list of DDL statements to run inside the newly created database. Statements can create tables, indexes, etc. These statements execute atomically with the creation of the database: if there is an error in any statement, the database is not created.
        """
        return pulumi.get(self, "extra_statements")

    @extra_statements.setter
    def extra_statements(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "extra_statements", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class Database(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_statement: Optional[pulumi.Input[str]] = None,
                 database_dialect: Optional[pulumi.Input['DatabaseDatabaseDialect']] = None,
                 encryption_config: Optional[pulumi.Input[pulumi.InputType['EncryptionConfigArgs']]] = None,
                 extra_statements: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new Cloud Spanner database and starts to prepare it for serving. The returned long-running operation will have a name of the format `/operations/` and can be used to track preparation of the database. The metadata field type is CreateDatabaseMetadata. The response field type is Database, if successful.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_statement: A `CREATE DATABASE` statement, which specifies the ID of the new database. The database ID must conform to the regular expression `a-z*[a-z0-9]` and be between 2 and 30 characters in length. If the database ID is a reserved word or if it contains a hyphen, the database ID must be enclosed in backticks (`` ` ``).
        :param pulumi.Input['DatabaseDatabaseDialect'] database_dialect: Optional. The dialect of the Cloud Spanner Database.
        :param pulumi.Input[pulumi.InputType['EncryptionConfigArgs']] encryption_config: Optional. The encryption configuration for the database. If this field is not specified, Cloud Spanner will encrypt/decrypt all data at rest using Google default encryption.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] extra_statements: Optional. A list of DDL statements to run inside the newly created database. Statements can create tables, indexes, etc. These statements execute atomically with the creation of the database: if there is an error in any statement, the database is not created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Cloud Spanner database and starts to prepare it for serving. The returned long-running operation will have a name of the format `/operations/` and can be used to track preparation of the database. The metadata field type is CreateDatabaseMetadata. The response field type is Database, if successful.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param DatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_statement: Optional[pulumi.Input[str]] = None,
                 database_dialect: Optional[pulumi.Input['DatabaseDatabaseDialect']] = None,
                 encryption_config: Optional[pulumi.Input[pulumi.InputType['EncryptionConfigArgs']]] = None,
                 extra_statements: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatabaseArgs.__new__(DatabaseArgs)

            if create_statement is None and not opts.urn:
                raise TypeError("Missing required property 'create_statement'")
            __props__.__dict__["create_statement"] = create_statement
            __props__.__dict__["database_dialect"] = database_dialect
            __props__.__dict__["encryption_config"] = encryption_config
            __props__.__dict__["extra_statements"] = extra_statements
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["project"] = project
            __props__.__dict__["create_time"] = None
            __props__.__dict__["default_leader"] = None
            __props__.__dict__["earliest_version_time"] = None
            __props__.__dict__["encryption_info"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["restore_info"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["version_retention_period"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["instance_id", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Database, __self__).__init__(
            'google-native:spanner/v1:Database',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Database':
        """
        Get an existing Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatabaseArgs.__new__(DatabaseArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["database_dialect"] = None
        __props__.__dict__["default_leader"] = None
        __props__.__dict__["earliest_version_time"] = None
        __props__.__dict__["encryption_config"] = None
        __props__.__dict__["encryption_info"] = None
        __props__.__dict__["instance_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["restore_info"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["version_retention_period"] = None
        return Database(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        If exists, the time at which the database creation started.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="databaseDialect")
    def database_dialect(self) -> pulumi.Output[str]:
        """
        The dialect of the Cloud Spanner Database.
        """
        return pulumi.get(self, "database_dialect")

    @property
    @pulumi.getter(name="defaultLeader")
    def default_leader(self) -> pulumi.Output[str]:
        """
        The read-write region which contains the database's leader replicas. This is the same as the value of default_leader database option set using DatabaseAdmin.CreateDatabase or DatabaseAdmin.UpdateDatabaseDdl. If not explicitly set, this is empty.
        """
        return pulumi.get(self, "default_leader")

    @property
    @pulumi.getter(name="earliestVersionTime")
    def earliest_version_time(self) -> pulumi.Output[str]:
        """
        Earliest timestamp at which older versions of the data can be read. This value is continuously updated by Cloud Spanner and becomes stale the moment it is queried. If you are using this value to recover data, make sure to account for the time from the moment when the value is queried to the moment when you initiate the recovery.
        """
        return pulumi.get(self, "earliest_version_time")

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> pulumi.Output['outputs.EncryptionConfigResponse']:
        """
        For databases that are using customer managed encryption, this field contains the encryption configuration for the database. For databases that are using Google default or other types of encryption, this field is empty.
        """
        return pulumi.get(self, "encryption_config")

    @property
    @pulumi.getter(name="encryptionInfo")
    def encryption_info(self) -> pulumi.Output[Sequence['outputs.EncryptionInfoResponse']]:
        """
        For databases that are using customer managed encryption, this field contains the encryption information for the database, such as encryption state and the Cloud KMS key versions that are in use. For databases that are using Google default or other types of encryption, this field is empty. This field is propagated lazily from the backend. There might be a delay from when a key version is being used and when it appears in this field.
        """
        return pulumi.get(self, "encryption_info")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the database. Values are of the form `projects//instances//databases/`, where `` is as specified in the `CREATE DATABASE` statement. This name can be passed to other API methods to identify the database.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="restoreInfo")
    def restore_info(self) -> pulumi.Output['outputs.RestoreInfoResponse']:
        """
        Applicable only for restored databases. Contains information about the restore source.
        """
        return pulumi.get(self, "restore_info")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current database state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="versionRetentionPeriod")
    def version_retention_period(self) -> pulumi.Output[str]:
        """
        The period in which Cloud Spanner retains all versions of data for the database. This is the same as the value of version_retention_period database option set using UpdateDatabaseDdl. Defaults to 1 hour, if not set.
        """
        return pulumi.get(self, "version_retention_period")

