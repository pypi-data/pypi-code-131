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
    'GetAdConnectorOfficeSitesResult',
    'AwaitableGetAdConnectorOfficeSitesResult',
    'get_ad_connector_office_sites',
    'get_ad_connector_office_sites_output',
]

@pulumi.output_type
class GetAdConnectorOfficeSitesResult:
    """
    A collection of values returned by getAdConnectorOfficeSites.
    """
    def __init__(__self__, id=None, ids=None, name_regex=None, names=None, output_file=None, sites=None, status=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if sites and not isinstance(sites, list):
            raise TypeError("Expected argument 'sites' to be a list")
        pulumi.set(__self__, "sites", sites)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

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
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def sites(self) -> Sequence['outputs.GetAdConnectorOfficeSitesSiteResult']:
        return pulumi.get(self, "sites")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetAdConnectorOfficeSitesResult(GetAdConnectorOfficeSitesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAdConnectorOfficeSitesResult(
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            sites=self.sites,
            status=self.status)


def get_ad_connector_office_sites(ids: Optional[Sequence[str]] = None,
                                  name_regex: Optional[str] = None,
                                  output_file: Optional[str] = None,
                                  status: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAdConnectorOfficeSitesResult:
    """
    This data source provides the Ecd Ad Connector Office Sites of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.176.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.eds.get_ad_connector_office_sites()
    pulumi.export("ecdAdConnectorOfficeSiteId1", ids.sites[0].id)
    name_regex = alicloud.eds.get_ad_connector_office_sites(name_regex="^my-AdConnectorOfficeSite")
    pulumi.export("ecdAdConnectorOfficeSiteId2", name_regex.sites[0].id)
    ```


    :param Sequence[str] ids: A list of Ad Connector Office Site IDs.
    :param str name_regex: A regex string to filter results by Ad Connector Office Site name.
    :param str status: The workspace status.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:eds/getAdConnectorOfficeSites:getAdConnectorOfficeSites', __args__, opts=opts, typ=GetAdConnectorOfficeSitesResult).value

    return AwaitableGetAdConnectorOfficeSitesResult(
        id=__ret__.id,
        ids=__ret__.ids,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        sites=__ret__.sites,
        status=__ret__.status)


@_utilities.lift_output_func(get_ad_connector_office_sites)
def get_ad_connector_office_sites_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                         name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                         output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                         status: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAdConnectorOfficeSitesResult]:
    """
    This data source provides the Ecd Ad Connector Office Sites of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.176.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.eds.get_ad_connector_office_sites()
    pulumi.export("ecdAdConnectorOfficeSiteId1", ids.sites[0].id)
    name_regex = alicloud.eds.get_ad_connector_office_sites(name_regex="^my-AdConnectorOfficeSite")
    pulumi.export("ecdAdConnectorOfficeSiteId2", name_regex.sites[0].id)
    ```


    :param Sequence[str] ids: A list of Ad Connector Office Site IDs.
    :param str name_regex: A regex string to filter results by Ad Connector Office Site name.
    :param str status: The workspace status.
    """
    ...
