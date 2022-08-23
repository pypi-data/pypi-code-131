# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetMscSubWebhooksResult',
    'AwaitableGetMscSubWebhooksResult',
    'get_msc_sub_webhooks',
    'get_msc_sub_webhooks_output',
]

@pulumi.output_type
class GetMscSubWebhooksResult:
    """
    A collection of values returned by getMscSubWebhooks.
    """
    def __init__(__self__, id=None, ids=None, name_regex=None, names=None, output_file=None, webhooks=None):
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
        if webhooks and not isinstance(webhooks, list):
            raise TypeError("Expected argument 'webhooks' to be a list")
        pulumi.set(__self__, "webhooks", webhooks)

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
    def webhooks(self) -> Sequence['outputs.GetMscSubWebhooksWebhookResult']:
        return pulumi.get(self, "webhooks")


class AwaitableGetMscSubWebhooksResult(GetMscSubWebhooksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMscSubWebhooksResult(
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            webhooks=self.webhooks)


def get_msc_sub_webhooks(ids: Optional[Sequence[str]] = None,
                         name_regex: Optional[str] = None,
                         output_file: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMscSubWebhooksResult:
    """
    This data source provides the Msc Sub Webhooks of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.141.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.get_msc_sub_webhooks(ids=["example_id"])
    pulumi.export("mscSubWebhookId1", ids.webhooks[0].id)
    name_regex = alicloud.get_msc_sub_webhooks(name_regex="^my-Webhook")
    pulumi.export("mscSubWebhookId2", name_regex.webhooks[0].id)
    ```


    :param Sequence[str] ids: A list of Webhook IDs.
    :param str name_regex: A regex string to filter results by Webhook name.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:index/getMscSubWebhooks:getMscSubWebhooks', __args__, opts=opts, typ=GetMscSubWebhooksResult).value

    return AwaitableGetMscSubWebhooksResult(
        id=__ret__.id,
        ids=__ret__.ids,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        webhooks=__ret__.webhooks)


@_utilities.lift_output_func(get_msc_sub_webhooks)
def get_msc_sub_webhooks_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMscSubWebhooksResult]:
    """
    This data source provides the Msc Sub Webhooks of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.141.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.get_msc_sub_webhooks(ids=["example_id"])
    pulumi.export("mscSubWebhookId1", ids.webhooks[0].id)
    name_regex = alicloud.get_msc_sub_webhooks(name_regex="^my-Webhook")
    pulumi.export("mscSubWebhookId2", name_regex.webhooks[0].id)
    ```


    :param Sequence[str] ids: A list of Webhook IDs.
    :param str name_regex: A regex string to filter results by Webhook name.
    """
    ...
