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

__all__ = [
    'GetDedicatedHostAccountsAccountResult',
    'GetDedicatedHostGroupsGroupResult',
    'GetDedicatedHostGroupsGroupDedicatedHostCountGroupByHostTypeResult',
    'GetDedicatedHostGroupsGroupZoneIdListResult',
    'GetDedicatedHostsHostResult',
    'GetHostEcsLevelInfosInfoResult',
    'GetZonesZoneResult',
]

@pulumi.output_type
class GetDedicatedHostAccountsAccountResult(dict):
    def __init__(__self__, *,
                 account_name: str,
                 dedicated_host_id: str,
                 id: str):
        """
        :param str account_name: The name of the Dedicated host account.
        :param str dedicated_host_id: The ID of the Dedicated host.
        :param str id: The ID of the Dedicated Host Account. The value formats as `<dedicated_host_id>:<account_name>`.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "dedicated_host_id", dedicated_host_id)
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> str:
        """
        The name of the Dedicated host account.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="dedicatedHostId")
    def dedicated_host_id(self) -> str:
        """
        The ID of the Dedicated host.
        """
        return pulumi.get(self, "dedicated_host_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Dedicated Host Account. The value formats as `<dedicated_host_id>:<account_name>`.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class GetDedicatedHostGroupsGroupResult(dict):
    def __init__(__self__, *,
                 allocation_policy: str,
                 bastion_instance_id: str,
                 cpu_allocate_ration: float,
                 cpu_allocated_amount: float,
                 cpu_allocation_ratio: int,
                 create_time: str,
                 dedicated_host_count_group_by_host_types: Sequence['outputs.GetDedicatedHostGroupsGroupDedicatedHostCountGroupByHostTypeResult'],
                 dedicated_host_group_desc: str,
                 dedicated_host_group_id: str,
                 deploy_type: str,
                 disk_allocate_ration: float,
                 disk_allocated_amount: float,
                 disk_allocation_ratio: int,
                 disk_used_amount: float,
                 disk_utility: float,
                 engine: str,
                 host_number: int,
                 host_replace_policy: str,
                 id: str,
                 instance_number: int,
                 mem_allocate_ration: float,
                 mem_allocated_amount: float,
                 mem_allocation_ratio: int,
                 mem_used_amount: float,
                 mem_utility: float,
                 text: str,
                 vpc_id: str,
                 zone_id_lists: Sequence['outputs.GetDedicatedHostGroupsGroupZoneIdListResult']):
        """
        :param str allocation_policy: The policy that is used to allocate resources in the dedicated cluster. Valid values:`Evenly`,`Intensively`
        :param str bastion_instance_id: The Bastion Instance id of the Dedicated Host Group.
        :param float cpu_allocate_ration: The CPU overcommitment ratio of the dedicated cluster. If you set this parameter to 200, the CPU resources that can be allocated are twice as many as the CPU resources that are provided. This maximizes the CPU utilization. Valid values: 100 to 300. Default value: 200.
        :param float cpu_allocated_amount: The CPU Allocated Amount of the Dedicated Host Group.
        :param int cpu_allocation_ratio: The CPU overcommitment ratio of the dedicated cluster.Valid values: 100 to 300. Default value: 200.
        :param str create_time: The Created Time of the Dedicated Host Group.
        :param Sequence['GetDedicatedHostGroupsGroupDedicatedHostCountGroupByHostTypeArgs'] dedicated_host_count_group_by_host_types: The Dedicated Host Count Group by Host Type of the Dedicated Host Group.
        :param str dedicated_host_group_desc: -The name of the dedicated cluster. The name must be 1 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        :param str dedicated_host_group_id: Dedicated Host Group ID.
        :param str deploy_type: The Deployment Type of the Dedicated Host Group.
        :param float disk_allocate_ration: The storage overcommitment ratio of the dedicated cluster.Valid values: 100 to 300. Default value: 200.
        :param float disk_allocated_amount: The Disk Allocated Amount of the Dedicated Host Group.
        :param int disk_allocation_ratio: The Disk Allocation Ratio of the Dedicated Host Group.
        :param float disk_used_amount: The DiskUsedAmount of the Dedicated Host Group.
        :param float disk_utility: The DiskUtility of the Dedicated Host Group.
        :param str engine: Database Engine Type.The database engine of the dedicated cluster. Valid values:`Redis`, `SQLServer`, `MySQL`, `PostgreSQL`, `MongoDB`
        :param int host_number: The Total Host Number  of the Dedicated Host Group.
        :param str host_replace_policy: The policy based on which the system handles host failures. Valid values:`Auto`,`Manual`
        :param str id: The ID of the Dedicated Host Group.
        :param int instance_number: The Total Instance Number of the Dedicated Host Group.
        :param float mem_allocate_ration: The maximum memory usage of each host in the dedicated cluster.Valid values: 0 to 90. Default value: 90.
        :param float mem_allocated_amount: The MemAllocatedAmount of the Dedicated Host Group.
        :param int mem_allocation_ratio: The Memory Allocation Ratio of the Dedicated Host Group.
        :param float mem_used_amount: The MemUsedAmount of the Dedicated Host Group.
        :param float mem_utility: The Mem Utility of the Dedicated Host Group.
        :param str text: The Text of the Dedicated Host Group.
        :param str vpc_id: The virtual private cloud (VPC) ID of the dedicated cluster.
        :param Sequence['GetDedicatedHostGroupsGroupZoneIdListArgs'] zone_id_lists: The ZoneIDList of the Dedicated Host Group.
        """
        pulumi.set(__self__, "allocation_policy", allocation_policy)
        pulumi.set(__self__, "bastion_instance_id", bastion_instance_id)
        pulumi.set(__self__, "cpu_allocate_ration", cpu_allocate_ration)
        pulumi.set(__self__, "cpu_allocated_amount", cpu_allocated_amount)
        pulumi.set(__self__, "cpu_allocation_ratio", cpu_allocation_ratio)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "dedicated_host_count_group_by_host_types", dedicated_host_count_group_by_host_types)
        pulumi.set(__self__, "dedicated_host_group_desc", dedicated_host_group_desc)
        pulumi.set(__self__, "dedicated_host_group_id", dedicated_host_group_id)
        pulumi.set(__self__, "deploy_type", deploy_type)
        pulumi.set(__self__, "disk_allocate_ration", disk_allocate_ration)
        pulumi.set(__self__, "disk_allocated_amount", disk_allocated_amount)
        pulumi.set(__self__, "disk_allocation_ratio", disk_allocation_ratio)
        pulumi.set(__self__, "disk_used_amount", disk_used_amount)
        pulumi.set(__self__, "disk_utility", disk_utility)
        pulumi.set(__self__, "engine", engine)
        pulumi.set(__self__, "host_number", host_number)
        pulumi.set(__self__, "host_replace_policy", host_replace_policy)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "instance_number", instance_number)
        pulumi.set(__self__, "mem_allocate_ration", mem_allocate_ration)
        pulumi.set(__self__, "mem_allocated_amount", mem_allocated_amount)
        pulumi.set(__self__, "mem_allocation_ratio", mem_allocation_ratio)
        pulumi.set(__self__, "mem_used_amount", mem_used_amount)
        pulumi.set(__self__, "mem_utility", mem_utility)
        pulumi.set(__self__, "text", text)
        pulumi.set(__self__, "vpc_id", vpc_id)
        pulumi.set(__self__, "zone_id_lists", zone_id_lists)

    @property
    @pulumi.getter(name="allocationPolicy")
    def allocation_policy(self) -> str:
        """
        The policy that is used to allocate resources in the dedicated cluster. Valid values:`Evenly`,`Intensively`
        """
        return pulumi.get(self, "allocation_policy")

    @property
    @pulumi.getter(name="bastionInstanceId")
    def bastion_instance_id(self) -> str:
        """
        The Bastion Instance id of the Dedicated Host Group.
        """
        return pulumi.get(self, "bastion_instance_id")

    @property
    @pulumi.getter(name="cpuAllocateRation")
    def cpu_allocate_ration(self) -> float:
        """
        The CPU overcommitment ratio of the dedicated cluster. If you set this parameter to 200, the CPU resources that can be allocated are twice as many as the CPU resources that are provided. This maximizes the CPU utilization. Valid values: 100 to 300. Default value: 200.
        """
        return pulumi.get(self, "cpu_allocate_ration")

    @property
    @pulumi.getter(name="cpuAllocatedAmount")
    def cpu_allocated_amount(self) -> float:
        """
        The CPU Allocated Amount of the Dedicated Host Group.
        """
        return pulumi.get(self, "cpu_allocated_amount")

    @property
    @pulumi.getter(name="cpuAllocationRatio")
    def cpu_allocation_ratio(self) -> int:
        """
        The CPU overcommitment ratio of the dedicated cluster.Valid values: 100 to 300. Default value: 200.
        """
        return pulumi.get(self, "cpu_allocation_ratio")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The Created Time of the Dedicated Host Group.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dedicatedHostCountGroupByHostTypes")
    def dedicated_host_count_group_by_host_types(self) -> Sequence['outputs.GetDedicatedHostGroupsGroupDedicatedHostCountGroupByHostTypeResult']:
        """
        The Dedicated Host Count Group by Host Type of the Dedicated Host Group.
        """
        return pulumi.get(self, "dedicated_host_count_group_by_host_types")

    @property
    @pulumi.getter(name="dedicatedHostGroupDesc")
    def dedicated_host_group_desc(self) -> str:
        """
        -The name of the dedicated cluster. The name must be 1 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        """
        return pulumi.get(self, "dedicated_host_group_desc")

    @property
    @pulumi.getter(name="dedicatedHostGroupId")
    def dedicated_host_group_id(self) -> str:
        """
        Dedicated Host Group ID.
        """
        return pulumi.get(self, "dedicated_host_group_id")

    @property
    @pulumi.getter(name="deployType")
    def deploy_type(self) -> str:
        """
        The Deployment Type of the Dedicated Host Group.
        """
        return pulumi.get(self, "deploy_type")

    @property
    @pulumi.getter(name="diskAllocateRation")
    def disk_allocate_ration(self) -> float:
        """
        The storage overcommitment ratio of the dedicated cluster.Valid values: 100 to 300. Default value: 200.
        """
        return pulumi.get(self, "disk_allocate_ration")

    @property
    @pulumi.getter(name="diskAllocatedAmount")
    def disk_allocated_amount(self) -> float:
        """
        The Disk Allocated Amount of the Dedicated Host Group.
        """
        return pulumi.get(self, "disk_allocated_amount")

    @property
    @pulumi.getter(name="diskAllocationRatio")
    def disk_allocation_ratio(self) -> int:
        """
        The Disk Allocation Ratio of the Dedicated Host Group.
        """
        return pulumi.get(self, "disk_allocation_ratio")

    @property
    @pulumi.getter(name="diskUsedAmount")
    def disk_used_amount(self) -> float:
        """
        The DiskUsedAmount of the Dedicated Host Group.
        """
        return pulumi.get(self, "disk_used_amount")

    @property
    @pulumi.getter(name="diskUtility")
    def disk_utility(self) -> float:
        """
        The DiskUtility of the Dedicated Host Group.
        """
        return pulumi.get(self, "disk_utility")

    @property
    @pulumi.getter
    def engine(self) -> str:
        """
        Database Engine Type.The database engine of the dedicated cluster. Valid values:`Redis`, `SQLServer`, `MySQL`, `PostgreSQL`, `MongoDB`
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="hostNumber")
    def host_number(self) -> int:
        """
        The Total Host Number  of the Dedicated Host Group.
        """
        return pulumi.get(self, "host_number")

    @property
    @pulumi.getter(name="hostReplacePolicy")
    def host_replace_policy(self) -> str:
        """
        The policy based on which the system handles host failures. Valid values:`Auto`,`Manual`
        """
        return pulumi.get(self, "host_replace_policy")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Dedicated Host Group.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceNumber")
    def instance_number(self) -> int:
        """
        The Total Instance Number of the Dedicated Host Group.
        """
        return pulumi.get(self, "instance_number")

    @property
    @pulumi.getter(name="memAllocateRation")
    def mem_allocate_ration(self) -> float:
        """
        The maximum memory usage of each host in the dedicated cluster.Valid values: 0 to 90. Default value: 90.
        """
        return pulumi.get(self, "mem_allocate_ration")

    @property
    @pulumi.getter(name="memAllocatedAmount")
    def mem_allocated_amount(self) -> float:
        """
        The MemAllocatedAmount of the Dedicated Host Group.
        """
        return pulumi.get(self, "mem_allocated_amount")

    @property
    @pulumi.getter(name="memAllocationRatio")
    def mem_allocation_ratio(self) -> int:
        """
        The Memory Allocation Ratio of the Dedicated Host Group.
        """
        return pulumi.get(self, "mem_allocation_ratio")

    @property
    @pulumi.getter(name="memUsedAmount")
    def mem_used_amount(self) -> float:
        """
        The MemUsedAmount of the Dedicated Host Group.
        """
        return pulumi.get(self, "mem_used_amount")

    @property
    @pulumi.getter(name="memUtility")
    def mem_utility(self) -> float:
        """
        The Mem Utility of the Dedicated Host Group.
        """
        return pulumi.get(self, "mem_utility")

    @property
    @pulumi.getter
    def text(self) -> str:
        """
        The Text of the Dedicated Host Group.
        """
        return pulumi.get(self, "text")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        The virtual private cloud (VPC) ID of the dedicated cluster.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="zoneIdLists")
    def zone_id_lists(self) -> Sequence['outputs.GetDedicatedHostGroupsGroupZoneIdListResult']:
        """
        The ZoneIDList of the Dedicated Host Group.
        """
        return pulumi.get(self, "zone_id_lists")


@pulumi.output_type
class GetDedicatedHostGroupsGroupDedicatedHostCountGroupByHostTypeResult(dict):
    def __init__(__self__, *,
                 place_holder: str):
        pulumi.set(__self__, "place_holder", place_holder)

    @property
    @pulumi.getter(name="placeHolder")
    def place_holder(self) -> str:
        return pulumi.get(self, "place_holder")


@pulumi.output_type
class GetDedicatedHostGroupsGroupZoneIdListResult(dict):
    def __init__(__self__, *,
                 zone_id_lists: Sequence[str]):
        """
        :param Sequence[str] zone_id_lists: The ZoneIDList of the Dedicated Host Group.
        """
        pulumi.set(__self__, "zone_id_lists", zone_id_lists)

    @property
    @pulumi.getter(name="zoneIdLists")
    def zone_id_lists(self) -> Sequence[str]:
        """
        The ZoneIDList of the Dedicated Host Group.
        """
        return pulumi.get(self, "zone_id_lists")


@pulumi.output_type
class GetDedicatedHostsHostResult(dict):
    def __init__(__self__, *,
                 allocation_status: str,
                 bastion_instance_id: str,
                 cpu_allocation_ratio: str,
                 cpu_used: str,
                 create_time: str,
                 dedicated_host_group_id: str,
                 dedicated_host_id: str,
                 disk_allocation_ratio: str,
                 ecs_class_code: str,
                 end_time: str,
                 engine: str,
                 expired_time: str,
                 host_class: str,
                 host_cpu: str,
                 host_mem: str,
                 host_name: str,
                 host_storage: str,
                 host_type: str,
                 id: str,
                 image_category: str,
                 ip_address: str,
                 mem_allocation_ratio: str,
                 memory_used: str,
                 open_permission: str,
                 status: str,
                 storage_used: str,
                 tags: Mapping[str, Any],
                 vpc_id: str,
                 vswitch_id: str,
                 zone_id: str):
        """
        :param str allocation_status: Specifies whether instances can be created on the host. Valid values: `1` or `0`. `1`: Instances can be created on the host. `0`: Instances cannot be created on the host.
        :param str bastion_instance_id: The ID of the bastion host with which the host is associated.
        :param str cpu_allocation_ratio: The numeric value of the CPU over commit ratio of the dedicated cluster.
        :param str cpu_used: The number of CPU cores used by the host.
        :param str create_time: The time when the host was created. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        :param str dedicated_host_group_id: The ID of the dedicated cluster in which the host is created.
        :param str dedicated_host_id: The ID of the host.
        :param str disk_allocation_ratio: The disk usage in percentage.
        :param str ecs_class_code: The Elastic Compute Service (ECS) instance type.
        :param str end_time: The time when the host expires. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        :param str engine: The type of the database engine that is used by the host.
        :param str expired_time: The time when the host expires. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        :param str host_class: The instance type of the host.
        :param str host_cpu: The number of CPU cores specified for the host. Unit: `core`.
        :param str host_mem: The memory of the host. Unit: `GB`.
        :param str host_name: The name of the host.
        :param str host_storage: The total storage capacity of the host. Unit: `GB`.
        :param str host_type: The storage type of the host.
        :param str id: The ID of the Dedicated Host. The value formats as `<dedicated_host_group_id>:<dedicated_host_id>`.
        :param str image_category: The image type of the host.
        :param str ip_address: The IP address of the host.
        :param str mem_allocation_ratio: The memory usage in percentage.
        :param str memory_used: The amount of memory used by the host. Unit: `GB`.
        :param str open_permission: Indicates whether you have the OS permissions on the host. Valid values: `0`: You do not have the OS permissions on the host. `1`: You have the OS permissions on the host.
        :param str status: The state of the host.
        :param str storage_used: The storage usage of the host. Unit: `GB`.
        :param Mapping[str, Any] tags: The tag of the resource.
        :param str vpc_id: The ID of the virtual private cloud (VPC) to which the host is connected.
        :param str vswitch_id: The ID of the vSwitch.
        :param str zone_id: The zone ID of the host.
        """
        pulumi.set(__self__, "allocation_status", allocation_status)
        pulumi.set(__self__, "bastion_instance_id", bastion_instance_id)
        pulumi.set(__self__, "cpu_allocation_ratio", cpu_allocation_ratio)
        pulumi.set(__self__, "cpu_used", cpu_used)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "dedicated_host_group_id", dedicated_host_group_id)
        pulumi.set(__self__, "dedicated_host_id", dedicated_host_id)
        pulumi.set(__self__, "disk_allocation_ratio", disk_allocation_ratio)
        pulumi.set(__self__, "ecs_class_code", ecs_class_code)
        pulumi.set(__self__, "end_time", end_time)
        pulumi.set(__self__, "engine", engine)
        pulumi.set(__self__, "expired_time", expired_time)
        pulumi.set(__self__, "host_class", host_class)
        pulumi.set(__self__, "host_cpu", host_cpu)
        pulumi.set(__self__, "host_mem", host_mem)
        pulumi.set(__self__, "host_name", host_name)
        pulumi.set(__self__, "host_storage", host_storage)
        pulumi.set(__self__, "host_type", host_type)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "image_category", image_category)
        pulumi.set(__self__, "ip_address", ip_address)
        pulumi.set(__self__, "mem_allocation_ratio", mem_allocation_ratio)
        pulumi.set(__self__, "memory_used", memory_used)
        pulumi.set(__self__, "open_permission", open_permission)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "storage_used", storage_used)
        pulumi.set(__self__, "tags", tags)
        pulumi.set(__self__, "vpc_id", vpc_id)
        pulumi.set(__self__, "vswitch_id", vswitch_id)
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="allocationStatus")
    def allocation_status(self) -> str:
        """
        Specifies whether instances can be created on the host. Valid values: `1` or `0`. `1`: Instances can be created on the host. `0`: Instances cannot be created on the host.
        """
        return pulumi.get(self, "allocation_status")

    @property
    @pulumi.getter(name="bastionInstanceId")
    def bastion_instance_id(self) -> str:
        """
        The ID of the bastion host with which the host is associated.
        """
        return pulumi.get(self, "bastion_instance_id")

    @property
    @pulumi.getter(name="cpuAllocationRatio")
    def cpu_allocation_ratio(self) -> str:
        """
        The numeric value of the CPU over commit ratio of the dedicated cluster.
        """
        return pulumi.get(self, "cpu_allocation_ratio")

    @property
    @pulumi.getter(name="cpuUsed")
    def cpu_used(self) -> str:
        """
        The number of CPU cores used by the host.
        """
        return pulumi.get(self, "cpu_used")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time when the host was created. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dedicatedHostGroupId")
    def dedicated_host_group_id(self) -> str:
        """
        The ID of the dedicated cluster in which the host is created.
        """
        return pulumi.get(self, "dedicated_host_group_id")

    @property
    @pulumi.getter(name="dedicatedHostId")
    def dedicated_host_id(self) -> str:
        """
        The ID of the host.
        """
        return pulumi.get(self, "dedicated_host_id")

    @property
    @pulumi.getter(name="diskAllocationRatio")
    def disk_allocation_ratio(self) -> str:
        """
        The disk usage in percentage.
        """
        return pulumi.get(self, "disk_allocation_ratio")

    @property
    @pulumi.getter(name="ecsClassCode")
    def ecs_class_code(self) -> str:
        """
        The Elastic Compute Service (ECS) instance type.
        """
        return pulumi.get(self, "ecs_class_code")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        The time when the host expires. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def engine(self) -> str:
        """
        The type of the database engine that is used by the host.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="expiredTime")
    def expired_time(self) -> str:
        """
        The time when the host expires. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        """
        return pulumi.get(self, "expired_time")

    @property
    @pulumi.getter(name="hostClass")
    def host_class(self) -> str:
        """
        The instance type of the host.
        """
        return pulumi.get(self, "host_class")

    @property
    @pulumi.getter(name="hostCpu")
    def host_cpu(self) -> str:
        """
        The number of CPU cores specified for the host. Unit: `core`.
        """
        return pulumi.get(self, "host_cpu")

    @property
    @pulumi.getter(name="hostMem")
    def host_mem(self) -> str:
        """
        The memory of the host. Unit: `GB`.
        """
        return pulumi.get(self, "host_mem")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> str:
        """
        The name of the host.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter(name="hostStorage")
    def host_storage(self) -> str:
        """
        The total storage capacity of the host. Unit: `GB`.
        """
        return pulumi.get(self, "host_storage")

    @property
    @pulumi.getter(name="hostType")
    def host_type(self) -> str:
        """
        The storage type of the host.
        """
        return pulumi.get(self, "host_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Dedicated Host. The value formats as `<dedicated_host_group_id>:<dedicated_host_id>`.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageCategory")
    def image_category(self) -> str:
        """
        The image type of the host.
        """
        return pulumi.get(self, "image_category")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        The IP address of the host.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="memAllocationRatio")
    def mem_allocation_ratio(self) -> str:
        """
        The memory usage in percentage.
        """
        return pulumi.get(self, "mem_allocation_ratio")

    @property
    @pulumi.getter(name="memoryUsed")
    def memory_used(self) -> str:
        """
        The amount of memory used by the host. Unit: `GB`.
        """
        return pulumi.get(self, "memory_used")

    @property
    @pulumi.getter(name="openPermission")
    def open_permission(self) -> str:
        """
        Indicates whether you have the OS permissions on the host. Valid values: `0`: You do not have the OS permissions on the host. `1`: You have the OS permissions on the host.
        """
        return pulumi.get(self, "open_permission")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The state of the host.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageUsed")
    def storage_used(self) -> str:
        """
        The storage usage of the host. Unit: `GB`.
        """
        return pulumi.get(self, "storage_used")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, Any]:
        """
        The tag of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        The ID of the virtual private cloud (VPC) to which the host is connected.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> str:
        """
        The ID of the vSwitch.
        """
        return pulumi.get(self, "vswitch_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        """
        The zone ID of the host.
        """
        return pulumi.get(self, "zone_id")


@pulumi.output_type
class GetHostEcsLevelInfosInfoResult(dict):
    def __init__(__self__, *,
                 description: str,
                 ecs_class: str,
                 ecs_class_code: str,
                 res_class_code: str):
        """
        :param str description: The description of the host ecs level info.
        :param str ecs_class: The instance family of the host ecs level info.
        :param str ecs_class_code: The Elastic Compute Service (ECS) instance type.
        :param str res_class_code: The ApsaraDB RDS instance type of the host ecs level info.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "ecs_class", ecs_class)
        pulumi.set(__self__, "ecs_class_code", ecs_class_code)
        pulumi.set(__self__, "res_class_code", res_class_code)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the host ecs level info.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ecsClass")
    def ecs_class(self) -> str:
        """
        The instance family of the host ecs level info.
        """
        return pulumi.get(self, "ecs_class")

    @property
    @pulumi.getter(name="ecsClassCode")
    def ecs_class_code(self) -> str:
        """
        The Elastic Compute Service (ECS) instance type.
        """
        return pulumi.get(self, "ecs_class_code")

    @property
    @pulumi.getter(name="resClassCode")
    def res_class_code(self) -> str:
        """
        The ApsaraDB RDS instance type of the host ecs level info.
        """
        return pulumi.get(self, "res_class_code")


@pulumi.output_type
class GetZonesZoneResult(dict):
    def __init__(__self__, *,
                 id: str,
                 region_id: str,
                 zone_id: str):
        """
        :param str id: The ID of the zone.
        :param str region_id: The ID of the region.
        :param str zone_id: The ID of the zone.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "region_id", region_id)
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the zone.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> str:
        """
        The ID of the region.
        """
        return pulumi.get(self, "region_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        """
        The ID of the zone.
        """
        return pulumi.get(self, "zone_id")


