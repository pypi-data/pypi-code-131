# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'InstanceConfigNetworkConfig',
    'LogicalNetworkInterfaceNetworkType',
    'LunMultiprotocolType',
    'LunState',
    'LunStorageType',
    'NetworkConfigBandwidth',
    'NetworkConfigServiceCidr',
    'NetworkConfigType',
    'NfsExportPermissions',
    'VolumeConfigProtocol',
    'VolumeConfigType',
    'VolumeSnapshotAutoDeleteBehavior',
    'VolumeState',
    'VolumeStorageType',
]


class InstanceConfigNetworkConfig(str, Enum):
    """
    The type of network configuration on the instance.
    """
    NETWORKCONFIG_UNSPECIFIED = "NETWORKCONFIG_UNSPECIFIED"
    """
    The unspecified network configuration.
    """
    SINGLE_VLAN = "SINGLE_VLAN"
    """
    Instance part of single client network and single private network.
    """
    MULTI_VLAN = "MULTI_VLAN"
    """
    Instance part of multiple (or single) client networks and private networks.
    """


class LogicalNetworkInterfaceNetworkType(str, Enum):
    """
    Type of network.
    """
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    """
    Unspecified value.
    """
    CLIENT = "CLIENT"
    """
    Client network, a network peered to a Google Cloud VPC.
    """
    PRIVATE = "PRIVATE"
    """
    Private network, a network local to the Bare Metal Solution environment.
    """


class LunMultiprotocolType(str, Enum):
    """
    The LUN multiprotocol type ensures the characteristics of the LUN are optimized for each operating system.
    """
    MULTIPROTOCOL_TYPE_UNSPECIFIED = "MULTIPROTOCOL_TYPE_UNSPECIFIED"
    """
    Server has no OS specified.
    """
    LINUX = "LINUX"
    """
    Server with Linux OS.
    """


class LunState(str, Enum):
    """
    The state of this storage volume.
    """
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    """
    The LUN is in an unknown state.
    """
    CREATING = "CREATING"
    """
    The LUN is being created.
    """
    UPDATING = "UPDATING"
    """
    The LUN is being updated.
    """
    READY = "READY"
    """
    The LUN is ready for use.
    """
    DELETING = "DELETING"
    """
    The LUN has been requested to be deleted.
    """


class LunStorageType(str, Enum):
    """
    The storage type for this LUN.
    """
    STORAGE_TYPE_UNSPECIFIED = "STORAGE_TYPE_UNSPECIFIED"
    """
    The storage type for this LUN is unknown.
    """
    SSD = "SSD"
    """
    This storage type for this LUN is SSD.
    """
    HDD = "HDD"
    """
    This storage type for this LUN is HDD.
    """


class NetworkConfigBandwidth(str, Enum):
    """
    Interconnect bandwidth. Set only when type is CLIENT.
    """
    BANDWIDTH_UNSPECIFIED = "BANDWIDTH_UNSPECIFIED"
    """
    Unspecified value.
    """
    BW1_GBPS = "BW_1_GBPS"
    """
    1 Gbps.
    """
    BW2_GBPS = "BW_2_GBPS"
    """
    2 Gbps.
    """
    BW5_GBPS = "BW_5_GBPS"
    """
    5 Gbps.
    """
    BW10_GBPS = "BW_10_GBPS"
    """
    10 Gbps.
    """


class NetworkConfigServiceCidr(str, Enum):
    """
    Service CIDR, if any.
    """
    SERVICE_CIDR_UNSPECIFIED = "SERVICE_CIDR_UNSPECIFIED"
    """
    Unspecified value.
    """
    DISABLED = "DISABLED"
    """
    Services are disabled for the given network.
    """
    HIGH26 = "HIGH_26"
    """
    Use the highest /26 block of the network to host services.
    """
    HIGH27 = "HIGH_27"
    """
    Use the highest /27 block of the network to host services.
    """
    HIGH28 = "HIGH_28"
    """
    Use the highest /28 block of the network to host services.
    """


class NetworkConfigType(str, Enum):
    """
    The type of this network, either Client or Private.
    """
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    """
    Unspecified value.
    """
    CLIENT = "CLIENT"
    """
    Client network, that is a network peered to a GCP VPC.
    """
    PRIVATE = "PRIVATE"
    """
    Private network, that is a network local to the BMS POD.
    """


class NfsExportPermissions(str, Enum):
    """
    Export permissions.
    """
    PERMISSIONS_UNSPECIFIED = "PERMISSIONS_UNSPECIFIED"
    """
    Unspecified value.
    """
    READ_ONLY = "READ_ONLY"
    """
    Read-only permission.
    """
    READ_WRITE = "READ_WRITE"
    """
    Read-write permission.
    """


class VolumeConfigProtocol(str, Enum):
    """
    Volume protocol.
    """
    PROTOCOL_UNSPECIFIED = "PROTOCOL_UNSPECIFIED"
    """
    Unspecified value.
    """
    PROTOCOL_FC = "PROTOCOL_FC"
    """
    Fibre channel.
    """
    PROTOCOL_NFS = "PROTOCOL_NFS"
    """
    Network file system.
    """


class VolumeConfigType(str, Enum):
    """
    The type of this Volume.
    """
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    """
    The unspecified type.
    """
    FLASH = "FLASH"
    """
    This Volume is on flash.
    """
    DISK = "DISK"
    """
    This Volume is on disk.
    """


class VolumeSnapshotAutoDeleteBehavior(str, Enum):
    """
    The behavior to use when snapshot reserved space is full.
    """
    SNAPSHOT_AUTO_DELETE_BEHAVIOR_UNSPECIFIED = "SNAPSHOT_AUTO_DELETE_BEHAVIOR_UNSPECIFIED"
    """
    The unspecified behavior.
    """
    DISABLED = "DISABLED"
    """
    Don't delete any snapshots. This disables new snapshot creation, as long as the snapshot reserved space is full.
    """
    OLDEST_FIRST = "OLDEST_FIRST"
    """
    Delete the oldest snapshots first.
    """
    NEWEST_FIRST = "NEWEST_FIRST"
    """
    Delete the newest snapshots first.
    """


class VolumeState(str, Enum):
    """
    The state of this storage volume.
    """
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    """
    The storage volume is in an unknown state.
    """
    CREATING = "CREATING"
    """
    The storage volume is being created.
    """
    READY = "READY"
    """
    The storage volume is ready for use.
    """
    DELETING = "DELETING"
    """
    The storage volume has been requested to be deleted.
    """


class VolumeStorageType(str, Enum):
    """
    The storage type for this volume.
    """
    STORAGE_TYPE_UNSPECIFIED = "STORAGE_TYPE_UNSPECIFIED"
    """
    The storage type for this volume is unknown.
    """
    SSD = "SSD"
    """
    The storage type for this volume is SSD.
    """
    HDD = "HDD"
    """
    This storage type for this volume is HDD.
    """
