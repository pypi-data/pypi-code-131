# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetBackupResult',
    'AwaitableGetBackupResult',
    'get_backup',
    'get_backup_output',
]

@pulumi.output_type
class GetBackupResult:
    def __init__(__self__, capacity_gb=None, create_time=None, description=None, download_bytes=None, kms_key_name=None, labels=None, name=None, satisfies_pzs=None, source_file_share=None, source_instance=None, source_instance_tier=None, state=None, storage_bytes=None):
        if capacity_gb and not isinstance(capacity_gb, str):
            raise TypeError("Expected argument 'capacity_gb' to be a str")
        pulumi.set(__self__, "capacity_gb", capacity_gb)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if download_bytes and not isinstance(download_bytes, str):
            raise TypeError("Expected argument 'download_bytes' to be a str")
        pulumi.set(__self__, "download_bytes", download_bytes)
        if kms_key_name and not isinstance(kms_key_name, str):
            raise TypeError("Expected argument 'kms_key_name' to be a str")
        pulumi.set(__self__, "kms_key_name", kms_key_name)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if satisfies_pzs and not isinstance(satisfies_pzs, bool):
            raise TypeError("Expected argument 'satisfies_pzs' to be a bool")
        pulumi.set(__self__, "satisfies_pzs", satisfies_pzs)
        if source_file_share and not isinstance(source_file_share, str):
            raise TypeError("Expected argument 'source_file_share' to be a str")
        pulumi.set(__self__, "source_file_share", source_file_share)
        if source_instance and not isinstance(source_instance, str):
            raise TypeError("Expected argument 'source_instance' to be a str")
        pulumi.set(__self__, "source_instance", source_instance)
        if source_instance_tier and not isinstance(source_instance_tier, str):
            raise TypeError("Expected argument 'source_instance_tier' to be a str")
        pulumi.set(__self__, "source_instance_tier", source_instance_tier)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if storage_bytes and not isinstance(storage_bytes, str):
            raise TypeError("Expected argument 'storage_bytes' to be a str")
        pulumi.set(__self__, "storage_bytes", storage_bytes)

    @property
    @pulumi.getter(name="capacityGb")
    def capacity_gb(self) -> str:
        """
        Capacity of the source file share when the backup was created.
        """
        return pulumi.get(self, "capacity_gb")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time when the backup was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description of the backup with 2048 characters or less. Requests with longer descriptions will be rejected.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="downloadBytes")
    def download_bytes(self) -> str:
        """
        Amount of bytes that will be downloaded if the backup is restored
        """
        return pulumi.get(self, "download_bytes")

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> str:
        """
        Immutable. KMS key name used for data encryption.
        """
        return pulumi.get(self, "kms_key_name")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Resource labels to represent user provided metadata.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the backup, in the format `projects/{project_id}/locations/{location_id}/backups/{backup_id}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> bool:
        """
        Reserved for future use.
        """
        return pulumi.get(self, "satisfies_pzs")

    @property
    @pulumi.getter(name="sourceFileShare")
    def source_file_share(self) -> str:
        """
        Name of the file share in the source Cloud Filestore instance that the backup is created from.
        """
        return pulumi.get(self, "source_file_share")

    @property
    @pulumi.getter(name="sourceInstance")
    def source_instance(self) -> str:
        """
        The resource name of the source Cloud Filestore instance, in the format `projects/{project_id}/locations/{location_id}/instances/{instance_id}`, used to create this backup.
        """
        return pulumi.get(self, "source_instance")

    @property
    @pulumi.getter(name="sourceInstanceTier")
    def source_instance_tier(self) -> str:
        """
        The service tier of the source Cloud Filestore instance that this backup is created from.
        """
        return pulumi.get(self, "source_instance_tier")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The backup state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageBytes")
    def storage_bytes(self) -> str:
        """
        The size of the storage used by the backup. As backups share storage, this number is expected to change with backup creation/deletion.
        """
        return pulumi.get(self, "storage_bytes")


class AwaitableGetBackupResult(GetBackupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackupResult(
            capacity_gb=self.capacity_gb,
            create_time=self.create_time,
            description=self.description,
            download_bytes=self.download_bytes,
            kms_key_name=self.kms_key_name,
            labels=self.labels,
            name=self.name,
            satisfies_pzs=self.satisfies_pzs,
            source_file_share=self.source_file_share,
            source_instance=self.source_instance,
            source_instance_tier=self.source_instance_tier,
            state=self.state,
            storage_bytes=self.storage_bytes)


def get_backup(backup_id: Optional[str] = None,
               location: Optional[str] = None,
               project: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackupResult:
    """
    Gets the details of a specific backup.
    """
    __args__ = dict()
    __args__['backupId'] = backup_id
    __args__['location'] = location
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:file/v1beta1:getBackup', __args__, opts=opts, typ=GetBackupResult).value

    return AwaitableGetBackupResult(
        capacity_gb=__ret__.capacity_gb,
        create_time=__ret__.create_time,
        description=__ret__.description,
        download_bytes=__ret__.download_bytes,
        kms_key_name=__ret__.kms_key_name,
        labels=__ret__.labels,
        name=__ret__.name,
        satisfies_pzs=__ret__.satisfies_pzs,
        source_file_share=__ret__.source_file_share,
        source_instance=__ret__.source_instance,
        source_instance_tier=__ret__.source_instance_tier,
        state=__ret__.state,
        storage_bytes=__ret__.storage_bytes)


@_utilities.lift_output_func(get_backup)
def get_backup_output(backup_id: Optional[pulumi.Input[str]] = None,
                      location: Optional[pulumi.Input[str]] = None,
                      project: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBackupResult]:
    """
    Gets the details of a specific backup.
    """
    ...
