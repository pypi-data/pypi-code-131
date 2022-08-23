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
    'GetConfigResult',
    'AwaitableGetConfigResult',
    'get_config',
    'get_config_output',
]

@pulumi.output_type
class GetConfigResult:
    def __init__(__self__, apis=None, authentication=None, backend=None, billing=None, config_version=None, context=None, control=None, custom_error=None, documentation=None, endpoints=None, enums=None, http=None, logging=None, logs=None, metrics=None, monitored_resources=None, monitoring=None, name=None, producer_project_id=None, quota=None, source_info=None, system_parameters=None, system_types=None, title=None, types=None, usage=None):
        if apis and not isinstance(apis, list):
            raise TypeError("Expected argument 'apis' to be a list")
        pulumi.set(__self__, "apis", apis)
        if authentication and not isinstance(authentication, dict):
            raise TypeError("Expected argument 'authentication' to be a dict")
        pulumi.set(__self__, "authentication", authentication)
        if backend and not isinstance(backend, dict):
            raise TypeError("Expected argument 'backend' to be a dict")
        pulumi.set(__self__, "backend", backend)
        if billing and not isinstance(billing, dict):
            raise TypeError("Expected argument 'billing' to be a dict")
        pulumi.set(__self__, "billing", billing)
        if config_version and not isinstance(config_version, int):
            raise TypeError("Expected argument 'config_version' to be a int")
        pulumi.set(__self__, "config_version", config_version)
        if context and not isinstance(context, dict):
            raise TypeError("Expected argument 'context' to be a dict")
        pulumi.set(__self__, "context", context)
        if control and not isinstance(control, dict):
            raise TypeError("Expected argument 'control' to be a dict")
        pulumi.set(__self__, "control", control)
        if custom_error and not isinstance(custom_error, dict):
            raise TypeError("Expected argument 'custom_error' to be a dict")
        pulumi.set(__self__, "custom_error", custom_error)
        if documentation and not isinstance(documentation, dict):
            raise TypeError("Expected argument 'documentation' to be a dict")
        pulumi.set(__self__, "documentation", documentation)
        if endpoints and not isinstance(endpoints, list):
            raise TypeError("Expected argument 'endpoints' to be a list")
        pulumi.set(__self__, "endpoints", endpoints)
        if enums and not isinstance(enums, list):
            raise TypeError("Expected argument 'enums' to be a list")
        pulumi.set(__self__, "enums", enums)
        if http and not isinstance(http, dict):
            raise TypeError("Expected argument 'http' to be a dict")
        pulumi.set(__self__, "http", http)
        if logging and not isinstance(logging, dict):
            raise TypeError("Expected argument 'logging' to be a dict")
        pulumi.set(__self__, "logging", logging)
        if logs and not isinstance(logs, list):
            raise TypeError("Expected argument 'logs' to be a list")
        pulumi.set(__self__, "logs", logs)
        if metrics and not isinstance(metrics, list):
            raise TypeError("Expected argument 'metrics' to be a list")
        pulumi.set(__self__, "metrics", metrics)
        if monitored_resources and not isinstance(monitored_resources, list):
            raise TypeError("Expected argument 'monitored_resources' to be a list")
        pulumi.set(__self__, "monitored_resources", monitored_resources)
        if monitoring and not isinstance(monitoring, dict):
            raise TypeError("Expected argument 'monitoring' to be a dict")
        pulumi.set(__self__, "monitoring", monitoring)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if producer_project_id and not isinstance(producer_project_id, str):
            raise TypeError("Expected argument 'producer_project_id' to be a str")
        pulumi.set(__self__, "producer_project_id", producer_project_id)
        if quota and not isinstance(quota, dict):
            raise TypeError("Expected argument 'quota' to be a dict")
        pulumi.set(__self__, "quota", quota)
        if source_info and not isinstance(source_info, dict):
            raise TypeError("Expected argument 'source_info' to be a dict")
        pulumi.set(__self__, "source_info", source_info)
        if system_parameters and not isinstance(system_parameters, dict):
            raise TypeError("Expected argument 'system_parameters' to be a dict")
        pulumi.set(__self__, "system_parameters", system_parameters)
        if system_types and not isinstance(system_types, list):
            raise TypeError("Expected argument 'system_types' to be a list")
        pulumi.set(__self__, "system_types", system_types)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if types and not isinstance(types, list):
            raise TypeError("Expected argument 'types' to be a list")
        pulumi.set(__self__, "types", types)
        if usage and not isinstance(usage, dict):
            raise TypeError("Expected argument 'usage' to be a dict")
        pulumi.set(__self__, "usage", usage)

    @property
    @pulumi.getter
    def apis(self) -> Sequence['outputs.ApiResponse']:
        """
        A list of API interfaces exported by this service. Only the `name` field of the google.protobuf.Api needs to be provided by the configuration author, as the remaining fields will be derived from the IDL during the normalization process. It is an error to specify an API interface here which cannot be resolved against the associated IDL files.
        """
        return pulumi.get(self, "apis")

    @property
    @pulumi.getter
    def authentication(self) -> 'outputs.AuthenticationResponse':
        """
        Auth configuration.
        """
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter
    def backend(self) -> 'outputs.BackendResponse':
        """
        API backend configuration.
        """
        return pulumi.get(self, "backend")

    @property
    @pulumi.getter
    def billing(self) -> 'outputs.BillingResponse':
        """
        Billing configuration.
        """
        return pulumi.get(self, "billing")

    @property
    @pulumi.getter(name="configVersion")
    def config_version(self) -> int:
        """
        Obsolete. Do not use. This field has no semantic meaning. The service config compiler always sets this field to `3`.
        """
        return pulumi.get(self, "config_version")

    @property
    @pulumi.getter
    def context(self) -> 'outputs.ContextResponse':
        """
        Context configuration.
        """
        return pulumi.get(self, "context")

    @property
    @pulumi.getter
    def control(self) -> 'outputs.ControlResponse':
        """
        Configuration for the service control plane.
        """
        return pulumi.get(self, "control")

    @property
    @pulumi.getter(name="customError")
    def custom_error(self) -> 'outputs.CustomErrorResponse':
        """
        Custom error configuration.
        """
        return pulumi.get(self, "custom_error")

    @property
    @pulumi.getter
    def documentation(self) -> 'outputs.DocumentationResponse':
        """
        Additional API documentation.
        """
        return pulumi.get(self, "documentation")

    @property
    @pulumi.getter
    def endpoints(self) -> Sequence['outputs.EndpointResponse']:
        """
        Configuration for network endpoints. If this is empty, then an endpoint with the same name as the service is automatically generated to service all defined APIs.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def enums(self) -> Sequence['outputs.EnumResponse']:
        """
        A list of all enum types included in this API service. Enums referenced directly or indirectly by the `apis` are automatically included. Enums which are not referenced but shall be included should be listed here by name by the configuration author. Example: enums: - name: google.someapi.v1.SomeEnum
        """
        return pulumi.get(self, "enums")

    @property
    @pulumi.getter
    def http(self) -> 'outputs.HttpResponse':
        """
        HTTP configuration.
        """
        return pulumi.get(self, "http")

    @property
    @pulumi.getter
    def logging(self) -> 'outputs.LoggingResponse':
        """
        Logging configuration.
        """
        return pulumi.get(self, "logging")

    @property
    @pulumi.getter
    def logs(self) -> Sequence['outputs.LogDescriptorResponse']:
        """
        Defines the logs used by this service.
        """
        return pulumi.get(self, "logs")

    @property
    @pulumi.getter
    def metrics(self) -> Sequence['outputs.MetricDescriptorResponse']:
        """
        Defines the metrics used by this service.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter(name="monitoredResources")
    def monitored_resources(self) -> Sequence['outputs.MonitoredResourceDescriptorResponse']:
        """
        Defines the monitored resources used by this service. This is required by the Service.monitoring and Service.logging configurations.
        """
        return pulumi.get(self, "monitored_resources")

    @property
    @pulumi.getter
    def monitoring(self) -> 'outputs.MonitoringResponse':
        """
        Monitoring configuration.
        """
        return pulumi.get(self, "monitoring")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The service name, which is a DNS-like logical identifier for the service, such as `calendar.googleapis.com`. The service name typically goes through DNS verification to make sure the owner of the service also owns the DNS name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="producerProjectId")
    def producer_project_id(self) -> str:
        """
        The Google project that owns this service.
        """
        return pulumi.get(self, "producer_project_id")

    @property
    @pulumi.getter
    def quota(self) -> 'outputs.QuotaResponse':
        """
        Quota configuration.
        """
        return pulumi.get(self, "quota")

    @property
    @pulumi.getter(name="sourceInfo")
    def source_info(self) -> 'outputs.SourceInfoResponse':
        """
        The source information for this configuration if available.
        """
        return pulumi.get(self, "source_info")

    @property
    @pulumi.getter(name="systemParameters")
    def system_parameters(self) -> 'outputs.SystemParametersResponse':
        """
        System parameter configuration.
        """
        return pulumi.get(self, "system_parameters")

    @property
    @pulumi.getter(name="systemTypes")
    def system_types(self) -> Sequence['outputs.TypeResponse']:
        """
        A list of all proto message types included in this API service. It serves similar purpose as [google.api.Service.types], except that these types are not needed by user-defined APIs. Therefore, they will not show up in the generated discovery doc. This field should only be used to define system APIs in ESF.
        """
        return pulumi.get(self, "system_types")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        The product title for this service, it is the name displayed in Google Cloud Console.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def types(self) -> Sequence['outputs.TypeResponse']:
        """
        A list of all proto message types included in this API service. Types referenced directly or indirectly by the `apis` are automatically included. Messages which are not referenced but shall be included, such as types used by the `google.protobuf.Any` type, should be listed here by name by the configuration author. Example: types: - name: google.protobuf.Int32
        """
        return pulumi.get(self, "types")

    @property
    @pulumi.getter
    def usage(self) -> 'outputs.UsageResponse':
        """
        Configuration controlling usage of this service.
        """
        return pulumi.get(self, "usage")


