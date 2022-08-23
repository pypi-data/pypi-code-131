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
    'GetInstancesResult',
    'AwaitableGetInstancesResult',
    'get_instances',
    'get_instances_output',
]

@pulumi.output_type
class GetInstancesResult:
    """
    A collection of values returned by getInstances.
    """
    def __init__(__self__, architecture_type=None, edition_type=None, enable_details=None, engine_version=None, expired=None, global_instance=None, id=None, ids=None, instance_class=None, instance_type=None, instances=None, name_regex=None, names=None, network_type=None, output_file=None, payment_type=None, resource_group_id=None, search_key=None, status=None, tags=None, vpc_id=None, vswitch_id=None, zone_id=None):
        if architecture_type and not isinstance(architecture_type, str):
            raise TypeError("Expected argument 'architecture_type' to be a str")
        pulumi.set(__self__, "architecture_type", architecture_type)
        if edition_type and not isinstance(edition_type, str):
            raise TypeError("Expected argument 'edition_type' to be a str")
        pulumi.set(__self__, "edition_type", edition_type)
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
        if engine_version and not isinstance(engine_version, str):
            raise TypeError("Expected argument 'engine_version' to be a str")
        pulumi.set(__self__, "engine_version", engine_version)
        if expired and not isinstance(expired, str):
            raise TypeError("Expected argument 'expired' to be a str")
        pulumi.set(__self__, "expired", expired)
        if global_instance and not isinstance(global_instance, bool):
            raise TypeError("Expected argument 'global_instance' to be a bool")
        pulumi.set(__self__, "global_instance", global_instance)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_class and not isinstance(instance_class, str):
            raise TypeError("Expected argument 'instance_class' to be a str")
        pulumi.set(__self__, "instance_class", instance_class)
        if instance_type and not isinstance(instance_type, str):
            raise TypeError("Expected argument 'instance_type' to be a str")
        pulumi.set(__self__, "instance_type", instance_type)
        if instances and not isinstance(instances, list):
            raise TypeError("Expected argument 'instances' to be a list")
        pulumi.set(__self__, "instances", instances)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if network_type and not isinstance(network_type, str):
            raise TypeError("Expected argument 'network_type' to be a str")
        pulumi.set(__self__, "network_type", network_type)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if payment_type and not isinstance(payment_type, str):
            raise TypeError("Expected argument 'payment_type' to be a str")
        pulumi.set(__self__, "payment_type", payment_type)
        if resource_group_id and not isinstance(resource_group_id, str):
            raise TypeError("Expected argument 'resource_group_id' to be a str")
        pulumi.set(__self__, "resource_group_id", resource_group_id)
        if search_key and not isinstance(search_key, str):
            raise TypeError("Expected argument 'search_key' to be a str")
        pulumi.set(__self__, "search_key", search_key)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)
        if vswitch_id and not isinstance(vswitch_id, str):
            raise TypeError("Expected argument 'vswitch_id' to be a str")
        pulumi.set(__self__, "vswitch_id", vswitch_id)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="architectureType")
    def architecture_type(self) -> Optional[str]:
        return pulumi.get(self, "architecture_type")

    @property
    @pulumi.getter(name="editionType")
    def edition_type(self) -> Optional[str]:
        return pulumi.get(self, "edition_type")

    @property
    @pulumi.getter(name="enableDetails")
    def enable_details(self) -> Optional[bool]:
        return pulumi.get(self, "enable_details")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[str]:
        """
        The engine version of the instance.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter
    def expired(self) -> Optional[str]:
        return pulumi.get(self, "expired")

    @property
    @pulumi.getter(name="globalInstance")
    def global_instance(self) -> Optional[bool]:
        return pulumi.get(self, "global_instance")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        A list of KVStore Instance IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> Optional[str]:
        return pulumi.get(self, "instance_class")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[str]:
        """
        (Optional) Database type. Valid Values: `Memcache`, `Redis`. If no value is specified, all types are returned.
        * `instance_class`- (Optional) Type of the applied ApsaraDB for instance.
        For more information, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/61135.htm).
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter
    def instances(self) -> Sequence['outputs.GetInstancesInstanceResult']:
        """
        A list of KVStore Instances. Its every element contains the following attributes:
        """
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of KVStore Instance names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[str]:
        """
        The network type of the instance.
        """
        return pulumi.get(self, "network_type")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="paymentType")
    def payment_type(self) -> Optional[str]:
        """
        Billing method. Valid Values: `PostPaid` for  Pay-As-You-Go and `PrePaid` for subscription.
        """
        return pulumi.get(self, "payment_type")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[str]:
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter(name="searchKey")
    def search_key(self) -> Optional[str]:
        return pulumi.get(self, "search_key")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Status of the instance.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        """
        VPC ID the instance belongs to.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> Optional[str]:
        """
        VSwitch ID the instance belongs to.
        """
        return pulumi.get(self, "vswitch_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[str]:
        """
        The ID of zone.
        """
        return pulumi.get(self, "zone_id")


class AwaitableGetInstancesResult(GetInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstancesResult(
            architecture_type=self.architecture_type,
            edition_type=self.edition_type,
            enable_details=self.enable_details,
            engine_version=self.engine_version,
            expired=self.expired,
            global_instance=self.global_instance,
            id=self.id,
            ids=self.ids,
            instance_class=self.instance_class,
            instance_type=self.instance_type,
            instances=self.instances,
            name_regex=self.name_regex,
            names=self.names,
            network_type=self.network_type,
            output_file=self.output_file,
            payment_type=self.payment_type,
            resource_group_id=self.resource_group_id,
            search_key=self.search_key,
            status=self.status,
            tags=self.tags,
            vpc_id=self.vpc_id,
            vswitch_id=self.vswitch_id,
            zone_id=self.zone_id)


def get_instances(architecture_type: Optional[str] = None,
                  edition_type: Optional[str] = None,
                  enable_details: Optional[bool] = None,
                  engine_version: Optional[str] = None,
                  expired: Optional[str] = None,
                  global_instance: Optional[bool] = None,
                  ids: Optional[Sequence[str]] = None,
                  instance_class: Optional[str] = None,
                  instance_type: Optional[str] = None,
                  name_regex: Optional[str] = None,
                  network_type: Optional[str] = None,
                  output_file: Optional[str] = None,
                  payment_type: Optional[str] = None,
                  resource_group_id: Optional[str] = None,
                  search_key: Optional[str] = None,
                  status: Optional[str] = None,
                  tags: Optional[Mapping[str, Any]] = None,
                  vpc_id: Optional[str] = None,
                  vswitch_id: Optional[str] = None,
                  zone_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstancesResult:
    """
    The `kvstore.get_instances` data source provides a collection of kvstore instances available in Alicloud account.
    Filters support regular expression for the instance name, searches by tags, and other filters which are listed below.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.kvstore.get_instances(name_regex="testname")
    pulumi.export("firstInstanceName", default.instances[0].name)
    ```


    :param str architecture_type: The type of the architecture. Valid values: `cluster`, `standard` and `SplitRW`.
    :param str edition_type: Used to retrieve instances belong to specified `vswitch` resources.  Valid values: `Enterprise`, `Community`.
    :param bool enable_details: Default to `false`. Set it to true can output more details.
    :param str engine_version: The engine version. Valid values: `2.8`, `4.0`, `5.0`, `6.0`.
    :param str expired: The expiration status of the instance.
    :param bool global_instance: Whether to create a distributed cache.
    :param Sequence[str] ids: A list of KVStore DBInstance IDs.
    :param str instance_class: Type of the applied ApsaraDB for Redis instance. For more information, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/61135.htm).
    :param str instance_type: The engine type of the KVStore DBInstance. Options are `Memcache`, and `Redis`. If no value is specified, all types are returned.
    :param str name_regex: A regex string to apply to the instance name.
    :param str network_type: The type of the network. Valid values: `CLASSIC`, `VPC`.
    :param str payment_type: The payment type. Valid values: `PostPaid`, `PrePaid`.
    :param str resource_group_id: The ID of the resource group.
    :param str search_key: The name of the instance.
    :param str status: The status of the KVStore DBInstance. Valid values: `Changing`, `CleaningUpExpiredData`, `Creating`, `Flushing`, `HASwitching`, `Inactive`, `MajorVersionUpgrading`, `Migrating`, `NetworkModifying`, `Normal`, `Rebooting`, `SSLModifying`, `Transforming`, `ZoneMigrating`.
    :param Mapping[str, Any] tags: Query the instance bound to the tag. The format of the incoming value is `json` string, including `TagKey` and `TagValue`. `TagKey` cannot be null, and `TagValue` can be empty. Format example `{"key1":"value1"}`.
    :param str vpc_id: Used to retrieve instances belong to specified VPC.
    :param str vswitch_id: Used to retrieve instances belong to specified `vswitch` resources.
    :param str zone_id: The ID of the zone.
    """
    __args__ = dict()
    __args__['architectureType'] = architecture_type
    __args__['editionType'] = edition_type
    __args__['enableDetails'] = enable_details
    __args__['engineVersion'] = engine_version
    __args__['expired'] = expired
    __args__['globalInstance'] = global_instance
    __args__['ids'] = ids
    __args__['instanceClass'] = instance_class
    __args__['instanceType'] = instance_type
    __args__['nameRegex'] = name_regex
    __args__['networkType'] = network_type
    __args__['outputFile'] = output_file
    __args__['paymentType'] = payment_type
    __args__['resourceGroupId'] = resource_group_id
    __args__['searchKey'] = search_key
    __args__['status'] = status
    __args__['tags'] = tags
    __args__['vpcId'] = vpc_id
    __args__['vswitchId'] = vswitch_id
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:kvstore/getInstances:getInstances', __args__, opts=opts, typ=GetInstancesResult).value

    return AwaitableGetInstancesResult(
        architecture_type=__ret__.architecture_type,
        edition_type=__ret__.edition_type,
        enable_details=__ret__.enable_details,
        engine_version=__ret__.engine_version,
        expired=__ret__.expired,
        global_instance=__ret__.global_instance,
        id=__ret__.id,
        ids=__ret__.ids,
        instance_class=__ret__.instance_class,
        instance_type=__ret__.instance_type,
        instances=__ret__.instances,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        network_type=__ret__.network_type,
        output_file=__ret__.output_file,
        payment_type=__ret__.payment_type,
        resource_group_id=__ret__.resource_group_id,
        search_key=__ret__.search_key,
        status=__ret__.status,
        tags=__ret__.tags,
        vpc_id=__ret__.vpc_id,
        vswitch_id=__ret__.vswitch_id,
        zone_id=__ret__.zone_id)


@_utilities.lift_output_func(get_instances)
def get_instances_output(architecture_type: Optional[pulumi.Input[Optional[str]]] = None,
                         edition_type: Optional[pulumi.Input[Optional[str]]] = None,
                         enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                         engine_version: Optional[pulumi.Input[Optional[str]]] = None,
                         expired: Optional[pulumi.Input[Optional[str]]] = None,
                         global_instance: Optional[pulumi.Input[Optional[bool]]] = None,
                         ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                         instance_class: Optional[pulumi.Input[Optional[str]]] = None,
                         instance_type: Optional[pulumi.Input[Optional[str]]] = None,
                         name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                         network_type: Optional[pulumi.Input[Optional[str]]] = None,
                         output_file: Optional[pulumi.Input[Optional[str]]] = None,
                         payment_type: Optional[pulumi.Input[Optional[str]]] = None,
                         resource_group_id: Optional[pulumi.Input[Optional[str]]] = None,
                         search_key: Optional[pulumi.Input[Optional[str]]] = None,
                         status: Optional[pulumi.Input[Optional[str]]] = None,
                         tags: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                         vpc_id: Optional[pulumi.Input[Optional[str]]] = None,
                         vswitch_id: Optional[pulumi.Input[Optional[str]]] = None,
                         zone_id: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstancesResult]:
    """
    The `kvstore.get_instances` data source provides a collection of kvstore instances available in Alicloud account.
    Filters support regular expression for the instance name, searches by tags, and other filters which are listed below.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.kvstore.get_instances(name_regex="testname")
    pulumi.export("firstInstanceName", default.instances[0].name)
    ```


    :param str architecture_type: The type of the architecture. Valid values: `cluster`, `standard` and `SplitRW`.
    :param str edition_type: Used to retrieve instances belong to specified `vswitch` resources.  Valid values: `Enterprise`, `Community`.
    :param bool enable_details: Default to `false`. Set it to true can output more details.
    :param str engine_version: The engine version. Valid values: `2.8`, `4.0`, `5.0`, `6.0`.
    :param str expired: The expiration status of the instance.
    :param bool global_instance: Whether to create a distributed cache.
    :param Sequence[str] ids: A list of KVStore DBInstance IDs.
    :param str instance_class: Type of the applied ApsaraDB for Redis instance. For more information, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/61135.htm).
    :param str instance_type: The engine type of the KVStore DBInstance. Options are `Memcache`, and `Redis`. If no value is specified, all types are returned.
    :param str name_regex: A regex string to apply to the instance name.
    :param str network_type: The type of the network. Valid values: `CLASSIC`, `VPC`.
    :param str payment_type: The payment type. Valid values: `PostPaid`, `PrePaid`.
    :param str resource_group_id: The ID of the resource group.
    :param str search_key: The name of the instance.
    :param str status: The status of the KVStore DBInstance. Valid values: `Changing`, `CleaningUpExpiredData`, `Creating`, `Flushing`, `HASwitching`, `Inactive`, `MajorVersionUpgrading`, `Migrating`, `NetworkModifying`, `Normal`, `Rebooting`, `SSLModifying`, `Transforming`, `ZoneMigrating`.
    :param Mapping[str, Any] tags: Query the instance bound to the tag. The format of the incoming value is `json` string, including `TagKey` and `TagValue`. `TagKey` cannot be null, and `TagValue` can be empty. Format example `{"key1":"value1"}`.
    :param str vpc_id: Used to retrieve instances belong to specified VPC.
    :param str vswitch_id: Used to retrieve instances belong to specified `vswitch` resources.
    :param str zone_id: The ID of the zone.
    """
    ...
