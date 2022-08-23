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
    'GetTopicsResult',
    'AwaitableGetTopicsResult',
    'get_topics',
    'get_topics_output',
]

@pulumi.output_type
class GetTopicsResult:
    """
    A collection of values returned by getTopics.
    """
    def __init__(__self__, enable_details=None, id=None, ids=None, instance_id=None, name_regex=None, names=None, output_file=None, tags=None, topics=None):
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
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if topics and not isinstance(topics, list):
            raise TypeError("Expected argument 'topics' to be a list")
        pulumi.set(__self__, "topics", topics)

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
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of topic names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        """
        A map of tags assigned to the Ons instance.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def topics(self) -> Sequence['outputs.GetTopicsTopicResult']:
        """
        A list of topics. Each element contains the following attributes:
        """
        return pulumi.get(self, "topics")


class AwaitableGetTopicsResult(GetTopicsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTopicsResult(
            enable_details=self.enable_details,
            id=self.id,
            ids=self.ids,
            instance_id=self.instance_id,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            tags=self.tags,
            topics=self.topics)


def get_topics(enable_details: Optional[bool] = None,
               ids: Optional[Sequence[str]] = None,
               instance_id: Optional[str] = None,
               name_regex: Optional[str] = None,
               output_file: Optional[str] = None,
               tags: Optional[Mapping[str, Any]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTopicsResult:
    """
    This data source provides a list of ONS Topics in an Alibaba Cloud account according to the specified filters.

    > **NOTE:** Available in 1.53.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    config = pulumi.Config()
    name = config.get("name")
    if name is None:
        name = "onsInstanceName"
    topic = config.get("topic")
    if topic is None:
        topic = "onsTopicDatasourceName"
    default_instance = alicloud.rocketmq.Instance("defaultInstance",
        instance_name=name,
        remark="default_ons_instance_remark")
    default_topic = alicloud.rocketmq.Topic("defaultTopic",
        topic_name=topic,
        instance_id=default_instance.id,
        message_type=0,
        remark="dafault_ons_topic_remark")
    topics_ds = alicloud.rocketmq.get_topics_output(instance_id=default_topic.instance_id,
        name_regex=topic,
        output_file="topics.txt")
    pulumi.export("firstTopicName", topics_ds.topics[0].topic_name)
    ```


    :param Sequence[str] ids: A list of topic IDs to filter results.
    :param str instance_id: ID of the ONS Instance that owns the topics.
    :param str name_regex: A regex string to filter results by the topic name.
    :param Mapping[str, Any] tags: A map of tags assigned to the Ons instance.
    """
    __args__ = dict()
    __args__['enableDetails'] = enable_details
    __args__['ids'] = ids
    __args__['instanceId'] = instance_id
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:rocketmq/getTopics:getTopics', __args__, opts=opts, typ=GetTopicsResult).value

    return AwaitableGetTopicsResult(
        enable_details=__ret__.enable_details,
        id=__ret__.id,
        ids=__ret__.ids,
        instance_id=__ret__.instance_id,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        tags=__ret__.tags,
        topics=__ret__.topics)


@_utilities.lift_output_func(get_topics)
def get_topics_output(enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                      ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                      instance_id: Optional[pulumi.Input[str]] = None,
                      name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                      output_file: Optional[pulumi.Input[Optional[str]]] = None,
                      tags: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTopicsResult]:
    """
    This data source provides a list of ONS Topics in an Alibaba Cloud account according to the specified filters.

    > **NOTE:** Available in 1.53.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    config = pulumi.Config()
    name = config.get("name")
    if name is None:
        name = "onsInstanceName"
    topic = config.get("topic")
    if topic is None:
        topic = "onsTopicDatasourceName"
    default_instance = alicloud.rocketmq.Instance("defaultInstance",
        instance_name=name,
        remark="default_ons_instance_remark")
    default_topic = alicloud.rocketmq.Topic("defaultTopic",
        topic_name=topic,
        instance_id=default_instance.id,
        message_type=0,
        remark="dafault_ons_topic_remark")
    topics_ds = alicloud.rocketmq.get_topics_output(instance_id=default_topic.instance_id,
        name_regex=topic,
        output_file="topics.txt")
    pulumi.export("firstTopicName", topics_ds.topics[0].topic_name)
    ```


    :param Sequence[str] ids: A list of topic IDs to filter results.
    :param str instance_id: ID of the ONS Instance that owns the topics.
    :param str name_regex: A regex string to filter results by the topic name.
    :param Mapping[str, Any] tags: A map of tags assigned to the Ons instance.
    """
    ...
