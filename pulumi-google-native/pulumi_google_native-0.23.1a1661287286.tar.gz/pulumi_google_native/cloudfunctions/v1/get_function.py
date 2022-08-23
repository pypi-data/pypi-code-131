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
    'GetFunctionResult',
    'AwaitableGetFunctionResult',
    'get_function',
    'get_function_output',
]

@pulumi.output_type
class GetFunctionResult:
    def __init__(__self__, available_memory_mb=None, build_environment_variables=None, build_id=None, build_name=None, build_worker_pool=None, description=None, docker_registry=None, docker_repository=None, entry_point=None, environment_variables=None, event_trigger=None, https_trigger=None, ingress_settings=None, kms_key_name=None, labels=None, max_instances=None, min_instances=None, name=None, network=None, runtime=None, secret_environment_variables=None, secret_volumes=None, service_account_email=None, source_archive_url=None, source_repository=None, source_token=None, source_upload_url=None, status=None, timeout=None, update_time=None, version_id=None, vpc_connector=None, vpc_connector_egress_settings=None):
        if available_memory_mb and not isinstance(available_memory_mb, int):
            raise TypeError("Expected argument 'available_memory_mb' to be a int")
        pulumi.set(__self__, "available_memory_mb", available_memory_mb)
        if build_environment_variables and not isinstance(build_environment_variables, dict):
            raise TypeError("Expected argument 'build_environment_variables' to be a dict")
        pulumi.set(__self__, "build_environment_variables", build_environment_variables)
        if build_id and not isinstance(build_id, str):
            raise TypeError("Expected argument 'build_id' to be a str")
        pulumi.set(__self__, "build_id", build_id)
        if build_name and not isinstance(build_name, str):
            raise TypeError("Expected argument 'build_name' to be a str")
        pulumi.set(__self__, "build_name", build_name)
        if build_worker_pool and not isinstance(build_worker_pool, str):
            raise TypeError("Expected argument 'build_worker_pool' to be a str")
        pulumi.set(__self__, "build_worker_pool", build_worker_pool)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if docker_registry and not isinstance(docker_registry, str):
            raise TypeError("Expected argument 'docker_registry' to be a str")
        pulumi.set(__self__, "docker_registry", docker_registry)
        if docker_repository and not isinstance(docker_repository, str):
            raise TypeError("Expected argument 'docker_repository' to be a str")
        pulumi.set(__self__, "docker_repository", docker_repository)
        if entry_point and not isinstance(entry_point, str):
            raise TypeError("Expected argument 'entry_point' to be a str")
        pulumi.set(__self__, "entry_point", entry_point)
        if environment_variables and not isinstance(environment_variables, dict):
            raise TypeError("Expected argument 'environment_variables' to be a dict")
        pulumi.set(__self__, "environment_variables", environment_variables)
        if event_trigger and not isinstance(event_trigger, dict):
            raise TypeError("Expected argument 'event_trigger' to be a dict")
        pulumi.set(__self__, "event_trigger", event_trigger)
        if https_trigger and not isinstance(https_trigger, dict):
            raise TypeError("Expected argument 'https_trigger' to be a dict")
        pulumi.set(__self__, "https_trigger", https_trigger)
        if ingress_settings and not isinstance(ingress_settings, str):
            raise TypeError("Expected argument 'ingress_settings' to be a str")
        pulumi.set(__self__, "ingress_settings", ingress_settings)
        if kms_key_name and not isinstance(kms_key_name, str):
            raise TypeError("Expected argument 'kms_key_name' to be a str")
        pulumi.set(__self__, "kms_key_name", kms_key_name)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if max_instances and not isinstance(max_instances, int):
            raise TypeError("Expected argument 'max_instances' to be a int")
        pulumi.set(__self__, "max_instances", max_instances)
        if min_instances and not isinstance(min_instances, int):
            raise TypeError("Expected argument 'min_instances' to be a int")
        pulumi.set(__self__, "min_instances", min_instances)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if runtime and not isinstance(runtime, str):
            raise TypeError("Expected argument 'runtime' to be a str")
        pulumi.set(__self__, "runtime", runtime)
        if secret_environment_variables and not isinstance(secret_environment_variables, list):
            raise TypeError("Expected argument 'secret_environment_variables' to be a list")
        pulumi.set(__self__, "secret_environment_variables", secret_environment_variables)
        if secret_volumes and not isinstance(secret_volumes, list):
            raise TypeError("Expected argument 'secret_volumes' to be a list")
        pulumi.set(__self__, "secret_volumes", secret_volumes)
        if service_account_email and not isinstance(service_account_email, str):
            raise TypeError("Expected argument 'service_account_email' to be a str")
        pulumi.set(__self__, "service_account_email", service_account_email)
        if source_archive_url and not isinstance(source_archive_url, str):
            raise TypeError("Expected argument 'source_archive_url' to be a str")
        pulumi.set(__self__, "source_archive_url", source_archive_url)
        if source_repository and not isinstance(source_repository, dict):
            raise TypeError("Expected argument 'source_repository' to be a dict")
        pulumi.set(__self__, "source_repository", source_repository)
        if source_token and not isinstance(source_token, str):
            raise TypeError("Expected argument 'source_token' to be a str")
        pulumi.set(__self__, "source_token", source_token)
        if source_upload_url and not isinstance(source_upload_url, str):
            raise TypeError("Expected argument 'source_upload_url' to be a str")
        pulumi.set(__self__, "source_upload_url", source_upload_url)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if timeout and not isinstance(timeout, str):
            raise TypeError("Expected argument 'timeout' to be a str")
        pulumi.set(__self__, "timeout", timeout)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)
        if version_id and not isinstance(version_id, str):
            raise TypeError("Expected argument 'version_id' to be a str")
        pulumi.set(__self__, "version_id", version_id)
        if vpc_connector and not isinstance(vpc_connector, str):
            raise TypeError("Expected argument 'vpc_connector' to be a str")
        pulumi.set(__self__, "vpc_connector", vpc_connector)
        if vpc_connector_egress_settings and not isinstance(vpc_connector_egress_settings, str):
            raise TypeError("Expected argument 'vpc_connector_egress_settings' to be a str")
        pulumi.set(__self__, "vpc_connector_egress_settings", vpc_connector_egress_settings)

    @property
    @pulumi.getter(name="availableMemoryMb")
    def available_memory_mb(self) -> int:
        """
        The amount of memory in MB available for a function. Defaults to 256MB.
        """
        return pulumi.get(self, "available_memory_mb")

    @property
    @pulumi.getter(name="buildEnvironmentVariables")
    def build_environment_variables(self) -> Mapping[str, str]:
        """
        Build environment variables that shall be available during build time.
        """
        return pulumi.get(self, "build_environment_variables")

    @property
    @pulumi.getter(name="buildId")
    def build_id(self) -> str:
        """
        The Cloud Build ID of the latest successful deployment of the function.
        """
        return pulumi.get(self, "build_id")

    @property
    @pulumi.getter(name="buildName")
    def build_name(self) -> str:
        """
        The Cloud Build Name of the function deployment. `projects//locations//builds/`.
        """
        return pulumi.get(self, "build_name")

    @property
    @pulumi.getter(name="buildWorkerPool")
    def build_worker_pool(self) -> str:
        """
        Name of the Cloud Build Custom Worker Pool that should be used to build the function. The format of this field is `projects/{project}/locations/{region}/workerPools/{workerPool}` where `{project}` and `{region}` are the project id and region respectively where the worker pool is defined and `{workerPool}` is the short name of the worker pool. If the project id is not the same as the function, then the Cloud Functions Service Agent (`service-@gcf-admin-robot.iam.gserviceaccount.com`) must be granted the role Cloud Build Custom Workers Builder (`roles/cloudbuild.customworkers.builder`) in the project.
        """
        return pulumi.get(self, "build_worker_pool")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        User-provided description of a function.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dockerRegistry")
    def docker_registry(self) -> str:
        """
        Docker Registry to use for this deployment. If `docker_repository` field is specified, this field will be automatically set as `ARTIFACT_REGISTRY`. If unspecified, it currently defaults to `CONTAINER_REGISTRY`. This field may be overridden by the backend for eligible deployments.
        """
        return pulumi.get(self, "docker_registry")

    @property
    @pulumi.getter(name="dockerRepository")
    def docker_repository(self) -> str:
        """
        User managed repository created in Artifact Registry optionally with a customer managed encryption key. If specified, deployments will use Artifact Registry. If unspecified and the deployment is eligible to use Artifact Registry, GCF will create and use a repository named 'gcf-artifacts' for every deployed region. This is the repository to which the function docker image will be pushed after it is built by Cloud Build. It must match the pattern `projects/{project}/locations/{location}/repositories/{repository}`. Cross-project repositories are not supported. Cross-location repositories are not supported. Repository format must be 'DOCKER'.
        """
        return pulumi.get(self, "docker_repository")

    @property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> str:
        """
        The name of the function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named "function". For Node.js this is name of a function exported by the module specified in `source_location`.
        """
        return pulumi.get(self, "entry_point")

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Mapping[str, str]:
        """
        Environment variables that shall be available during function execution.
        """
        return pulumi.get(self, "environment_variables")

    @property
    @pulumi.getter(name="eventTrigger")
    def event_trigger(self) -> 'outputs.EventTriggerResponse':
        """
        A source that fires events in response to a condition in another service.
        """
        return pulumi.get(self, "event_trigger")

    @property
    @pulumi.getter(name="httpsTrigger")
    def https_trigger(self) -> 'outputs.HttpsTriggerResponse':
        """
        An HTTPS endpoint type of source that can be triggered via URL.
        """
        return pulumi.get(self, "https_trigger")

    @property
    @pulumi.getter(name="ingressSettings")
    def ingress_settings(self) -> str:
        """
        The ingress settings for the function, controlling what traffic can reach it.
        """
        return pulumi.get(self, "ingress_settings")

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> str:
        """
        Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt function resources. It must match the pattern `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`. If specified, you must also provide an artifact registry repository using the `docker_repository` field that was created with the same KMS crypto key. The following service accounts need to be granted the role 'Cloud KMS CryptoKey Encrypter/Decrypter (roles/cloudkms.cryptoKeyEncrypterDecrypter)' on the Key/KeyRing/Project/Organization (least access preferred). 1. Google Cloud Functions service account (service-{project_number}@gcf-admin-robot.iam.gserviceaccount.com) - Required to protect the function's image. 2. Google Storage service account (service-{project_number}@gs-project-accounts.iam.gserviceaccount.com) - Required to protect the function's source code. If this service account does not exist, deploying a function without a KMS key or retrieving the service agent name provisions it. For more information, see https://cloud.google.com/storage/docs/projects#service-agents and https://cloud.google.com/storage/docs/getting-service-agent#gsutil. Google Cloud Functions delegates access to service agents to protect function resources in internal projects that are not accessible by the end user.
        """
        return pulumi.get(self, "kms_key_name")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Labels associated with this Cloud Function.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> int:
        """
        The limit on the maximum number of function instances that may coexist at a given time. In some cases, such as rapid traffic surges, Cloud Functions may, for a short period of time, create more instances than the specified max instances limit. If your function cannot tolerate this temporary behavior, you may want to factor in a safety margin and set a lower max instances value than your function can tolerate. See the [Max Instances](https://cloud.google.com/functions/docs/max-instances) Guide for more details.
        """
        return pulumi.get(self, "max_instances")

    @property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> int:
        """
        A lower bound for the number function instances that may coexist at a given time.
        """
        return pulumi.get(self, "min_instances")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A user-defined name of the function. Function names must be unique globally and match pattern `projects/*/locations/*/functions/*`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> str:
        """
        The VPC Network that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network resource. If the short network name is used, the network must belong to the same project. Otherwise, it must belong to a project within the same organization. The format of this field is either `projects/{project}/global/networks/{network}` or `{network}`, where `{project}` is a project id where the network is defined, and `{network}` is the short name of the network. This field is mutually exclusive with `vpc_connector` and will be replaced by it. See [the VPC documentation](https://cloud.google.com/compute/docs/vpc) for more information on connecting Cloud projects.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def runtime(self) -> str:
        """
        The runtime in which to run the function. Required when deploying a new function, optional when updating an existing function. For a complete list of possible choices, see the [`gcloud` command reference](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime).
        """
        return pulumi.get(self, "runtime")

    @property
    @pulumi.getter(name="secretEnvironmentVariables")
    def secret_environment_variables(self) -> Sequence['outputs.SecretEnvVarResponse']:
        """
        Secret environment variables configuration.
        """
        return pulumi.get(self, "secret_environment_variables")

    @property
    @pulumi.getter(name="secretVolumes")
    def secret_volumes(self) -> Sequence['outputs.SecretVolumeResponse']:
        """
        Secret volumes configuration.
        """
        return pulumi.get(self, "secret_volumes")

    @property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> str:
        """
        The email of the function's service account. If empty, defaults to `{project_id}@appspot.gserviceaccount.com`.
        """
        return pulumi.get(self, "service_account_email")

    @property
    @pulumi.getter(name="sourceArchiveUrl")
    def source_archive_url(self) -> str:
        """
        The Google Cloud Storage URL, starting with `gs://`, pointing to the zip archive which contains the function.
        """
        return pulumi.get(self, "source_archive_url")

    @property
    @pulumi.getter(name="sourceRepository")
    def source_repository(self) -> 'outputs.SourceRepositoryResponse':
        """
        **Beta Feature** The source repository where a function is hosted.
        """
        return pulumi.get(self, "source_repository")

    @property
    @pulumi.getter(name="sourceToken")
    def source_token(self) -> str:
        """
        Input only. An identifier for Firebase function sources. Disclaimer: This field is only supported for Firebase function deployments.
        """
        return pulumi.get(self, "source_token")

    @property
    @pulumi.getter(name="sourceUploadUrl")
    def source_upload_url(self) -> str:
        """
        The Google Cloud Storage signed URL used for source uploading, generated by calling [google.cloud.functions.v1.GenerateUploadUrl]. The signature is validated on write methods (Create, Update) The signature is stripped from the Function object on read methods (Get, List)
        """
        return pulumi.get(self, "source_upload_url")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the function deployment.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def timeout(self) -> str:
        """
        The function execution timeout. Execution is considered failed and can be terminated if the function is not completed at the end of the timeout period. Defaults to 60 seconds.
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The last update timestamp of a Cloud Function.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> str:
        """
        The version identifier of the Cloud Function. Each deployment attempt results in a new version of a function being created.
        """
        return pulumi.get(self, "version_id")

    @property
    @pulumi.getter(name="vpcConnector")
    def vpc_connector(self) -> str:
        """
        The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*` This field is mutually exclusive with `network` field and will eventually replace it. See [the VPC documentation](https://cloud.google.com/compute/docs/vpc) for more information on connecting Cloud projects.
        """
        return pulumi.get(self, "vpc_connector")

    @property
    @pulumi.getter(name="vpcConnectorEgressSettings")
    def vpc_connector_egress_settings(self) -> str:
        """
        The egress settings for the connector, controlling what traffic is diverted through it.
        """
        return pulumi.get(self, "vpc_connector_egress_settings")


