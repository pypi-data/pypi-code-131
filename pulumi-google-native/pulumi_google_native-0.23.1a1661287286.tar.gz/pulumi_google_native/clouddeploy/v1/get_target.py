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
    'GetTargetResult',
    'AwaitableGetTargetResult',
    'get_target',
    'get_target_output',
]

@pulumi.output_type
class GetTargetResult:
    def __init__(__self__, annotations=None, anthos_cluster=None, create_time=None, description=None, etag=None, execution_configs=None, gke=None, labels=None, name=None, require_approval=None, target_id=None, uid=None, update_time=None):
        if annotations and not isinstance(annotations, dict):
            raise TypeError("Expected argument 'annotations' to be a dict")
        pulumi.set(__self__, "annotations", annotations)
        if anthos_cluster and not isinstance(anthos_cluster, dict):
            raise TypeError("Expected argument 'anthos_cluster' to be a dict")
        pulumi.set(__self__, "anthos_cluster", anthos_cluster)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if execution_configs and not isinstance(execution_configs, list):
            raise TypeError("Expected argument 'execution_configs' to be a list")
        pulumi.set(__self__, "execution_configs", execution_configs)
        if gke and not isinstance(gke, dict):
            raise TypeError("Expected argument 'gke' to be a dict")
        pulumi.set(__self__, "gke", gke)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if require_approval and not isinstance(require_approval, bool):
            raise TypeError("Expected argument 'require_approval' to be a bool")
        pulumi.set(__self__, "require_approval", require_approval)
        if target_id and not isinstance(target_id, str):
            raise TypeError("Expected argument 'target_id' to be a str")
        pulumi.set(__self__, "target_id", target_id)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def annotations(self) -> Mapping[str, str]:
        """
        Optional. User annotations. These attributes can only be set and used by the user, and not by Google Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="anthosCluster")
    def anthos_cluster(self) -> 'outputs.AnthosClusterResponse':
        """
        Information specifying an Anthos Cluster.
        """
        return pulumi.get(self, "anthos_cluster")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Time at which the `Target` was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional. Description of the `Target`. Max length is 255 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="executionConfigs")
    def execution_configs(self) -> Sequence['outputs.ExecutionConfigResponse']:
        """
        Configurations for all execution that relates to this `Target`. Each `ExecutionEnvironmentUsage` value may only be used in a single configuration; using the same value multiple times is an error. When one or more configurations are specified, they must include the `RENDER` and `DEPLOY` `ExecutionEnvironmentUsage` values. When no configurations are specified, execution will use the default specified in `DefaultPool`.
        """
        return pulumi.get(self, "execution_configs")

    @property
    @pulumi.getter
    def gke(self) -> 'outputs.GkeClusterResponse':
        """
        Information specifying a GKE Cluster.
        """
        return pulumi.get(self, "gke")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Optional. Labels are attributes that can be set and used by both the user and by Google Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Optional. Name of the `Target`. Format is projects/{project}/locations/{location}/targets/a-z{0,62}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="requireApproval")
    def require_approval(self) -> bool:
        """
        Optional. Whether or not the `Target` requires approval.
        """
        return pulumi.get(self, "require_approval")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> str:
        """
        Resource id of the `Target`.
        """
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter
    def uid(self) -> str:
        """
        Unique identifier of the `Target`.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Most recent time at which the `Target` was updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetTargetResult(GetTargetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTargetResult(
            annotations=self.annotations,
            anthos_cluster=self.anthos_cluster,
            create_time=self.create_time,
            description=self.description,
            etag=self.etag,
            execution_configs=self.execution_configs,
            gke=self.gke,
            labels=self.labels,
            name=self.name,
            require_approval=self.require_approval,
            target_id=self.target_id,
            uid=self.uid,
            update_time=self.update_time)


def get_target(location: Optional[str] = None,
               project: Optional[str] = None,
               target_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTargetResult:
    """
    Gets details of a single Target.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['targetId'] = target_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:clouddeploy/v1:getTarget', __args__, opts=opts, typ=GetTargetResult).value

    return AwaitableGetTargetResult(
        annotations=__ret__.annotations,
        anthos_cluster=__ret__.anthos_cluster,
        create_time=__ret__.create_time,
        description=__ret__.description,
        etag=__ret__.etag,
        execution_configs=__ret__.execution_configs,
        gke=__ret__.gke,
        labels=__ret__.labels,
        name=__ret__.name,
        require_approval=__ret__.require_approval,
        target_id=__ret__.target_id,
        uid=__ret__.uid,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_target)
def get_target_output(location: Optional[pulumi.Input[str]] = None,
                      project: Optional[pulumi.Input[Optional[str]]] = None,
                      target_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTargetResult]:
    """
    Gets details of a single Target.
    """
    ...
