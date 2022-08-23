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
    'GetNamespaceResult',
    'AwaitableGetNamespaceResult',
    'get_namespace',
    'get_namespace_output',
]

@pulumi.output_type
class GetNamespaceResult:
    def __init__(__self__, admin_username=None, db_name=None, default_iam_role_arn=None, final_snapshot_name=None, final_snapshot_retention_period=None, iam_roles=None, kms_key_id=None, log_exports=None, namespace=None):
        if admin_username and not isinstance(admin_username, str):
            raise TypeError("Expected argument 'admin_username' to be a str")
        pulumi.set(__self__, "admin_username", admin_username)
        if db_name and not isinstance(db_name, str):
            raise TypeError("Expected argument 'db_name' to be a str")
        pulumi.set(__self__, "db_name", db_name)
        if default_iam_role_arn and not isinstance(default_iam_role_arn, str):
            raise TypeError("Expected argument 'default_iam_role_arn' to be a str")
        pulumi.set(__self__, "default_iam_role_arn", default_iam_role_arn)
        if final_snapshot_name and not isinstance(final_snapshot_name, str):
            raise TypeError("Expected argument 'final_snapshot_name' to be a str")
        pulumi.set(__self__, "final_snapshot_name", final_snapshot_name)
        if final_snapshot_retention_period and not isinstance(final_snapshot_retention_period, int):
            raise TypeError("Expected argument 'final_snapshot_retention_period' to be a int")
        pulumi.set(__self__, "final_snapshot_retention_period", final_snapshot_retention_period)
        if iam_roles and not isinstance(iam_roles, list):
            raise TypeError("Expected argument 'iam_roles' to be a list")
        pulumi.set(__self__, "iam_roles", iam_roles)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if log_exports and not isinstance(log_exports, list):
            raise TypeError("Expected argument 'log_exports' to be a list")
        pulumi.set(__self__, "log_exports", log_exports)
        if namespace and not isinstance(namespace, dict):
            raise TypeError("Expected argument 'namespace' to be a dict")
        pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[str]:
        """
        The user name associated with the admin user for the namespace that is being created. Only alphanumeric characters and underscores are allowed. It should start with an alphabet.
        """
        return pulumi.get(self, "admin_username")

    @property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[str]:
        """
        The database name associated for the namespace that is being created. Only alphanumeric characters and underscores are allowed. It should start with an alphabet.
        """
        return pulumi.get(self, "db_name")

    @property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> Optional[str]:
        """
        The default IAM role ARN for the namespace that is being created.
        """
        return pulumi.get(self, "default_iam_role_arn")

    @property
    @pulumi.getter(name="finalSnapshotName")
    def final_snapshot_name(self) -> Optional[str]:
        """
        The name of the namespace the source snapshot was created from. Please specify the name if needed before deleting namespace
        """
        return pulumi.get(self, "final_snapshot_name")

    @property
    @pulumi.getter(name="finalSnapshotRetentionPeriod")
    def final_snapshot_retention_period(self) -> Optional[int]:
        """
        The number of days to retain automated snapshot in the destination region after they are copied from the source region. If the value is -1, the manual snapshot is retained indefinitely. The value must be either -1 or an integer between 1 and 3,653.
        """
        return pulumi.get(self, "final_snapshot_retention_period")

    @property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> Optional[Sequence[str]]:
        """
        A list of AWS Identity and Access Management (IAM) roles that can be used by the namespace to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. The Default role limit for each request is 10.
        """
        return pulumi.get(self, "iam_roles")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the namespace.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> Optional[Sequence['NamespaceLogExport']]:
        """
        The collection of log types to be exported provided by the customer. Should only be one of the three supported log types: userlog, useractivitylog and connectionlog
        """
        return pulumi.get(self, "log_exports")

    @property
    @pulumi.getter
    def namespace(self) -> Optional['outputs.Namespace']:
        return pulumi.get(self, "namespace")


class AwaitableGetNamespaceResult(GetNamespaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceResult(
            admin_username=self.admin_username,
            db_name=self.db_name,
            default_iam_role_arn=self.default_iam_role_arn,
            final_snapshot_name=self.final_snapshot_name,
            final_snapshot_retention_period=self.final_snapshot_retention_period,
            iam_roles=self.iam_roles,
            kms_key_id=self.kms_key_id,
            log_exports=self.log_exports,
            namespace=self.namespace)


def get_namespace(namespace_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceResult:
    """
    Definition of AWS::RedshiftServerless::Namespace Resource Type


    :param str namespace_name: A unique identifier for the namespace. You use this identifier to refer to the namespace for any subsequent namespace operations such as deleting or modifying. All alphabetical characters must be lower case. Namespace name should be unique for all namespaces within an AWS account.
    """
    __args__ = dict()
    __args__['namespaceName'] = namespace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:redshiftserverless:getNamespace', __args__, opts=opts, typ=GetNamespaceResult).value

    return AwaitableGetNamespaceResult(
        admin_username=__ret__.admin_username,
        db_name=__ret__.db_name,
        default_iam_role_arn=__ret__.default_iam_role_arn,
        final_snapshot_name=__ret__.final_snapshot_name,
        final_snapshot_retention_period=__ret__.final_snapshot_retention_period,
        iam_roles=__ret__.iam_roles,
        kms_key_id=__ret__.kms_key_id,
        log_exports=__ret__.log_exports,
        namespace=__ret__.namespace)


@_utilities.lift_output_func(get_namespace)
def get_namespace_output(namespace_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceResult]:
    """
    Definition of AWS::RedshiftServerless::Namespace Resource Type


    :param str namespace_name: A unique identifier for the namespace. You use this identifier to refer to the namespace for any subsequent namespace operations such as deleting or modifying. All alphabetical characters must be lower case. Namespace name should be unique for all namespaces within an AWS account.
    """
    ...
