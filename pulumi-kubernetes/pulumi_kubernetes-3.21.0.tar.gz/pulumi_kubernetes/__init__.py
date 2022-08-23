# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *
from ._inputs import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_kubernetes.admissionregistration as __admissionregistration
    admissionregistration = __admissionregistration
    import pulumi_kubernetes.apiextensions as __apiextensions
    apiextensions = __apiextensions
    import pulumi_kubernetes.apiregistration as __apiregistration
    apiregistration = __apiregistration
    import pulumi_kubernetes.apps as __apps
    apps = __apps
    import pulumi_kubernetes.auditregistration as __auditregistration
    auditregistration = __auditregistration
    import pulumi_kubernetes.authentication as __authentication
    authentication = __authentication
    import pulumi_kubernetes.authorization as __authorization
    authorization = __authorization
    import pulumi_kubernetes.autoscaling as __autoscaling
    autoscaling = __autoscaling
    import pulumi_kubernetes.batch as __batch
    batch = __batch
    import pulumi_kubernetes.certificates as __certificates
    certificates = __certificates
    import pulumi_kubernetes.coordination as __coordination
    coordination = __coordination
    import pulumi_kubernetes.core as __core
    core = __core
    import pulumi_kubernetes.discovery as __discovery
    discovery = __discovery
    import pulumi_kubernetes.events as __events
    events = __events
    import pulumi_kubernetes.extensions as __extensions
    extensions = __extensions
    import pulumi_kubernetes.flowcontrol as __flowcontrol
    flowcontrol = __flowcontrol
    import pulumi_kubernetes.helm as __helm
    helm = __helm
    import pulumi_kubernetes.kustomize as __kustomize
    kustomize = __kustomize
    import pulumi_kubernetes.meta as __meta
    meta = __meta
    import pulumi_kubernetes.networking as __networking
    networking = __networking
    import pulumi_kubernetes.node as __node
    node = __node
    import pulumi_kubernetes.policy as __policy
    policy = __policy
    import pulumi_kubernetes.rbac as __rbac
    rbac = __rbac
    import pulumi_kubernetes.scheduling as __scheduling
    scheduling = __scheduling
    import pulumi_kubernetes.settings as __settings
    settings = __settings
    import pulumi_kubernetes.storage as __storage
    storage = __storage
    import pulumi_kubernetes.yaml as __yaml
    yaml = __yaml
