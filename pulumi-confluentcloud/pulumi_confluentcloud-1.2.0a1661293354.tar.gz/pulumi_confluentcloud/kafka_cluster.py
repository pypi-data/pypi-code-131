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
from ._inputs import *

__all__ = ['KafkaClusterArgs', 'KafkaCluster']

@pulumi.input_type
class KafkaClusterArgs:
    def __init__(__self__, *,
                 availability: pulumi.Input[str],
                 cloud: pulumi.Input[str],
                 environment: pulumi.Input['KafkaClusterEnvironmentArgs'],
                 region: pulumi.Input[str],
                 basics: Optional[pulumi.Input[Sequence[pulumi.Input['KafkaClusterBasicArgs']]]] = None,
                 dedicated: Optional[pulumi.Input['KafkaClusterDedicatedArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input['KafkaClusterNetworkArgs']] = None,
                 standards: Optional[pulumi.Input[Sequence[pulumi.Input['KafkaClusterStandardArgs']]]] = None):
        """
        The set of arguments for constructing a KafkaCluster resource.
        :param pulumi.Input[str] availability: The availability zone configuration of the Kafka cluster. Accepted values are: `SINGLE_ZONE` and `MULTI_ZONE`.
        :param pulumi.Input[str] cloud: The cloud service provider that runs the Kafka cluster. Accepted values are: `AWS`, `AZURE`, and `GCP`.
        :param pulumi.Input['KafkaClusterEnvironmentArgs'] environment: Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        :param pulumi.Input[str] region: The cloud service provider region where the Kafka cluster is running, for example, `us-west-2`. See [Cloud Providers and Regions](https://docs.confluent.io/cloud/current/clusters/regions.html#cloud-providers-and-regions) for a full list of options for AWS, Azure, and GCP.
        :param pulumi.Input[Sequence[pulumi.Input['KafkaClusterBasicArgs']]] basics: The configuration of the Basic Kafka cluster.
        :param pulumi.Input[str] display_name: The name of the Kafka cluster.
        :param pulumi.Input['KafkaClusterNetworkArgs'] network: Network represents a network (VPC) in Confluent Cloud. All Networks exist within Confluent-managed cloud provider
               accounts.
        :param pulumi.Input[Sequence[pulumi.Input['KafkaClusterStandardArgs']]] standards: The configuration of the Standard Kafka cluster.
        """
        pulumi.set(__self__, "availability", availability)
        pulumi.set(__self__, "cloud", cloud)
        pulumi.set(__self__, "environment", environment)
        pulumi.set(__self__, "region", region)
        if basics is not None:
            pulumi.set(__self__, "basics", basics)
        if dedicated is not None:
            pulumi.set(__self__, "dedicated", dedicated)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if standards is not None:
            pulumi.set(__self__, "standards", standards)

    @property
    @pulumi.getter
    def availability(self) -> pulumi.Input[str]:
        """
        The availability zone configuration of the Kafka cluster. Accepted values are: `SINGLE_ZONE` and `MULTI_ZONE`.
        """
        return pulumi.get(self, "availability")

    @availability.setter
    def availability(self, value: pulumi.Input[str]):
        pulumi.set(self, "availability", value)

    @property
    @pulumi.getter
    def cloud(self) -> pulumi.Input[str]:
        """
        The cloud service provider that runs the Kafka cluster. Accepted values are: `AWS`, `AZURE`, and `GCP`.
        """
        return pulumi.get(self, "cloud")

    @cloud.setter
    def cloud(self, value: pulumi.Input[str]):
        pulumi.set(self, "cloud", value)

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Input['KafkaClusterEnvironmentArgs']:
        """
        Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: pulumi.Input['KafkaClusterEnvironmentArgs']):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        The cloud service provider region where the Kafka cluster is running, for example, `us-west-2`. See [Cloud Providers and Regions](https://docs.confluent.io/cloud/current/clusters/regions.html#cloud-providers-and-regions) for a full list of options for AWS, Azure, and GCP.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def basics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KafkaClusterBasicArgs']]]]:
        """
        The configuration of the Basic Kafka cluster.
        """
        return pulumi.get(self, "basics")

    @basics.setter
    def basics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KafkaClusterBasicArgs']]]]):
        pulumi.set(self, "basics", value)

    @property
    @pulumi.getter
    def dedicated(self) -> Optional[pulumi.Input['KafkaClusterDedicatedArgs']]:
        return pulumi.get(self, "dedicated")

    @dedicated.setter
    def dedicated(self, value: Optional[pulumi.Input['KafkaClusterDedicatedArgs']]):
        pulumi.set(self, "dedicated", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Kafka cluster.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input['KafkaClusterNetworkArgs']]:
        """
        Network represents a network (VPC) in Confluent Cloud. All Networks exist within Confluent-managed cloud provider
        accounts.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input['KafkaClusterNetworkArgs']]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter
    def standards(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KafkaClusterStandardArgs']]]]:
        """
        The configuration of the Standard Kafka cluster.
        """
        return pulumi.get(self, "standards")

    @standards.setter
    def standards(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KafkaClusterStandardArgs']]]]):
        pulumi.set(self, "standards", value)


@pulumi.input_type
class _KafkaClusterState:
    def __init__(__self__, *,
                 api_version: Optional[pulumi.Input[str]] = None,
                 availability: Optional[pulumi.Input[str]] = None,
                 basics: Optional[pulumi.Input[Sequence[pulumi.Input['KafkaClusterBasicArgs']]]] = None,
                 bootstrap_endpoint: Optional[pulumi.Input[str]] = None,
                 cloud: Optional[pulumi.Input[str]] = None,
                 dedicated: Optional[pulumi.Input['KafkaClusterDedicatedArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input['KafkaClusterEnvironmentArgs']] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input['KafkaClusterNetworkArgs']] = None,
                 rbac_crn: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 rest_endpoint: Optional[pulumi.Input[str]] = None,
                 standards: Optional[pulumi.Input[Sequence[pulumi.Input['KafkaClusterStandardArgs']]]] = None):
        """
        Input properties used for looking up and filtering KafkaCluster resources.
        :param pulumi.Input[str] api_version: (Required String) An API Version of the schema version of the Kafka cluster, for example, `cmk/v2`.
        :param pulumi.Input[str] availability: The availability zone configuration of the Kafka cluster. Accepted values are: `SINGLE_ZONE` and `MULTI_ZONE`.
        :param pulumi.Input[Sequence[pulumi.Input['KafkaClusterBasicArgs']]] basics: The configuration of the Basic Kafka cluster.
        :param pulumi.Input[str] bootstrap_endpoint: (Required String) The bootstrap endpoint used by Kafka clients to connect to the Kafka cluster. (e.g., `SASL_SSL://pkc-00000.us-central1.gcp.confluent.cloud:9092`).
        :param pulumi.Input[str] cloud: The cloud service provider that runs the Kafka cluster. Accepted values are: `AWS`, `AZURE`, and `GCP`.
        :param pulumi.Input[str] display_name: The name of the Kafka cluster.
        :param pulumi.Input['KafkaClusterEnvironmentArgs'] environment: Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        :param pulumi.Input[str] kind: (Required String) A kind of the Kafka cluster, for example, `Cluster`.
        :param pulumi.Input['KafkaClusterNetworkArgs'] network: Network represents a network (VPC) in Confluent Cloud. All Networks exist within Confluent-managed cloud provider
               accounts.
        :param pulumi.Input[str] rbac_crn: (Required String) The Confluent Resource Name of the Kafka cluster, for example, `crn://confluent.cloud/organization=1111aaaa-11aa-11aa-11aa-111111aaaaaa/environment=env-abc123/cloud-cluster=lkc-abc123`.
        :param pulumi.Input[str] region: The cloud service provider region where the Kafka cluster is running, for example, `us-west-2`. See [Cloud Providers and Regions](https://docs.confluent.io/cloud/current/clusters/regions.html#cloud-providers-and-regions) for a full list of options for AWS, Azure, and GCP.
        :param pulumi.Input[str] rest_endpoint: (Required String) The REST endpoint of the Kafka cluster (e.g., `https://pkc-00000.us-central1.gcp.confluent.cloud:443`).
        :param pulumi.Input[Sequence[pulumi.Input['KafkaClusterStandardArgs']]] standards: The configuration of the Standard Kafka cluster.
        """
        if api_version is not None:
            pulumi.set(__self__, "api_version", api_version)
        if availability is not None:
            pulumi.set(__self__, "availability", availability)
        if basics is not None:
            pulumi.set(__self__, "basics", basics)
        if bootstrap_endpoint is not None:
            pulumi.set(__self__, "bootstrap_endpoint", bootstrap_endpoint)
        if cloud is not None:
            pulumi.set(__self__, "cloud", cloud)
        if dedicated is not None:
            pulumi.set(__self__, "dedicated", dedicated)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if rbac_crn is not None:
            pulumi.set(__self__, "rbac_crn", rbac_crn)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if rest_endpoint is not None:
            pulumi.set(__self__, "rest_endpoint", rest_endpoint)
        if standards is not None:
            pulumi.set(__self__, "standards", standards)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        (Required String) An API Version of the schema version of the Kafka cluster, for example, `cmk/v2`.
        """
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter
    def availability(self) -> Optional[pulumi.Input[str]]:
        """
        The availability zone configuration of the Kafka cluster. Accepted values are: `SINGLE_ZONE` and `MULTI_ZONE`.
        """
        return pulumi.get(self, "availability")

    @availability.setter
    def availability(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability", value)

    @property
    @pulumi.getter
    def basics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KafkaClusterBasicArgs']]]]:
        """
        The configuration of the Basic Kafka cluster.
        """
        return pulumi.get(self, "basics")

    @basics.setter
    def basics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KafkaClusterBasicArgs']]]]):
        pulumi.set(self, "basics", value)

    @property
    @pulumi.getter(name="bootstrapEndpoint")
    def bootstrap_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        (Required String) The bootstrap endpoint used by Kafka clients to connect to the Kafka cluster. (e.g., `SASL_SSL://pkc-00000.us-central1.gcp.confluent.cloud:9092`).
        """
        return pulumi.get(self, "bootstrap_endpoint")

    @bootstrap_endpoint.setter
    def bootstrap_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bootstrap_endpoint", value)

    @property
    @pulumi.getter
    def cloud(self) -> Optional[pulumi.Input[str]]:
        """
        The cloud service provider that runs the Kafka cluster. Accepted values are: `AWS`, `AZURE`, and `GCP`.
        """
        return pulumi.get(self, "cloud")

    @cloud.setter
    def cloud(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud", value)

    @property
    @pulumi.getter
    def dedicated(self) -> Optional[pulumi.Input['KafkaClusterDedicatedArgs']]:
        return pulumi.get(self, "dedicated")

    @dedicated.setter
    def dedicated(self, value: Optional[pulumi.Input['KafkaClusterDedicatedArgs']]):
        pulumi.set(self, "dedicated", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Kafka cluster.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input['KafkaClusterEnvironmentArgs']]:
        """
        Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input['KafkaClusterEnvironmentArgs']]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        (Required String) A kind of the Kafka cluster, for example, `Cluster`.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input['KafkaClusterNetworkArgs']]:
        """
        Network represents a network (VPC) in Confluent Cloud. All Networks exist within Confluent-managed cloud provider
        accounts.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input['KafkaClusterNetworkArgs']]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter(name="rbacCrn")
    def rbac_crn(self) -> Optional[pulumi.Input[str]]:
        """
        (Required String) The Confluent Resource Name of the Kafka cluster, for example, `crn://confluent.cloud/organization=1111aaaa-11aa-11aa-11aa-111111aaaaaa/environment=env-abc123/cloud-cluster=lkc-abc123`.
        """
        return pulumi.get(self, "rbac_crn")

    @rbac_crn.setter
    def rbac_crn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rbac_crn", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The cloud service provider region where the Kafka cluster is running, for example, `us-west-2`. See [Cloud Providers and Regions](https://docs.confluent.io/cloud/current/clusters/regions.html#cloud-providers-and-regions) for a full list of options for AWS, Azure, and GCP.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="restEndpoint")
    def rest_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        (Required String) The REST endpoint of the Kafka cluster (e.g., `https://pkc-00000.us-central1.gcp.confluent.cloud:443`).
        """
        return pulumi.get(self, "rest_endpoint")

    @rest_endpoint.setter
    def rest_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rest_endpoint", value)

    @property
    @pulumi.getter
    def standards(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KafkaClusterStandardArgs']]]]:
        """
        The configuration of the Standard Kafka cluster.
        """
        return pulumi.get(self, "standards")

    @standards.setter
    def standards(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KafkaClusterStandardArgs']]]]):
        pulumi.set(self, "standards", value)


class KafkaCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability: Optional[pulumi.Input[str]] = None,
                 basics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KafkaClusterBasicArgs']]]]] = None,
                 cloud: Optional[pulumi.Input[str]] = None,
                 dedicated: Optional[pulumi.Input[pulumi.InputType['KafkaClusterDedicatedArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[pulumi.InputType['KafkaClusterEnvironmentArgs']]] = None,
                 network: Optional[pulumi.Input[pulumi.InputType['KafkaClusterNetworkArgs']]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 standards: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KafkaClusterStandardArgs']]]]] = None,
                 __props__=None):
        """
        ## Import

        You can import a Kafka cluster by using Environment ID and Kafka cluster ID, in the format `<Environment ID>/<Kafka cluster ID>`, e.g. $ export CONFLUENT_CLOUD_API_KEY="<cloud_api_key>" $ export CONFLUENT_CLOUD_API_SECRET="<cloud_api_secret>"

        ```sh
         $ pulumi import confluentcloud:index/kafkaCluster:KafkaCluster my_kafka env-abc123/lkc-abc123
        ```

         !> **Warning:** Do not forget to delete terminal command history afterwards for security purposes.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability: The availability zone configuration of the Kafka cluster. Accepted values are: `SINGLE_ZONE` and `MULTI_ZONE`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KafkaClusterBasicArgs']]]] basics: The configuration of the Basic Kafka cluster.
        :param pulumi.Input[str] cloud: The cloud service provider that runs the Kafka cluster. Accepted values are: `AWS`, `AZURE`, and `GCP`.
        :param pulumi.Input[str] display_name: The name of the Kafka cluster.
        :param pulumi.Input[pulumi.InputType['KafkaClusterEnvironmentArgs']] environment: Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        :param pulumi.Input[pulumi.InputType['KafkaClusterNetworkArgs']] network: Network represents a network (VPC) in Confluent Cloud. All Networks exist within Confluent-managed cloud provider
               accounts.
        :param pulumi.Input[str] region: The cloud service provider region where the Kafka cluster is running, for example, `us-west-2`. See [Cloud Providers and Regions](https://docs.confluent.io/cloud/current/clusters/regions.html#cloud-providers-and-regions) for a full list of options for AWS, Azure, and GCP.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KafkaClusterStandardArgs']]]] standards: The configuration of the Standard Kafka cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KafkaClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        You can import a Kafka cluster by using Environment ID and Kafka cluster ID, in the format `<Environment ID>/<Kafka cluster ID>`, e.g. $ export CONFLUENT_CLOUD_API_KEY="<cloud_api_key>" $ export CONFLUENT_CLOUD_API_SECRET="<cloud_api_secret>"

        ```sh
         $ pulumi import confluentcloud:index/kafkaCluster:KafkaCluster my_kafka env-abc123/lkc-abc123
        ```

         !> **Warning:** Do not forget to delete terminal command history afterwards for security purposes.

        :param str resource_name: The name of the resource.
        :param KafkaClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KafkaClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability: Optional[pulumi.Input[str]] = None,
                 basics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KafkaClusterBasicArgs']]]]] = None,
                 cloud: Optional[pulumi.Input[str]] = None,
                 dedicated: Optional[pulumi.Input[pulumi.InputType['KafkaClusterDedicatedArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[pulumi.InputType['KafkaClusterEnvironmentArgs']]] = None,
                 network: Optional[pulumi.Input[pulumi.InputType['KafkaClusterNetworkArgs']]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 standards: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KafkaClusterStandardArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KafkaClusterArgs.__new__(KafkaClusterArgs)

            if availability is None and not opts.urn:
                raise TypeError("Missing required property 'availability'")
            __props__.__dict__["availability"] = availability
            __props__.__dict__["basics"] = basics
            if cloud is None and not opts.urn:
                raise TypeError("Missing required property 'cloud'")
            __props__.__dict__["cloud"] = cloud
            __props__.__dict__["dedicated"] = dedicated
            __props__.__dict__["display_name"] = display_name
            if environment is None and not opts.urn:
                raise TypeError("Missing required property 'environment'")
            __props__.__dict__["environment"] = environment
            __props__.__dict__["network"] = network
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["standards"] = standards
            __props__.__dict__["api_version"] = None
            __props__.__dict__["bootstrap_endpoint"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["rbac_crn"] = None
            __props__.__dict__["rest_endpoint"] = None
        super(KafkaCluster, __self__).__init__(
            'confluentcloud:index/kafkaCluster:KafkaCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_version: Optional[pulumi.Input[str]] = None,
            availability: Optional[pulumi.Input[str]] = None,
            basics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KafkaClusterBasicArgs']]]]] = None,
            bootstrap_endpoint: Optional[pulumi.Input[str]] = None,
            cloud: Optional[pulumi.Input[str]] = None,
            dedicated: Optional[pulumi.Input[pulumi.InputType['KafkaClusterDedicatedArgs']]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            environment: Optional[pulumi.Input[pulumi.InputType['KafkaClusterEnvironmentArgs']]] = None,
            kind: Optional[pulumi.Input[str]] = None,
            network: Optional[pulumi.Input[pulumi.InputType['KafkaClusterNetworkArgs']]] = None,
            rbac_crn: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            rest_endpoint: Optional[pulumi.Input[str]] = None,
            standards: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KafkaClusterStandardArgs']]]]] = None) -> 'KafkaCluster':
        """
        Get an existing KafkaCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_version: (Required String) An API Version of the schema version of the Kafka cluster, for example, `cmk/v2`.
        :param pulumi.Input[str] availability: The availability zone configuration of the Kafka cluster. Accepted values are: `SINGLE_ZONE` and `MULTI_ZONE`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KafkaClusterBasicArgs']]]] basics: The configuration of the Basic Kafka cluster.
        :param pulumi.Input[str] bootstrap_endpoint: (Required String) The bootstrap endpoint used by Kafka clients to connect to the Kafka cluster. (e.g., `SASL_SSL://pkc-00000.us-central1.gcp.confluent.cloud:9092`).
        :param pulumi.Input[str] cloud: The cloud service provider that runs the Kafka cluster. Accepted values are: `AWS`, `AZURE`, and `GCP`.
        :param pulumi.Input[str] display_name: The name of the Kafka cluster.
        :param pulumi.Input[pulumi.InputType['KafkaClusterEnvironmentArgs']] environment: Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        :param pulumi.Input[str] kind: (Required String) A kind of the Kafka cluster, for example, `Cluster`.
        :param pulumi.Input[pulumi.InputType['KafkaClusterNetworkArgs']] network: Network represents a network (VPC) in Confluent Cloud. All Networks exist within Confluent-managed cloud provider
               accounts.
        :param pulumi.Input[str] rbac_crn: (Required String) The Confluent Resource Name of the Kafka cluster, for example, `crn://confluent.cloud/organization=1111aaaa-11aa-11aa-11aa-111111aaaaaa/environment=env-abc123/cloud-cluster=lkc-abc123`.
        :param pulumi.Input[str] region: The cloud service provider region where the Kafka cluster is running, for example, `us-west-2`. See [Cloud Providers and Regions](https://docs.confluent.io/cloud/current/clusters/regions.html#cloud-providers-and-regions) for a full list of options for AWS, Azure, and GCP.
        :param pulumi.Input[str] rest_endpoint: (Required String) The REST endpoint of the Kafka cluster (e.g., `https://pkc-00000.us-central1.gcp.confluent.cloud:443`).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KafkaClusterStandardArgs']]]] standards: The configuration of the Standard Kafka cluster.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KafkaClusterState.__new__(_KafkaClusterState)

        __props__.__dict__["api_version"] = api_version
        __props__.__dict__["availability"] = availability
        __props__.__dict__["basics"] = basics
        __props__.__dict__["bootstrap_endpoint"] = bootstrap_endpoint
        __props__.__dict__["cloud"] = cloud
        __props__.__dict__["dedicated"] = dedicated
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["environment"] = environment
        __props__.__dict__["kind"] = kind
        __props__.__dict__["network"] = network
        __props__.__dict__["rbac_crn"] = rbac_crn
        __props__.__dict__["region"] = region
        __props__.__dict__["rest_endpoint"] = rest_endpoint
        __props__.__dict__["standards"] = standards
        return KafkaCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[str]:
        """
        (Required String) An API Version of the schema version of the Kafka cluster, for example, `cmk/v2`.
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def availability(self) -> pulumi.Output[str]:
        """
        The availability zone configuration of the Kafka cluster. Accepted values are: `SINGLE_ZONE` and `MULTI_ZONE`.
        """
        return pulumi.get(self, "availability")

    @property
    @pulumi.getter
    def basics(self) -> pulumi.Output[Optional[Sequence['outputs.KafkaClusterBasic']]]:
        """
        The configuration of the Basic Kafka cluster.
        """
        return pulumi.get(self, "basics")

    @property
    @pulumi.getter(name="bootstrapEndpoint")
    def bootstrap_endpoint(self) -> pulumi.Output[str]:
        """
        (Required String) The bootstrap endpoint used by Kafka clients to connect to the Kafka cluster. (e.g., `SASL_SSL://pkc-00000.us-central1.gcp.confluent.cloud:9092`).
        """
        return pulumi.get(self, "bootstrap_endpoint")

    @property
    @pulumi.getter
    def cloud(self) -> pulumi.Output[str]:
        """
        The cloud service provider that runs the Kafka cluster. Accepted values are: `AWS`, `AZURE`, and `GCP`.
        """
        return pulumi.get(self, "cloud")

    @property
    @pulumi.getter
    def dedicated(self) -> pulumi.Output[Optional['outputs.KafkaClusterDedicated']]:
        return pulumi.get(self, "dedicated")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The name of the Kafka cluster.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output['outputs.KafkaClusterEnvironment']:
        """
        Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        (Required String) A kind of the Kafka cluster, for example, `Cluster`.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output['outputs.KafkaClusterNetwork']:
        """
        Network represents a network (VPC) in Confluent Cloud. All Networks exist within Confluent-managed cloud provider
        accounts.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="rbacCrn")
    def rbac_crn(self) -> pulumi.Output[str]:
        """
        (Required String) The Confluent Resource Name of the Kafka cluster, for example, `crn://confluent.cloud/organization=1111aaaa-11aa-11aa-11aa-111111aaaaaa/environment=env-abc123/cloud-cluster=lkc-abc123`.
        """
        return pulumi.get(self, "rbac_crn")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The cloud service provider region where the Kafka cluster is running, for example, `us-west-2`. See [Cloud Providers and Regions](https://docs.confluent.io/cloud/current/clusters/regions.html#cloud-providers-and-regions) for a full list of options for AWS, Azure, and GCP.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="restEndpoint")
    def rest_endpoint(self) -> pulumi.Output[str]:
        """
        (Required String) The REST endpoint of the Kafka cluster (e.g., `https://pkc-00000.us-central1.gcp.confluent.cloud:443`).
        """
        return pulumi.get(self, "rest_endpoint")

    @property
    @pulumi.getter
    def standards(self) -> pulumi.Output[Optional[Sequence['outputs.KafkaClusterStandard']]]:
        """
        The configuration of the Standard Kafka cluster.
        """
        return pulumi.get(self, "standards")

