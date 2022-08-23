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
    'GetRegistryEnterpriseReposResult',
    'AwaitableGetRegistryEnterpriseReposResult',
    'get_registry_enterprise_repos',
    'get_registry_enterprise_repos_output',
]

@pulumi.output_type
class GetRegistryEnterpriseReposResult:
    """
    A collection of values returned by getRegistryEnterpriseRepos.
    """
    def __init__(__self__, enable_details=None, id=None, ids=None, instance_id=None, name_regex=None, names=None, namespace=None, output_file=None, repos=None):
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if repos and not isinstance(repos, list):
            raise TypeError("Expected argument 'repos' to be a list")
        pulumi.set(__self__, "repos", repos)

    @property
    @pulumi.getter(name="enableDetails")
    def enable_details(self) -> Optional[bool]:
        return pulumi.get(self, "enable_details")

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
        A list of matched Container Registry Enterprise Edition repositories. Its element is a repository id.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        """
        ID of Container Registry Enterprise Edition instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of repository names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        Name of Container Registry Enterprise Edition namespace where repo is located.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def repos(self) -> Sequence['outputs.GetRegistryEnterpriseReposRepoResult']:
        """
        A list of matched Container Registry Enterprise Edition namespaces. Each element contains the following attributes:
        """
        return pulumi.get(self, "repos")


class AwaitableGetRegistryEnterpriseReposResult(GetRegistryEnterpriseReposResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegistryEnterpriseReposResult(
            enable_details=self.enable_details,
            id=self.id,
            ids=self.ids,
            instance_id=self.instance_id,
            name_regex=self.name_regex,
            names=self.names,
            namespace=self.namespace,
            output_file=self.output_file,
            repos=self.repos)


def get_registry_enterprise_repos(enable_details: Optional[bool] = None,
                                  ids: Optional[Sequence[str]] = None,
                                  instance_id: Optional[str] = None,
                                  name_regex: Optional[str] = None,
                                  namespace: Optional[str] = None,
                                  output_file: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegistryEnterpriseReposResult:
    """
    This data source provides a list Container Registry Enterprise Edition repositories on Alibaba Cloud.

    > **NOTE:** Available in v1.87.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    my_repos = alicloud.cs.get_registry_enterprise_repos(instance_id="cri-xx",
        name_regex="my-repos",
        output_file="my-repo-json")
    pulumi.export("output", my_repos.repos)
    ```


    :param bool enable_details: Boolean, false by default, only repository attributes are exported. Set to true if tags belong to this repository are needed. See `tags` in attributes.
    :param Sequence[str] ids: A list of ids to filter results by repository id.
    :param str instance_id: ID of Container Registry Enterprise Edition instance.
    :param str name_regex: A regex string to filter results by repository name.
    :param str namespace: Name of Container Registry Enterprise Edition namespace where the repositories are located in.
    """
    __args__ = dict()
    __args__['enableDetails'] = enable_details
    __args__['ids'] = ids
    __args__['instanceId'] = instance_id
    __args__['nameRegex'] = name_regex
    __args__['namespace'] = namespace
    __args__['outputFile'] = output_file
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:cs/getRegistryEnterpriseRepos:getRegistryEnterpriseRepos', __args__, opts=opts, typ=GetRegistryEnterpriseReposResult).value

    return AwaitableGetRegistryEnterpriseReposResult(
        enable_details=__ret__.enable_details,
        id=__ret__.id,
        ids=__ret__.ids,
        instance_id=__ret__.instance_id,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        namespace=__ret__.namespace,
        output_file=__ret__.output_file,
        repos=__ret__.repos)


@_utilities.lift_output_func(get_registry_enterprise_repos)
def get_registry_enterprise_repos_output(enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                                         ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                         instance_id: Optional[pulumi.Input[str]] = None,
                                         name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                         namespace: Optional[pulumi.Input[Optional[str]]] = None,
                                         output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRegistryEnterpriseReposResult]:
    """
    This data source provides a list Container Registry Enterprise Edition repositories on Alibaba Cloud.

    > **NOTE:** Available in v1.87.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    my_repos = alicloud.cs.get_registry_enterprise_repos(instance_id="cri-xx",
        name_regex="my-repos",
        output_file="my-repo-json")
    pulumi.export("output", my_repos.repos)
    ```


    :param bool enable_details: Boolean, false by default, only repository attributes are exported. Set to true if tags belong to this repository are needed. See `tags` in attributes.
    :param Sequence[str] ids: A list of ids to filter results by repository id.
    :param str instance_id: ID of Container Registry Enterprise Edition instance.
    :param str name_regex: A regex string to filter results by repository name.
    :param str namespace: Name of Container Registry Enterprise Edition namespace where the repositories are located in.
    """
    ...