else:
    admissionregistration = _utilities.lazy_import('pulumi_kubernetes.admissionregistration')
    apiextensions = _utilities.lazy_import('pulumi_kubernetes.apiextensions')
    apiregistration = _utilities.lazy_import('pulumi_kubernetes.apiregistration')
    apps = _utilities.lazy_import('pulumi_kubernetes.apps')
    auditregistration = _utilities.lazy_import('pulumi_kubernetes.auditregistration')
    authentication = _utilities.lazy_import('pulumi_kubernetes.authentication')
    authorization = _utilities.lazy_import('pulumi_kubernetes.authorization')
    autoscaling = _utilities.lazy_import('pulumi_kubernetes.autoscaling')
    batch = _utilities.lazy_import('pulumi_kubernetes.batch')
    certificates = _utilities.lazy_import('pulumi_kubernetes.certificates')
    coordination = _utilities.lazy_import('pulumi_kubernetes.coordination')
    core = _utilities.lazy_import('pulumi_kubernetes.core')
    discovery = _utilities.lazy_import('pulumi_kubernetes.discovery')
    events = _utilities.lazy_import('pulumi_kubernetes.events')
    extensions = _utilities.lazy_import('pulumi_kubernetes.extensions')
    flowcontrol = _utilities.lazy_import('pulumi_kubernetes.flowcontrol')
    helm = _utilities.lazy_import('pulumi_kubernetes.helm')
    kustomize = _utilities.lazy_import('pulumi_kubernetes.kustomize')
    meta = _utilities.lazy_import('pulumi_kubernetes.meta')
    networking = _utilities.lazy_import('pulumi_kubernetes.networking')
    node = _utilities.lazy_import('pulumi_kubernetes.node')
    policy = _utilities.lazy_import('pulumi_kubernetes.policy')
    rbac = _utilities.lazy_import('pulumi_kubernetes.rbac')
    scheduling = _utilities.lazy_import('pulumi_kubernetes.scheduling')
    settings = _utilities.lazy_import('pulumi_kubernetes.settings')
    storage = _utilities.lazy_import('pulumi_kubernetes.storage')
    yaml = _utilities.lazy_import('pulumi_kubernetes.yaml')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "kubernetes",
  "mod": "admissionregistration.k8s.io/v1",
  "fqn": "pulumi_kubernetes.admissionregistration.v1",
  "classes": {
   "kubernetes:admissionregistration.k8s.io/v1:MutatingWebhookConfiguration": "MutatingWebhookConfiguration",
   "kubernetes:admissionregistration.k8s.io/v1:MutatingWebhookConfigurationList": "MutatingWebhookConfigurationList",
   "kubernetes:admissionregistration.k8s.io/v1:MutatingWebhookConfigurationPatch": "MutatingWebhookConfigurationPatch",
   "kubernetes:admissionregistration.k8s.io/v1:ValidatingWebhookConfiguration": "ValidatingWebhookConfiguration",
   "kubernetes:admissionregistration.k8s.io/v1:ValidatingWebhookConfigurationList": "ValidatingWebhookConfigurationList",
   "kubernetes:admissionregistration.k8s.io/v1:ValidatingWebhookConfigurationPatch": "ValidatingWebhookConfigurationPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "admissionregistration.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.admissionregistration.v1beta1",
  "classes": {
   "kubernetes:admissionregistration.k8s.io/v1beta1:MutatingWebhookConfiguration": "MutatingWebhookConfiguration",
   "kubernetes:admissionregistration.k8s.io/v1beta1:MutatingWebhookConfigurationList": "MutatingWebhookConfigurationList",
   "kubernetes:admissionregistration.k8s.io/v1beta1:MutatingWebhookConfigurationPatch": "MutatingWebhookConfigurationPatch",
   "kubernetes:admissionregistration.k8s.io/v1beta1:ValidatingWebhookConfiguration": "ValidatingWebhookConfiguration",
   "kubernetes:admissionregistration.k8s.io/v1beta1:ValidatingWebhookConfigurationList": "ValidatingWebhookConfigurationList",
   "kubernetes:admissionregistration.k8s.io/v1beta1:ValidatingWebhookConfigurationPatch": "ValidatingWebhookConfigurationPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apiextensions.k8s.io/v1",
  "fqn": "pulumi_kubernetes.apiextensions.v1",
  "classes": {
   "kubernetes:apiextensions.k8s.io/v1:CustomResourceDefinition": "CustomResourceDefinition",
   "kubernetes:apiextensions.k8s.io/v1:CustomResourceDefinitionList": "CustomResourceDefinitionList",
   "kubernetes:apiextensions.k8s.io/v1:CustomResourceDefinitionPatch": "CustomResourceDefinitionPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apiextensions.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.apiextensions.v1beta1",
  "classes": {
   "kubernetes:apiextensions.k8s.io/v1beta1:CustomResourceDefinition": "CustomResourceDefinition",
   "kubernetes:apiextensions.k8s.io/v1beta1:CustomResourceDefinitionList": "CustomResourceDefinitionList",
   "kubernetes:apiextensions.k8s.io/v1beta1:CustomResourceDefinitionPatch": "CustomResourceDefinitionPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apiregistration.k8s.io/v1",
  "fqn": "pulumi_kubernetes.apiregistration.v1",
  "classes": {
   "kubernetes:apiregistration.k8s.io/v1:APIService": "APIService",
   "kubernetes:apiregistration.k8s.io/v1:APIServiceList": "APIServiceList",
   "kubernetes:apiregistration.k8s.io/v1:APIServicePatch": "APIServicePatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apiregistration.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.apiregistration.v1beta1",
  "classes": {
   "kubernetes:apiregistration.k8s.io/v1beta1:APIService": "APIService",
   "kubernetes:apiregistration.k8s.io/v1beta1:APIServiceList": "APIServiceList",
   "kubernetes:apiregistration.k8s.io/v1beta1:APIServicePatch": "APIServicePatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apps/v1",
  "fqn": "pulumi_kubernetes.apps.v1",
  "classes": {
   "kubernetes:apps/v1:ControllerRevision": "ControllerRevision",
   "kubernetes:apps/v1:ControllerRevisionList": "ControllerRevisionList",
   "kubernetes:apps/v1:ControllerRevisionPatch": "ControllerRevisionPatch",
   "kubernetes:apps/v1:DaemonSet": "DaemonSet",
   "kubernetes:apps/v1:DaemonSetList": "DaemonSetList",
   "kubernetes:apps/v1:DaemonSetPatch": "DaemonSetPatch",
   "kubernetes:apps/v1:Deployment": "Deployment",
   "kubernetes:apps/v1:DeploymentList": "DeploymentList",
   "kubernetes:apps/v1:DeploymentPatch": "DeploymentPatch",
   "kubernetes:apps/v1:ReplicaSet": "ReplicaSet",
   "kubernetes:apps/v1:ReplicaSetList": "ReplicaSetList",
   "kubernetes:apps/v1:ReplicaSetPatch": "ReplicaSetPatch",
   "kubernetes:apps/v1:StatefulSet": "StatefulSet",
   "kubernetes:apps/v1:StatefulSetList": "StatefulSetList",
   "kubernetes:apps/v1:StatefulSetPatch": "StatefulSetPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apps/v1beta1",
  "fqn": "pulumi_kubernetes.apps.v1beta1",
  "classes": {
   "kubernetes:apps/v1beta1:ControllerRevision": "ControllerRevision",
   "kubernetes:apps/v1beta1:ControllerRevisionList": "ControllerRevisionList",
   "kubernetes:apps/v1beta1:ControllerRevisionPatch": "ControllerRevisionPatch",
   "kubernetes:apps/v1beta1:Deployment": "Deployment",
   "kubernetes:apps/v1beta1:DeploymentList": "DeploymentList",
   "kubernetes:apps/v1beta1:DeploymentPatch": "DeploymentPatch",
   "kubernetes:apps/v1beta1:StatefulSet": "StatefulSet",
   "kubernetes:apps/v1beta1:StatefulSetList": "StatefulSetList",
   "kubernetes:apps/v1beta1:StatefulSetPatch": "StatefulSetPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "apps/v1beta2",
  "fqn": "pulumi_kubernetes.apps.v1beta2",
  "classes": {
   "kubernetes:apps/v1beta2:ControllerRevision": "ControllerRevision",
   "kubernetes:apps/v1beta2:ControllerRevisionList": "ControllerRevisionList",
   "kubernetes:apps/v1beta2:ControllerRevisionPatch": "ControllerRevisionPatch",
   "kubernetes:apps/v1beta2:DaemonSet": "DaemonSet",
   "kubernetes:apps/v1beta2:DaemonSetList": "DaemonSetList",
   "kubernetes:apps/v1beta2:DaemonSetPatch": "DaemonSetPatch",
   "kubernetes:apps/v1beta2:Deployment": "Deployment",
   "kubernetes:apps/v1beta2:DeploymentList": "DeploymentList",
   "kubernetes:apps/v1beta2:DeploymentPatch": "DeploymentPatch",
   "kubernetes:apps/v1beta2:ReplicaSet": "ReplicaSet",
   "kubernetes:apps/v1beta2:ReplicaSetList": "ReplicaSetList",
   "kubernetes:apps/v1beta2:ReplicaSetPatch": "ReplicaSetPatch",
   "kubernetes:apps/v1beta2:StatefulSet": "StatefulSet",
   "kubernetes:apps/v1beta2:StatefulSetList": "StatefulSetList",
   "kubernetes:apps/v1beta2:StatefulSetPatch": "StatefulSetPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "auditregistration.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.auditregistration.v1alpha1",
  "classes": {
   "kubernetes:auditregistration.k8s.io/v1alpha1:AuditSink": "AuditSink",
   "kubernetes:auditregistration.k8s.io/v1alpha1:AuditSinkList": "AuditSinkList",
   "kubernetes:auditregistration.k8s.io/v1alpha1:AuditSinkPatch": "AuditSinkPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "authentication.k8s.io/v1",
  "fqn": "pulumi_kubernetes.authentication.v1",
  "classes": {
   "kubernetes:authentication.k8s.io/v1:TokenRequest": "TokenRequest",
   "kubernetes:authentication.k8s.io/v1:TokenRequestPatch": "TokenRequestPatch",
   "kubernetes:authentication.k8s.io/v1:TokenReview": "TokenReview",
   "kubernetes:authentication.k8s.io/v1:TokenReviewPatch": "TokenReviewPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "authentication.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.authentication.v1beta1",
  "classes": {
   "kubernetes:authentication.k8s.io/v1beta1:TokenReview": "TokenReview",
   "kubernetes:authentication.k8s.io/v1beta1:TokenReviewPatch": "TokenReviewPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "authorization.k8s.io/v1",
  "fqn": "pulumi_kubernetes.authorization.v1",
  "classes": {
   "kubernetes:authorization.k8s.io/v1:LocalSubjectAccessReview": "LocalSubjectAccessReview",
   "kubernetes:authorization.k8s.io/v1:LocalSubjectAccessReviewPatch": "LocalSubjectAccessReviewPatch",
   "kubernetes:authorization.k8s.io/v1:SelfSubjectAccessReview": "SelfSubjectAccessReview",
   "kubernetes:authorization.k8s.io/v1:SelfSubjectAccessReviewPatch": "SelfSubjectAccessReviewPatch",
   "kubernetes:authorization.k8s.io/v1:SelfSubjectRulesReview": "SelfSubjectRulesReview",
   "kubernetes:authorization.k8s.io/v1:SelfSubjectRulesReviewPatch": "SelfSubjectRulesReviewPatch",
   "kubernetes:authorization.k8s.io/v1:SubjectAccessReview": "SubjectAccessReview",
   "kubernetes:authorization.k8s.io/v1:SubjectAccessReviewPatch": "SubjectAccessReviewPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "authorization.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.authorization.v1beta1",
  "classes": {
   "kubernetes:authorization.k8s.io/v1beta1:LocalSubjectAccessReview": "LocalSubjectAccessReview",
   "kubernetes:authorization.k8s.io/v1beta1:LocalSubjectAccessReviewPatch": "LocalSubjectAccessReviewPatch",
   "kubernetes:authorization.k8s.io/v1beta1:SelfSubjectAccessReview": "SelfSubjectAccessReview",
   "kubernetes:authorization.k8s.io/v1beta1:SelfSubjectAccessReviewPatch": "SelfSubjectAccessReviewPatch",
   "kubernetes:authorization.k8s.io/v1beta1:SelfSubjectRulesReview": "SelfSubjectRulesReview",
   "kubernetes:authorization.k8s.io/v1beta1:SelfSubjectRulesReviewPatch": "SelfSubjectRulesReviewPatch",
   "kubernetes:authorization.k8s.io/v1beta1:SubjectAccessReview": "SubjectAccessReview",
   "kubernetes:authorization.k8s.io/v1beta1:SubjectAccessReviewPatch": "SubjectAccessReviewPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "autoscaling/v1",
  "fqn": "pulumi_kubernetes.autoscaling.v1",
  "classes": {
   "kubernetes:autoscaling/v1:HorizontalPodAutoscaler": "HorizontalPodAutoscaler",
   "kubernetes:autoscaling/v1:HorizontalPodAutoscalerList": "HorizontalPodAutoscalerList",
   "kubernetes:autoscaling/v1:HorizontalPodAutoscalerPatch": "HorizontalPodAutoscalerPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "autoscaling/v2",
  "fqn": "pulumi_kubernetes.autoscaling.v2",
  "classes": {
   "kubernetes:autoscaling/v2:HorizontalPodAutoscaler": "HorizontalPodAutoscaler",
   "kubernetes:autoscaling/v2:HorizontalPodAutoscalerList": "HorizontalPodAutoscalerList",
   "kubernetes:autoscaling/v2:HorizontalPodAutoscalerPatch": "HorizontalPodAutoscalerPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "autoscaling/v2beta1",
  "fqn": "pulumi_kubernetes.autoscaling.v2beta1",
  "classes": {
   "kubernetes:autoscaling/v2beta1:HorizontalPodAutoscaler": "HorizontalPodAutoscaler",
   "kubernetes:autoscaling/v2beta1:HorizontalPodAutoscalerList": "HorizontalPodAutoscalerList",
   "kubernetes:autoscaling/v2beta1:HorizontalPodAutoscalerPatch": "HorizontalPodAutoscalerPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "autoscaling/v2beta2",
  "fqn": "pulumi_kubernetes.autoscaling.v2beta2",
  "classes": {
   "kubernetes:autoscaling/v2beta2:HorizontalPodAutoscaler": "HorizontalPodAutoscaler",
   "kubernetes:autoscaling/v2beta2:HorizontalPodAutoscalerList": "HorizontalPodAutoscalerList",
   "kubernetes:autoscaling/v2beta2:HorizontalPodAutoscalerPatch": "HorizontalPodAutoscalerPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "batch/v1",
  "fqn": "pulumi_kubernetes.batch.v1",
  "classes": {
   "kubernetes:batch/v1:CronJob": "CronJob",
   "kubernetes:batch/v1:CronJobList": "CronJobList",
   "kubernetes:batch/v1:CronJobPatch": "CronJobPatch",
   "kubernetes:batch/v1:Job": "Job",
   "kubernetes:batch/v1:JobList": "JobList",
   "kubernetes:batch/v1:JobPatch": "JobPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "batch/v1beta1",
  "fqn": "pulumi_kubernetes.batch.v1beta1",
  "classes": {
   "kubernetes:batch/v1beta1:CronJob": "CronJob",
   "kubernetes:batch/v1beta1:CronJobList": "CronJobList",
   "kubernetes:batch/v1beta1:CronJobPatch": "CronJobPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "batch/v2alpha1",
  "fqn": "pulumi_kubernetes.batch.v2alpha1",
  "classes": {
   "kubernetes:batch/v2alpha1:CronJob": "CronJob",
   "kubernetes:batch/v2alpha1:CronJobList": "CronJobList",
   "kubernetes:batch/v2alpha1:CronJobPatch": "CronJobPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "certificates.k8s.io/v1",
  "fqn": "pulumi_kubernetes.certificates.v1",
  "classes": {
   "kubernetes:certificates.k8s.io/v1:CertificateSigningRequest": "CertificateSigningRequest",
   "kubernetes:certificates.k8s.io/v1:CertificateSigningRequestList": "CertificateSigningRequestList",
   "kubernetes:certificates.k8s.io/v1:CertificateSigningRequestPatch": "CertificateSigningRequestPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "certificates.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.certificates.v1beta1",
  "classes": {
   "kubernetes:certificates.k8s.io/v1beta1:CertificateSigningRequest": "CertificateSigningRequest",
   "kubernetes:certificates.k8s.io/v1beta1:CertificateSigningRequestList": "CertificateSigningRequestList",
   "kubernetes:certificates.k8s.io/v1beta1:CertificateSigningRequestPatch": "CertificateSigningRequestPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "coordination.k8s.io/v1",
  "fqn": "pulumi_kubernetes.coordination.v1",
  "classes": {
   "kubernetes:coordination.k8s.io/v1:Lease": "Lease",
   "kubernetes:coordination.k8s.io/v1:LeaseList": "LeaseList",
   "kubernetes:coordination.k8s.io/v1:LeasePatch": "LeasePatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "coordination.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.coordination.v1beta1",
  "classes": {
   "kubernetes:coordination.k8s.io/v1beta1:Lease": "Lease",
   "kubernetes:coordination.k8s.io/v1beta1:LeaseList": "LeaseList",
   "kubernetes:coordination.k8s.io/v1beta1:LeasePatch": "LeasePatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "core/v1",
  "fqn": "pulumi_kubernetes.core.v1",
  "classes": {
   "kubernetes:core/v1:Binding": "Binding",
   "kubernetes:core/v1:BindingPatch": "BindingPatch",
   "kubernetes:core/v1:ConfigMap": "ConfigMap",
   "kubernetes:core/v1:ConfigMapList": "ConfigMapList",
   "kubernetes:core/v1:ConfigMapPatch": "ConfigMapPatch",
   "kubernetes:core/v1:Endpoints": "Endpoints",
   "kubernetes:core/v1:EndpointsList": "EndpointsList",
   "kubernetes:core/v1:EndpointsPatch": "EndpointsPatch",
   "kubernetes:core/v1:Event": "Event",
   "kubernetes:core/v1:EventList": "EventList",
   "kubernetes:core/v1:EventPatch": "EventPatch",
   "kubernetes:core/v1:LimitRange": "LimitRange",
   "kubernetes:core/v1:LimitRangeList": "LimitRangeList",
   "kubernetes:core/v1:LimitRangePatch": "LimitRangePatch",
   "kubernetes:core/v1:Namespace": "Namespace",
   "kubernetes:core/v1:NamespaceList": "NamespaceList",
   "kubernetes:core/v1:NamespacePatch": "NamespacePatch",
   "kubernetes:core/v1:Node": "Node",
   "kubernetes:core/v1:NodeList": "NodeList",
   "kubernetes:core/v1:NodePatch": "NodePatch",
   "kubernetes:core/v1:PersistentVolume": "PersistentVolume",
   "kubernetes:core/v1:PersistentVolumeClaim": "PersistentVolumeClaim",
   "kubernetes:core/v1:PersistentVolumeClaimList": "PersistentVolumeClaimList",
   "kubernetes:core/v1:PersistentVolumeClaimPatch": "PersistentVolumeClaimPatch",
   "kubernetes:core/v1:PersistentVolumeList": "PersistentVolumeList",
   "kubernetes:core/v1:PersistentVolumePatch": "PersistentVolumePatch",
   "kubernetes:core/v1:Pod": "Pod",
   "kubernetes:core/v1:PodList": "PodList",
   "kubernetes:core/v1:PodPatch": "PodPatch",
   "kubernetes:core/v1:PodTemplate": "PodTemplate",
   "kubernetes:core/v1:PodTemplateList": "PodTemplateList",
   "kubernetes:core/v1:PodTemplatePatch": "PodTemplatePatch",
   "kubernetes:core/v1:ReplicationController": "ReplicationController",
   "kubernetes:core/v1:ReplicationControllerList": "ReplicationControllerList",
   "kubernetes:core/v1:ReplicationControllerPatch": "ReplicationControllerPatch",
   "kubernetes:core/v1:ResourceQuota": "ResourceQuota",
   "kubernetes:core/v1:ResourceQuotaList": "ResourceQuotaList",
   "kubernetes:core/v1:ResourceQuotaPatch": "ResourceQuotaPatch",
   "kubernetes:core/v1:Secret": "Secret",
   "kubernetes:core/v1:SecretList": "SecretList",
   "kubernetes:core/v1:SecretPatch": "SecretPatch",
   "kubernetes:core/v1:Service": "Service",
   "kubernetes:core/v1:ServiceAccount": "ServiceAccount",
   "kubernetes:core/v1:ServiceAccountList": "ServiceAccountList",
   "kubernetes:core/v1:ServiceAccountPatch": "ServiceAccountPatch",
   "kubernetes:core/v1:ServiceList": "ServiceList",
   "kubernetes:core/v1:ServicePatch": "ServicePatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "discovery.k8s.io/v1",
  "fqn": "pulumi_kubernetes.discovery.v1",
  "classes": {
   "kubernetes:discovery.k8s.io/v1:EndpointSlice": "EndpointSlice",
   "kubernetes:discovery.k8s.io/v1:EndpointSliceList": "EndpointSliceList",
   "kubernetes:discovery.k8s.io/v1:EndpointSlicePatch": "EndpointSlicePatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "discovery.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.discovery.v1beta1",
  "classes": {
   "kubernetes:discovery.k8s.io/v1beta1:EndpointSlice": "EndpointSlice",
   "kubernetes:discovery.k8s.io/v1beta1:EndpointSliceList": "EndpointSliceList",
   "kubernetes:discovery.k8s.io/v1beta1:EndpointSlicePatch": "EndpointSlicePatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "events.k8s.io/v1",
  "fqn": "pulumi_kubernetes.events.v1",
  "classes": {
   "kubernetes:events.k8s.io/v1:Event": "Event",
   "kubernetes:events.k8s.io/v1:EventList": "EventList",
   "kubernetes:events.k8s.io/v1:EventPatch": "EventPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "events.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.events.v1beta1",
  "classes": {
   "kubernetes:events.k8s.io/v1beta1:Event": "Event",
   "kubernetes:events.k8s.io/v1beta1:EventList": "EventList",
   "kubernetes:events.k8s.io/v1beta1:EventPatch": "EventPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "extensions/v1beta1",
  "fqn": "pulumi_kubernetes.extensions.v1beta1",
  "classes": {
   "kubernetes:extensions/v1beta1:DaemonSet": "DaemonSet",
   "kubernetes:extensions/v1beta1:DaemonSetList": "DaemonSetList",
   "kubernetes:extensions/v1beta1:DaemonSetPatch": "DaemonSetPatch",
   "kubernetes:extensions/v1beta1:Deployment": "Deployment",
   "kubernetes:extensions/v1beta1:DeploymentList": "DeploymentList",
   "kubernetes:extensions/v1beta1:DeploymentPatch": "DeploymentPatch",
   "kubernetes:extensions/v1beta1:Ingress": "Ingress",
   "kubernetes:extensions/v1beta1:IngressList": "IngressList",
   "kubernetes:extensions/v1beta1:IngressPatch": "IngressPatch",
   "kubernetes:extensions/v1beta1:NetworkPolicy": "NetworkPolicy",
   "kubernetes:extensions/v1beta1:NetworkPolicyList": "NetworkPolicyList",
   "kubernetes:extensions/v1beta1:NetworkPolicyPatch": "NetworkPolicyPatch",
   "kubernetes:extensions/v1beta1:PodSecurityPolicy": "PodSecurityPolicy",
   "kubernetes:extensions/v1beta1:PodSecurityPolicyList": "PodSecurityPolicyList",
   "kubernetes:extensions/v1beta1:PodSecurityPolicyPatch": "PodSecurityPolicyPatch",
   "kubernetes:extensions/v1beta1:ReplicaSet": "ReplicaSet",
   "kubernetes:extensions/v1beta1:ReplicaSetList": "ReplicaSetList",
   "kubernetes:extensions/v1beta1:ReplicaSetPatch": "ReplicaSetPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "flowcontrol.apiserver.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.flowcontrol.v1alpha1",
  "classes": {
   "kubernetes:flowcontrol.apiserver.k8s.io/v1alpha1:FlowSchema": "FlowSchema",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1alpha1:FlowSchemaList": "FlowSchemaList",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1alpha1:FlowSchemaPatch": "FlowSchemaPatch",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1alpha1:PriorityLevelConfiguration": "PriorityLevelConfiguration",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1alpha1:PriorityLevelConfigurationList": "PriorityLevelConfigurationList",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1alpha1:PriorityLevelConfigurationPatch": "PriorityLevelConfigurationPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "flowcontrol.apiserver.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.flowcontrol.v1beta1",
  "classes": {
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta1:FlowSchema": "FlowSchema",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta1:FlowSchemaList": "FlowSchemaList",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta1:FlowSchemaPatch": "FlowSchemaPatch",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta1:PriorityLevelConfiguration": "PriorityLevelConfiguration",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta1:PriorityLevelConfigurationList": "PriorityLevelConfigurationList",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta1:PriorityLevelConfigurationPatch": "PriorityLevelConfigurationPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "flowcontrol.apiserver.k8s.io/v1beta2",
  "fqn": "pulumi_kubernetes.flowcontrol.v1beta2",
  "classes": {
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta2:FlowSchema": "FlowSchema",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta2:FlowSchemaList": "FlowSchemaList",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta2:FlowSchemaPatch": "FlowSchemaPatch",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta2:PriorityLevelConfiguration": "PriorityLevelConfiguration",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta2:PriorityLevelConfigurationList": "PriorityLevelConfigurationList",
   "kubernetes:flowcontrol.apiserver.k8s.io/v1beta2:PriorityLevelConfigurationPatch": "PriorityLevelConfigurationPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "helm.sh/v3",
  "fqn": "pulumi_kubernetes.helm.v3",
  "classes": {
   "kubernetes:helm.sh/v3:Release": "Release"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "meta/v1",
  "fqn": "pulumi_kubernetes.meta.v1",
  "classes": {
   "kubernetes:meta/v1:Status": "Status",
   "kubernetes:meta/v1:StatusPatch": "StatusPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "networking.k8s.io/v1",
  "fqn": "pulumi_kubernetes.networking.v1",
  "classes": {
   "kubernetes:networking.k8s.io/v1:Ingress": "Ingress",
   "kubernetes:networking.k8s.io/v1:IngressClass": "IngressClass",
   "kubernetes:networking.k8s.io/v1:IngressClassList": "IngressClassList",
   "kubernetes:networking.k8s.io/v1:IngressClassPatch": "IngressClassPatch",
   "kubernetes:networking.k8s.io/v1:IngressList": "IngressList",
   "kubernetes:networking.k8s.io/v1:IngressPatch": "IngressPatch",
   "kubernetes:networking.k8s.io/v1:NetworkPolicy": "NetworkPolicy",
   "kubernetes:networking.k8s.io/v1:NetworkPolicyList": "NetworkPolicyList",
   "kubernetes:networking.k8s.io/v1:NetworkPolicyPatch": "NetworkPolicyPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "networking.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.networking.v1alpha1",
  "classes": {
   "kubernetes:networking.k8s.io/v1alpha1:ClusterCIDR": "ClusterCIDR",
   "kubernetes:networking.k8s.io/v1alpha1:ClusterCIDRList": "ClusterCIDRList",
   "kubernetes:networking.k8s.io/v1alpha1:ClusterCIDRPatch": "ClusterCIDRPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "networking.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.networking.v1beta1",
  "classes": {
   "kubernetes:networking.k8s.io/v1beta1:Ingress": "Ingress",
   "kubernetes:networking.k8s.io/v1beta1:IngressClass": "IngressClass",
   "kubernetes:networking.k8s.io/v1beta1:IngressClassList": "IngressClassList",
   "kubernetes:networking.k8s.io/v1beta1:IngressClassPatch": "IngressClassPatch",
   "kubernetes:networking.k8s.io/v1beta1:IngressList": "IngressList",
   "kubernetes:networking.k8s.io/v1beta1:IngressPatch": "IngressPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "node.k8s.io/v1",
  "fqn": "pulumi_kubernetes.node.v1",
  "classes": {
   "kubernetes:node.k8s.io/v1:RuntimeClass": "RuntimeClass",
   "kubernetes:node.k8s.io/v1:RuntimeClassList": "RuntimeClassList",
   "kubernetes:node.k8s.io/v1:RuntimeClassPatch": "RuntimeClassPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "node.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.node.v1alpha1",
  "classes": {
   "kubernetes:node.k8s.io/v1alpha1:RuntimeClass": "RuntimeClass",
   "kubernetes:node.k8s.io/v1alpha1:RuntimeClassList": "RuntimeClassList",
   "kubernetes:node.k8s.io/v1alpha1:RuntimeClassPatch": "RuntimeClassPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "node.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.node.v1beta1",
  "classes": {
   "kubernetes:node.k8s.io/v1beta1:RuntimeClass": "RuntimeClass",
   "kubernetes:node.k8s.io/v1beta1:RuntimeClassList": "RuntimeClassList",
   "kubernetes:node.k8s.io/v1beta1:RuntimeClassPatch": "RuntimeClassPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "policy/v1",
  "fqn": "pulumi_kubernetes.policy.v1",
  "classes": {
   "kubernetes:policy/v1:PodDisruptionBudget": "PodDisruptionBudget",
   "kubernetes:policy/v1:PodDisruptionBudgetList": "PodDisruptionBudgetList",
   "kubernetes:policy/v1:PodDisruptionBudgetPatch": "PodDisruptionBudgetPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "policy/v1beta1",
  "fqn": "pulumi_kubernetes.policy.v1beta1",
  "classes": {
   "kubernetes:policy/v1beta1:PodDisruptionBudget": "PodDisruptionBudget",
   "kubernetes:policy/v1beta1:PodDisruptionBudgetList": "PodDisruptionBudgetList",
   "kubernetes:policy/v1beta1:PodDisruptionBudgetPatch": "PodDisruptionBudgetPatch",
   "kubernetes:policy/v1beta1:PodSecurityPolicy": "PodSecurityPolicy",
   "kubernetes:policy/v1beta1:PodSecurityPolicyList": "PodSecurityPolicyList",
   "kubernetes:policy/v1beta1:PodSecurityPolicyPatch": "PodSecurityPolicyPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "rbac.authorization.k8s.io/v1",
  "fqn": "pulumi_kubernetes.rbac.v1",
  "classes": {
   "kubernetes:rbac.authorization.k8s.io/v1:ClusterRole": "ClusterRole",
   "kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding": "ClusterRoleBinding",
   "kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBindingList": "ClusterRoleBindingList",
   "kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBindingPatch": "ClusterRoleBindingPatch",
   "kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleList": "ClusterRoleList",
   "kubernetes:rbac.authorization.k8s.io/v1:ClusterRolePatch": "ClusterRolePatch",
   "kubernetes:rbac.authorization.k8s.io/v1:Role": "Role",
   "kubernetes:rbac.authorization.k8s.io/v1:RoleBinding": "RoleBinding",
   "kubernetes:rbac.authorization.k8s.io/v1:RoleBindingList": "RoleBindingList",
   "kubernetes:rbac.authorization.k8s.io/v1:RoleBindingPatch": "RoleBindingPatch",
   "kubernetes:rbac.authorization.k8s.io/v1:RoleList": "RoleList",
   "kubernetes:rbac.authorization.k8s.io/v1:RolePatch": "RolePatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "rbac.authorization.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.rbac.v1alpha1",
  "classes": {
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:ClusterRole": "ClusterRole",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:ClusterRoleBinding": "ClusterRoleBinding",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:ClusterRoleBindingList": "ClusterRoleBindingList",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:ClusterRoleBindingPatch": "ClusterRoleBindingPatch",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:ClusterRoleList": "ClusterRoleList",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:ClusterRolePatch": "ClusterRolePatch",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:Role": "Role",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:RoleBinding": "RoleBinding",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:RoleBindingList": "RoleBindingList",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:RoleBindingPatch": "RoleBindingPatch",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:RoleList": "RoleList",
   "kubernetes:rbac.authorization.k8s.io/v1alpha1:RolePatch": "RolePatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "rbac.authorization.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.rbac.v1beta1",
  "classes": {
   "kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRole": "ClusterRole",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRoleBinding": "ClusterRoleBinding",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRoleBindingList": "ClusterRoleBindingList",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRoleBindingPatch": "ClusterRoleBindingPatch",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRoleList": "ClusterRoleList",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRolePatch": "ClusterRolePatch",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:Role": "Role",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:RoleBinding": "RoleBinding",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:RoleBindingList": "RoleBindingList",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:RoleBindingPatch": "RoleBindingPatch",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:RoleList": "RoleList",
   "kubernetes:rbac.authorization.k8s.io/v1beta1:RolePatch": "RolePatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "scheduling.k8s.io/v1",
  "fqn": "pulumi_kubernetes.scheduling.v1",
  "classes": {
   "kubernetes:scheduling.k8s.io/v1:PriorityClass": "PriorityClass",
   "kubernetes:scheduling.k8s.io/v1:PriorityClassList": "PriorityClassList",
   "kubernetes:scheduling.k8s.io/v1:PriorityClassPatch": "PriorityClassPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "scheduling.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.scheduling.v1alpha1",
  "classes": {
   "kubernetes:scheduling.k8s.io/v1alpha1:PriorityClass": "PriorityClass",
   "kubernetes:scheduling.k8s.io/v1alpha1:PriorityClassList": "PriorityClassList",
   "kubernetes:scheduling.k8s.io/v1alpha1:PriorityClassPatch": "PriorityClassPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "scheduling.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.scheduling.v1beta1",
  "classes": {
   "kubernetes:scheduling.k8s.io/v1beta1:PriorityClass": "PriorityClass",
   "kubernetes:scheduling.k8s.io/v1beta1:PriorityClassList": "PriorityClassList",
   "kubernetes:scheduling.k8s.io/v1beta1:PriorityClassPatch": "PriorityClassPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "settings.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.settings.v1alpha1",
  "classes": {
   "kubernetes:settings.k8s.io/v1alpha1:PodPreset": "PodPreset",
   "kubernetes:settings.k8s.io/v1alpha1:PodPresetList": "PodPresetList",
   "kubernetes:settings.k8s.io/v1alpha1:PodPresetPatch": "PodPresetPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "storage.k8s.io/v1",
  "fqn": "pulumi_kubernetes.storage.v1",
  "classes": {
   "kubernetes:storage.k8s.io/v1:CSIDriver": "CSIDriver",
   "kubernetes:storage.k8s.io/v1:CSIDriverList": "CSIDriverList",
   "kubernetes:storage.k8s.io/v1:CSIDriverPatch": "CSIDriverPatch",
   "kubernetes:storage.k8s.io/v1:CSINode": "CSINode",
   "kubernetes:storage.k8s.io/v1:CSINodeList": "CSINodeList",
   "kubernetes:storage.k8s.io/v1:CSINodePatch": "CSINodePatch",
   "kubernetes:storage.k8s.io/v1:CSIStorageCapacity": "CSIStorageCapacity",
   "kubernetes:storage.k8s.io/v1:CSIStorageCapacityList": "CSIStorageCapacityList",
   "kubernetes:storage.k8s.io/v1:CSIStorageCapacityPatch": "CSIStorageCapacityPatch",
   "kubernetes:storage.k8s.io/v1:StorageClass": "StorageClass",
   "kubernetes:storage.k8s.io/v1:StorageClassList": "StorageClassList",
   "kubernetes:storage.k8s.io/v1:StorageClassPatch": "StorageClassPatch",
   "kubernetes:storage.k8s.io/v1:VolumeAttachment": "VolumeAttachment",
   "kubernetes:storage.k8s.io/v1:VolumeAttachmentList": "VolumeAttachmentList",
   "kubernetes:storage.k8s.io/v1:VolumeAttachmentPatch": "VolumeAttachmentPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "storage.k8s.io/v1alpha1",
  "fqn": "pulumi_kubernetes.storage.v1alpha1",
  "classes": {
   "kubernetes:storage.k8s.io/v1alpha1:VolumeAttachment": "VolumeAttachment",
   "kubernetes:storage.k8s.io/v1alpha1:VolumeAttachmentList": "VolumeAttachmentList",
   "kubernetes:storage.k8s.io/v1alpha1:VolumeAttachmentPatch": "VolumeAttachmentPatch"
  }
 },
 {
  "pkg": "kubernetes",
  "mod": "storage.k8s.io/v1beta1",
  "fqn": "pulumi_kubernetes.storage.v1beta1",
  "classes": {
   "kubernetes:storage.k8s.io/v1beta1:CSIDriver": "CSIDriver",
   "kubernetes:storage.k8s.io/v1beta1:CSIDriverList": "CSIDriverList",
   "kubernetes:storage.k8s.io/v1beta1:CSIDriverPatch": "CSIDriverPatch",
   "kubernetes:storage.k8s.io/v1beta1:CSINode": "CSINode",
   "kubernetes:storage.k8s.io/v1beta1:CSINodeList": "CSINodeList",
   "kubernetes:storage.k8s.io/v1beta1:CSINodePatch": "CSINodePatch",
   "kubernetes:storage.k8s.io/v1beta1:CSIStorageCapacity": "CSIStorageCapacity",
   "kubernetes:storage.k8s.io/v1beta1:CSIStorageCapacityList": "CSIStorageCapacityList",
   "kubernetes:storage.k8s.io/v1beta1:CSIStorageCapacityPatch": "CSIStorageCapacityPatch",
   "kubernetes:storage.k8s.io/v1beta1:StorageClass": "StorageClass",
   "kubernetes:storage.k8s.io/v1beta1:StorageClassList": "StorageClassList",
   "kubernetes:storage.k8s.io/v1beta1:StorageClassPatch": "StorageClassPatch",
   "kubernetes:storage.k8s.io/v1beta1:VolumeAttachment": "VolumeAttachment",
   "kubernetes:storage.k8s.io/v1beta1:VolumeAttachmentList": "VolumeAttachmentList",
   "kubernetes:storage.k8s.io/v1beta1:VolumeAttachmentPatch": "VolumeAttachmentPatch"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "kubernetes",
  "token": "pulumi:providers:kubernetes",
  "fqn": "pulumi_kubernetes",
  "class": "Provider"
 }
]
"""
)
