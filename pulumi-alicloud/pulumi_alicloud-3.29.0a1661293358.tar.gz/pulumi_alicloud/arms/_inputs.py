# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DispatchRuleGroupRuleArgs',
    'DispatchRuleLabelMatchExpressionGridArgs',
    'DispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupArgs',
    'DispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupLabelMatchExpressionArgs',
    'DispatchRuleNotifyRuleArgs',
    'DispatchRuleNotifyRuleNotifyObjectArgs',
    'PrometheusAlertRuleAnnotationArgs',
    'PrometheusAlertRuleLabelArgs',
]

@pulumi.input_type
class DispatchRuleGroupRuleArgs:
    def __init__(__self__, *,
                 group_interval: pulumi.Input[int],
                 group_wait_time: pulumi.Input[int],
                 grouping_fields: pulumi.Input[Sequence[pulumi.Input[str]]],
                 group_id: Optional[pulumi.Input[int]] = None,
                 repeat_interval: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] group_interval: The duration for which the system waits after the first alert is sent. After the duration, all alerts are sent in a single notification to the handler.
        :param pulumi.Input[int] group_wait_time: The duration for which the system waits after the first alert is sent. After the duration, all alerts are sent in a single notification to the handler.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] grouping_fields: The fields that are used to group events. Events with the same field content are assigned to a group. Alerts with the same specified grouping field are sent to the handler in separate notifications.
        :param pulumi.Input[int] repeat_interval: The silence period of repeated alerts. All alerts are repeatedly sent at specified intervals until the alerts are cleared. The minimum value is 61. Default to 600.
        """
        pulumi.set(__self__, "group_interval", group_interval)
        pulumi.set(__self__, "group_wait_time", group_wait_time)
        pulumi.set(__self__, "grouping_fields", grouping_fields)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if repeat_interval is not None:
            pulumi.set(__self__, "repeat_interval", repeat_interval)

    @property
    @pulumi.getter(name="groupInterval")
    def group_interval(self) -> pulumi.Input[int]:
        """
        The duration for which the system waits after the first alert is sent. After the duration, all alerts are sent in a single notification to the handler.
        """
        return pulumi.get(self, "group_interval")

    @group_interval.setter
    def group_interval(self, value: pulumi.Input[int]):
        pulumi.set(self, "group_interval", value)

    @property
    @pulumi.getter(name="groupWaitTime")
    def group_wait_time(self) -> pulumi.Input[int]:
        """
        The duration for which the system waits after the first alert is sent. After the duration, all alerts are sent in a single notification to the handler.
        """
        return pulumi.get(self, "group_wait_time")

    @group_wait_time.setter
    def group_wait_time(self, value: pulumi.Input[int]):
        pulumi.set(self, "group_wait_time", value)

    @property
    @pulumi.getter(name="groupingFields")
    def grouping_fields(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The fields that are used to group events. Events with the same field content are assigned to a group. Alerts with the same specified grouping field are sent to the handler in separate notifications.
        """
        return pulumi.get(self, "grouping_fields")

    @grouping_fields.setter
    def grouping_fields(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "grouping_fields", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="repeatInterval")
    def repeat_interval(self) -> Optional[pulumi.Input[int]]:
        """
        The silence period of repeated alerts. All alerts are repeatedly sent at specified intervals until the alerts are cleared. The minimum value is 61. Default to 600.
        """
        return pulumi.get(self, "repeat_interval")

    @repeat_interval.setter
    def repeat_interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "repeat_interval", value)


@pulumi.input_type
class DispatchRuleLabelMatchExpressionGridArgs:
    def __init__(__self__, *,
                 label_match_expression_groups: pulumi.Input[Sequence[pulumi.Input['DispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupArgs']]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input['DispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupArgs']]] label_match_expression_groups: Sets the dispatch rule. See the following `Block label_match_expression_groups`.
        """
        pulumi.set(__self__, "label_match_expression_groups", label_match_expression_groups)

    @property
    @pulumi.getter(name="labelMatchExpressionGroups")
    def label_match_expression_groups(self) -> pulumi.Input[Sequence[pulumi.Input['DispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupArgs']]]:
        """
        Sets the dispatch rule. See the following `Block label_match_expression_groups`.
        """
        return pulumi.get(self, "label_match_expression_groups")

    @label_match_expression_groups.setter
    def label_match_expression_groups(self, value: pulumi.Input[Sequence[pulumi.Input['DispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupArgs']]]):
        pulumi.set(self, "label_match_expression_groups", value)


@pulumi.input_type
class DispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupArgs:
    def __init__(__self__, *,
                 label_match_expressions: pulumi.Input[Sequence[pulumi.Input['DispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupLabelMatchExpressionArgs']]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input['DispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupLabelMatchExpressionArgs']]] label_match_expressions: Sets the dispatch rule. See the following `Block label_match_expressions`.
        """
        pulumi.set(__self__, "label_match_expressions", label_match_expressions)

    @property
    @pulumi.getter(name="labelMatchExpressions")
    def label_match_expressions(self) -> pulumi.Input[Sequence[pulumi.Input['DispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupLabelMatchExpressionArgs']]]:
        """
        Sets the dispatch rule. See the following `Block label_match_expressions`.
        """
        return pulumi.get(self, "label_match_expressions")

    @label_match_expressions.setter
    def label_match_expressions(self, value: pulumi.Input[Sequence[pulumi.Input['DispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupLabelMatchExpressionArgs']]]):
        pulumi.set(self, "label_match_expressions", value)


