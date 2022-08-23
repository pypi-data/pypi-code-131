# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetTableResult',
    'AwaitableGetTableResult',
    'get_table',
    'get_table_output',
]

@pulumi.output_type
class GetTableResult:
    def __init__(__self__, arn=None, attribute_definitions=None, billing_mode=None, contributor_insights_specification=None, global_secondary_indexes=None, id=None, kinesis_stream_specification=None, point_in_time_recovery_specification=None, provisioned_throughput=None, s_se_specification=None, stream_arn=None, stream_specification=None, table_class=None, tags=None, time_to_live_specification=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if attribute_definitions and not isinstance(attribute_definitions, list):
            raise TypeError("Expected argument 'attribute_definitions' to be a list")
        pulumi.set(__self__, "attribute_definitions", attribute_definitions)
        if billing_mode and not isinstance(billing_mode, str):
            raise TypeError("Expected argument 'billing_mode' to be a str")
        pulumi.set(__self__, "billing_mode", billing_mode)
        if contributor_insights_specification and not isinstance(contributor_insights_specification, dict):
            raise TypeError("Expected argument 'contributor_insights_specification' to be a dict")
        pulumi.set(__self__, "contributor_insights_specification", contributor_insights_specification)
        if global_secondary_indexes and not isinstance(global_secondary_indexes, list):
            raise TypeError("Expected argument 'global_secondary_indexes' to be a list")
        pulumi.set(__self__, "global_secondary_indexes", global_secondary_indexes)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kinesis_stream_specification and not isinstance(kinesis_stream_specification, dict):
            raise TypeError("Expected argument 'kinesis_stream_specification' to be a dict")
        pulumi.set(__self__, "kinesis_stream_specification", kinesis_stream_specification)
        if point_in_time_recovery_specification and not isinstance(point_in_time_recovery_specification, dict):
            raise TypeError("Expected argument 'point_in_time_recovery_specification' to be a dict")
        pulumi.set(__self__, "point_in_time_recovery_specification", point_in_time_recovery_specification)
        if provisioned_throughput and not isinstance(provisioned_throughput, dict):
            raise TypeError("Expected argument 'provisioned_throughput' to be a dict")
        pulumi.set(__self__, "provisioned_throughput", provisioned_throughput)
        if s_se_specification and not isinstance(s_se_specification, dict):
            raise TypeError("Expected argument 's_se_specification' to be a dict")
        pulumi.set(__self__, "s_se_specification", s_se_specification)
        if stream_arn and not isinstance(stream_arn, str):
            raise TypeError("Expected argument 'stream_arn' to be a str")
        pulumi.set(__self__, "stream_arn", stream_arn)
        if stream_specification and not isinstance(stream_specification, dict):
            raise TypeError("Expected argument 'stream_specification' to be a dict")
        pulumi.set(__self__, "stream_specification", stream_specification)
        if table_class and not isinstance(table_class, str):
            raise TypeError("Expected argument 'table_class' to be a str")
        pulumi.set(__self__, "table_class", table_class)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if time_to_live_specification and not isinstance(time_to_live_specification, dict):
            raise TypeError("Expected argument 'time_to_live_specification' to be a dict")
        pulumi.set(__self__, "time_to_live_specification", time_to_live_specification)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="attributeDefinitions")
    def attribute_definitions(self) -> Optional[Sequence['outputs.TableAttributeDefinition']]:
        return pulumi.get(self, "attribute_definitions")

    @property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> Optional[str]:
        return pulumi.get(self, "billing_mode")

    @property
    @pulumi.getter(name="contributorInsightsSpecification")
    def contributor_insights_specification(self) -> Optional['outputs.TableContributorInsightsSpecification']:
        return pulumi.get(self, "contributor_insights_specification")

    @property
    @pulumi.getter(name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> Optional[Sequence['outputs.TableGlobalSecondaryIndex']]:
        return pulumi.get(self, "global_secondary_indexes")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kinesisStreamSpecification")
    def kinesis_stream_specification(self) -> Optional['outputs.TableKinesisStreamSpecification']:
        return pulumi.get(self, "kinesis_stream_specification")

    @property
    @pulumi.getter(name="pointInTimeRecoverySpecification")
    def point_in_time_recovery_specification(self) -> Optional['outputs.TablePointInTimeRecoverySpecification']:
        return pulumi.get(self, "point_in_time_recovery_specification")

    @property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional['outputs.TableProvisionedThroughput']:
        return pulumi.get(self, "provisioned_throughput")

    @property
    @pulumi.getter(name="sSESpecification")
    def s_se_specification(self) -> Optional['outputs.TableSSESpecification']:
        return pulumi.get(self, "s_se_specification")

    @property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> Optional[str]:
        return pulumi.get(self, "stream_arn")

    @property
    @pulumi.getter(name="streamSpecification")
    def stream_specification(self) -> Optional['outputs.TableStreamSpecification']:
        return pulumi.get(self, "stream_specification")

    @property
    @pulumi.getter(name="tableClass")
    def table_class(self) -> Optional[str]:
        return pulumi.get(self, "table_class")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.TableTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeToLiveSpecification")
    def time_to_live_specification(self) -> Optional['outputs.TableTimeToLiveSpecification']:
        return pulumi.get(self, "time_to_live_specification")


class AwaitableGetTableResult(GetTableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTableResult(
            arn=self.arn,
            attribute_definitions=self.attribute_definitions,
            billing_mode=self.billing_mode,
            contributor_insights_specification=self.contributor_insights_specification,
            global_secondary_indexes=self.global_secondary_indexes,
            id=self.id,
            kinesis_stream_specification=self.kinesis_stream_specification,
            point_in_time_recovery_specification=self.point_in_time_recovery_specification,
            provisioned_throughput=self.provisioned_throughput,
            s_se_specification=self.s_se_specification,
            stream_arn=self.stream_arn,
            stream_specification=self.stream_specification,
            table_class=self.table_class,
            tags=self.tags,
            time_to_live_specification=self.time_to_live_specification)


def get_table(id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTableResult:
    """
    Resource Type definition for AWS::DynamoDB::Table
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:dynamodb:getTable', __args__, opts=opts, typ=GetTableResult).value

    return AwaitableGetTableResult(
        arn=__ret__.arn,
        attribute_definitions=__ret__.attribute_definitions,
        billing_mode=__ret__.billing_mode,
        contributor_insights_specification=__ret__.contributor_insights_specification,
        global_secondary_indexes=__ret__.global_secondary_indexes,
        id=__ret__.id,
        kinesis_stream_specification=__ret__.kinesis_stream_specification,
        point_in_time_recovery_specification=__ret__.point_in_time_recovery_specification,
        provisioned_throughput=__ret__.provisioned_throughput,
        s_se_specification=__ret__.s_se_specification,
        stream_arn=__ret__.stream_arn,
        stream_specification=__ret__.stream_specification,
        table_class=__ret__.table_class,
        tags=__ret__.tags,
        time_to_live_specification=__ret__.time_to_live_specification)


@_utilities.lift_output_func(get_table)
def get_table_output(id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTableResult]:
    """
    Resource Type definition for AWS::DynamoDB::Table
    """
    ...