class AwaitableGetConfigResult(GetConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigResult(
            apis=self.apis,
            authentication=self.authentication,
            backend=self.backend,
            billing=self.billing,
            config_version=self.config_version,
            context=self.context,
            control=self.control,
            custom_error=self.custom_error,
            documentation=self.documentation,
            endpoints=self.endpoints,
            enums=self.enums,
            http=self.http,
            logging=self.logging,
            logs=self.logs,
            metrics=self.metrics,
            monitored_resources=self.monitored_resources,
            monitoring=self.monitoring,
            name=self.name,
            producer_project_id=self.producer_project_id,
            quota=self.quota,
            source_info=self.source_info,
            system_parameters=self.system_parameters,
            system_types=self.system_types,
            title=self.title,
            types=self.types,
            usage=self.usage)


def get_config(config_id: Optional[str] = None,
               service_name: Optional[str] = None,
               view: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigResult:
    """
    Gets a service configuration (version) for a managed service.
    """
    __args__ = dict()
    __args__['configId'] = config_id
    __args__['serviceName'] = service_name
    __args__['view'] = view
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:servicemanagement/v1:getConfig', __args__, opts=opts, typ=GetConfigResult).value

    return AwaitableGetConfigResult(
        apis=__ret__.apis,
        authentication=__ret__.authentication,
        backend=__ret__.backend,
        billing=__ret__.billing,
        config_version=__ret__.config_version,
        context=__ret__.context,
        control=__ret__.control,
        custom_error=__ret__.custom_error,
        documentation=__ret__.documentation,
        endpoints=__ret__.endpoints,
        enums=__ret__.enums,
        http=__ret__.http,
        logging=__ret__.logging,
        logs=__ret__.logs,
        metrics=__ret__.metrics,
        monitored_resources=__ret__.monitored_resources,
        monitoring=__ret__.monitoring,
        name=__ret__.name,
        producer_project_id=__ret__.producer_project_id,
        quota=__ret__.quota,
        source_info=__ret__.source_info,
        system_parameters=__ret__.system_parameters,
        system_types=__ret__.system_types,
        title=__ret__.title,
        types=__ret__.types,
        usage=__ret__.usage)


@_utilities.lift_output_func(get_config)
def get_config_output(config_id: Optional[pulumi.Input[str]] = None,
                      service_name: Optional[pulumi.Input[str]] = None,
                      view: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigResult]:
    """
    Gets a service configuration (version) for a managed service.
    """
    ...