@pulumi.input_type
class DispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupLabelMatchExpressionArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 operator: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] key: The key of the tag of the dispatch rule. Valud values:
               * _aliyun_arms_userid: user ID
               * _aliyun_arms_involvedObject_kind: type of the associated object
               * _aliyun_arms_involvedObject_id: ID of the associated object
               * _aliyun_arms_involvedObject_name: name of the associated object
               * _aliyun_arms_alert_name: alert name
               * _aliyun_arms_alert_rule_id: alert rule ID
               * _aliyun_arms_alert_type: alert type
               * _aliyun_arms_alert_level: alert severity
        :param pulumi.Input[str] operator: The operator used in the dispatch rule. Valid values: 
               * eq: equals to.
               * re: matches a regular expression.
        :param pulumi.Input[str] value: The value of the tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key of the tag of the dispatch rule. Valud values:
        * _aliyun_arms_userid: user ID
        * _aliyun_arms_involvedObject_kind: type of the associated object
        * _aliyun_arms_involvedObject_id: ID of the associated object
        * _aliyun_arms_involvedObject_name: name of the associated object
        * _aliyun_arms_alert_name: alert name
        * _aliyun_arms_alert_rule_id: alert rule ID
        * _aliyun_arms_alert_type: alert type
        * _aliyun_arms_alert_level: alert severity
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def operator(self) -> pulumi.Input[str]:
        """
        The operator used in the dispatch rule. Valid values: 
        * eq: equals to.
        * re: matches a regular expression.
        """
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: pulumi.Input[str]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the tag.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class DispatchRuleNotifyRuleArgs:
    def __init__(__self__, *,
                 notify_channels: pulumi.Input[Sequence[pulumi.Input[str]]],
                 notify_objects: pulumi.Input[Sequence[pulumi.Input['DispatchRuleNotifyRuleNotifyObjectArgs']]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] notify_channels: The notification method. Valid values: dingTalk, sms, webhook, email, and wechat.
        :param pulumi.Input[Sequence[pulumi.Input['DispatchRuleNotifyRuleNotifyObjectArgs']]] notify_objects: Sets the notification object. See the following `Block notify_objects`.
        """
        pulumi.set(__self__, "notify_channels", notify_channels)
        pulumi.set(__self__, "notify_objects", notify_objects)

    @property
    @pulumi.getter(name="notifyChannels")
    def notify_channels(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The notification method. Valid values: dingTalk, sms, webhook, email, and wechat.
        """
        return pulumi.get(self, "notify_channels")

    @notify_channels.setter
    def notify_channels(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "notify_channels", value)

    @property
    @pulumi.getter(name="notifyObjects")
    def notify_objects(self) -> pulumi.Input[Sequence[pulumi.Input['DispatchRuleNotifyRuleNotifyObjectArgs']]]:
        """
        Sets the notification object. See the following `Block notify_objects`.
        """
        return pulumi.get(self, "notify_objects")

    @notify_objects.setter
    def notify_objects(self, value: pulumi.Input[Sequence[pulumi.Input['DispatchRuleNotifyRuleNotifyObjectArgs']]]):
        pulumi.set(self, "notify_objects", value)


@pulumi.input_type
class DispatchRuleNotifyRuleNotifyObjectArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 notify_object_id: pulumi.Input[str],
                 notify_type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The name of the contact or contact group.
        :param pulumi.Input[str] notify_object_id: The ID of the contact or contact group.
        :param pulumi.Input[str] notify_type: The type of the alert contact. Valid values: ARMS_CONTACT: contact. ARMS_CONTACT_GROUP: contact group.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "notify_object_id", notify_object_id)
        pulumi.set(__self__, "notify_type", notify_type)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the contact or contact group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notifyObjectId")
    def notify_object_id(self) -> pulumi.Input[str]:
        """
        The ID of the contact or contact group.
        """
        return pulumi.get(self, "notify_object_id")

    @notify_object_id.setter
    def notify_object_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "notify_object_id", value)

    @property
    @pulumi.getter(name="notifyType")
    def notify_type(self) -> pulumi.Input[str]:
        """
        The type of the alert contact. Valid values: ARMS_CONTACT: contact. ARMS_CONTACT_GROUP: contact group.
        """
        return pulumi.get(self, "notify_type")

    @notify_type.setter
    def notify_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "notify_type", value)


@pulumi.input_type
class PrometheusAlertRuleAnnotationArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: The name of the annotation.
        :param pulumi.Input[str] value: The value of the annotation.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the annotation.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the annotation.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class PrometheusAlertRuleLabelArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: The name of the annotation.
        :param pulumi.Input[str] value: The value of the annotation.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the annotation.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the annotation.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


