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
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    def __init__(__self__, cluster_name=None, cluster_uuid=None, config=None, labels=None, metrics=None, project=None, status=None, status_history=None):
        if cluster_name and not isinstance(cluster_name, str):
            raise TypeError("Expected argument 'cluster_name' to be a str")
        pulumi.set(__self__, "cluster_name", cluster_name)
        if cluster_uuid and not isinstance(cluster_uuid, str):
            raise TypeError("Expected argument 'cluster_uuid' to be a str")
        pulumi.set(__self__, "cluster_uuid", cluster_uuid)
        if config and not isinstance(config, dict):
            raise TypeError("Expected argument 'config' to be a dict")
        pulumi.set(__self__, "config", config)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if metrics and not isinstance(metrics, dict):
            raise TypeError("Expected argument 'metrics' to be a dict")
        pulumi.set(__self__, "metrics", metrics)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if status_history and not isinstance(status_history, list):
            raise TypeError("Expected argument 'status_history' to be a list")
        pulumi.set(__self__, "status_history", status_history)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> str:
        """
        The cluster name. Cluster names within a project must be unique. Names of deleted clusters can be reused.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="clusterUuid")
    def cluster_uuid(self) -> str:
        """
        A cluster UUID (Unique Universal Identifier). Dataproc generates this value when it creates the cluster.
        """
        return pulumi.get(self, "cluster_uuid")

    @property
    @pulumi.getter
    def config(self) -> 'outputs.ClusterConfigResponse':
        """
        The cluster config. Note that Dataproc may set default values, and values may change when clusters are updated.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Optional. The labels to associate with this cluster. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a cluster.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def metrics(self) -> 'outputs.ClusterMetricsResponse':
        """
        Contains cluster daemon metrics such as HDFS and YARN stats.Beta Feature: This report is available for testing purposes only. It may be changed before final release.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def project(self) -> str:
        """
        The Google Cloud Platform project ID that the cluster belongs to.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.ClusterStatusResponse':
        """
        Cluster status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusHistory")
    def status_history(self) -> Sequence['outputs.ClusterStatusResponse']:
        """
        The previous cluster status.
        """
        return pulumi.get(self, "status_history")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            cluster_name=self.cluster_name,
            cluster_uuid=self.cluster_uuid,
            config=self.config,
            labels=self.labels,
            metrics=self.metrics,
            project=self.project,
            status=self.status,
            status_history=self.status_history)


def get_cluster(cluster_name: Optional[str] = None,
                project: Optional[str] = None,
                region: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    Gets the resource representation for a cluster in a project.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['project'] = project
    __args__['region'] = region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:dataproc/v1beta2:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        cluster_name=__ret__.cluster_name,
        cluster_uuid=__ret__.cluster_uuid,
        config=__ret__.config,
        labels=__ret__.labels,
        metrics=__ret__.metrics,
        project=__ret__.project,
        status=__ret__.status,
        status_history=__ret__.status_history)


@_utilities.lift_output_func(get_cluster)
def get_cluster_output(cluster_name: Optional[pulumi.Input[str]] = None,
                       project: Optional[pulumi.Input[Optional[str]]] = None,
                       region: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    Gets the resource representation for a cluster in a project.
    """
    ...
