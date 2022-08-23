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
    'GetAccountsResult',
    'AwaitableGetAccountsResult',
    'get_accounts',
    'get_accounts_output',
]

@pulumi.output_type
class GetAccountsResult:
    """
    A collection of values returned by getAccounts.
    """
    def __init__(__self__, accounts=None, db_cluster_id=None, id=None, name_regex=None, names=None):
        if accounts and not isinstance(accounts, list):
            raise TypeError("Expected argument 'accounts' to be a list")
        pulumi.set(__self__, "accounts", accounts)
        if db_cluster_id and not isinstance(db_cluster_id, str):
            raise TypeError("Expected argument 'db_cluster_id' to be a str")
        pulumi.set(__self__, "db_cluster_id", db_cluster_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)

    @property
    @pulumi.getter
    def accounts(self) -> Sequence['outputs.GetAccountsAccountResult']:
        """
        A list of PolarDB cluster accounts. Each element contains the following attributes:
        """
        return pulumi.get(self, "accounts")

    @property
    @pulumi.getter(name="dbClusterId")
    def db_cluster_id(self) -> str:
        return pulumi.get(self, "db_cluster_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        Account name of the cluster.
        """
        return pulumi.get(self, "names")


class AwaitableGetAccountsResult(GetAccountsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountsResult(
            accounts=self.accounts,
            db_cluster_id=self.db_cluster_id,
            id=self.id,
            name_regex=self.name_regex,
            names=self.names)


def get_accounts(db_cluster_id: Optional[str] = None,
                 name_regex: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountsResult:
    """
    The `polardb.get_accounts` data source provides a collection of PolarDB cluster database account available in Alibaba Cloud account.
    Filters support regular expression for the account name, searches by clusterId.

    > **NOTE:** Available in v1.70.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    polardb_clusters_ds = alicloud.polardb.get_clusters(description_regex="pc-\\\\w+",
        status="Running")
    default = alicloud.polardb.get_accounts(db_cluster_id=polardb_clusters_ds.clusters[0].id)
    pulumi.export("account", default.accounts[0].account_name)
    ```


    :param str db_cluster_id: The polarDB cluster ID.
    :param str name_regex: A regex string to filter results by account name.
    """
    __args__ = dict()
    __args__['dbClusterId'] = db_cluster_id
    __args__['nameRegex'] = name_regex
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:polardb/getAccounts:getAccounts', __args__, opts=opts, typ=GetAccountsResult).value

    return AwaitableGetAccountsResult(
        accounts=__ret__.accounts,
        db_cluster_id=__ret__.db_cluster_id,
        id=__ret__.id,
        name_regex=__ret__.name_regex,
        names=__ret__.names)


@_utilities.lift_output_func(get_accounts)
def get_accounts_output(db_cluster_id: Optional[pulumi.Input[str]] = None,
                        name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountsResult]:
    """
    The `polardb.get_accounts` data source provides a collection of PolarDB cluster database account available in Alibaba Cloud account.
    Filters support regular expression for the account name, searches by clusterId.

    > **NOTE:** Available in v1.70.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    polardb_clusters_ds = alicloud.polardb.get_clusters(description_regex="pc-\\\\w+",
        status="Running")
    default = alicloud.polardb.get_accounts(db_cluster_id=polardb_clusters_ds.clusters[0].id)
    pulumi.export("account", default.accounts[0].account_name)
    ```


    :param str db_cluster_id: The polarDB cluster ID.
    :param str name_regex: A regex string to filter results by account name.
    """
    ...