class AwaitableGetFunctionResult(GetFunctionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFunctionResult(
            available_memory_mb=self.available_memory_mb,
            build_environment_variables=self.build_environment_variables,
            build_id=self.build_id,
            build_name=self.build_name,
            build_worker_pool=self.build_worker_pool,
            description=self.description,
            docker_registry=self.docker_registry,
            docker_repository=self.docker_repository,
            entry_point=self.entry_point,
            environment_variables=self.environment_variables,
            event_trigger=self.event_trigger,
            https_trigger=self.https_trigger,
            ingress_settings=self.ingress_settings,
            kms_key_name=self.kms_key_name,
            labels=self.labels,
            max_instances=self.max_instances,
            min_instances=self.min_instances,
            name=self.name,
            network=self.network,
            runtime=self.runtime,
            secret_environment_variables=self.secret_environment_variables,
            secret_volumes=self.secret_volumes,
            service_account_email=self.service_account_email,
            source_archive_url=self.source_archive_url,
            source_repository=self.source_repository,
            source_token=self.source_token,
            source_upload_url=self.source_upload_url,
            status=self.status,
            timeout=self.timeout,
            update_time=self.update_time,
            version_id=self.version_id,
            vpc_connector=self.vpc_connector,
            vpc_connector_egress_settings=self.vpc_connector_egress_settings)


def get_function(function_id: Optional[str] = None,
                 location: Optional[str] = None,
                 project: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFunctionResult:
    """
    Returns a function with the given name from the requested project.
    """
    __args__ = dict()
    __args__['functionId'] = function_id
    __args__['location'] = location
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:cloudfunctions/v1:getFunction', __args__, opts=opts, typ=GetFunctionResult).value

    return AwaitableGetFunctionResult(
        available_memory_mb=__ret__.available_memory_mb,
        build_environment_variables=__ret__.build_environment_variables,
        build_id=__ret__.build_id,
        build_name=__ret__.build_name,
        build_worker_pool=__ret__.build_worker_pool,
        description=__ret__.description,
        docker_registry=__ret__.docker_registry,
        docker_repository=__ret__.docker_repository,
        entry_point=__ret__.entry_point,
        environment_variables=__ret__.environment_variables,
        event_trigger=__ret__.event_trigger,
        https_trigger=__ret__.https_trigger,
        ingress_settings=__ret__.ingress_settings,
        kms_key_name=__ret__.kms_key_name,
        labels=__ret__.labels,
        max_instances=__ret__.max_instances,
        min_instances=__ret__.min_instances,
        name=__ret__.name,
        network=__ret__.network,
        runtime=__ret__.runtime,
        secret_environment_variables=__ret__.secret_environment_variables,
        secret_volumes=__ret__.secret_volumes,
        service_account_email=__ret__.service_account_email,
        source_archive_url=__ret__.source_archive_url,
        source_repository=__ret__.source_repository,
        source_token=__ret__.source_token,
        source_upload_url=__ret__.source_upload_url,
        status=__ret__.status,
        timeout=__ret__.timeout,
        update_time=__ret__.update_time,
        version_id=__ret__.version_id,
        vpc_connector=__ret__.vpc_connector,
        vpc_connector_egress_settings=__ret__.vpc_connector_egress_settings)


@_utilities.lift_output_func(get_function)
def get_function_output(function_id: Optional[pulumi.Input[str]] = None,
                        location: Optional[pulumi.Input[str]] = None,
                        project: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFunctionResult]:
    """
    Returns a function with the given name from the requested project.
    """
    ...
