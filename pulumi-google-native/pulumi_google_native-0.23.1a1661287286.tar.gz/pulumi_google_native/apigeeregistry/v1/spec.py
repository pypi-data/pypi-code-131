# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['SpecArgs', 'Spec']

@pulumi.input_type
class SpecArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 api_spec_id: pulumi.Input[str],
                 version_id: pulumi.Input[str],
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 contents: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filename: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mime_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 source_uri: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Spec resource.
        :param pulumi.Input[str] api_spec_id: Required. The ID to use for the spec, which will become the final component of the spec's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts.
        :param pulumi.Input[str] contents: Input only. The contents of the spec. Provided by API callers when specs are created or updated. To access the contents of a spec, use GetApiSpecContents.
        :param pulumi.Input[str] description: A detailed description.
        :param pulumi.Input[str] filename: A possibly-hierarchical name used to refer to the spec from other specs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "apigeeregistry.googleapis.com/" and cannot be changed.
        :param pulumi.Input[str] mime_type: A style (format) descriptor for this spec that is specified as a Media Type (https://en.wikipedia.org/wiki/Media_type). Possible values include "application/vnd.apigee.proto", "application/vnd.apigee.openapi", and "application/vnd.apigee.graphql", with possible suffixes representing compression types. These hypothetical names are defined in the vendor tree defined in RFC6838 (https://tools.ietf.org/html/rfc6838) and are not final. Content types can specify compression. Currently only GZip compression is supported (indicated with "+gzip").
        :param pulumi.Input[str] name: Resource name.
        :param pulumi.Input[str] source_uri: The original source URI of the spec (if one exists). This is an external location that can be used for reference purposes but which may not be authoritative since this external resource may change after the spec is retrieved.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "api_spec_id", api_spec_id)
        pulumi.set(__self__, "version_id", version_id)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if contents is not None:
            pulumi.set(__self__, "contents", contents)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if filename is not None:
            pulumi.set(__self__, "filename", filename)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mime_type is not None:
            pulumi.set(__self__, "mime_type", mime_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if source_uri is not None:
            pulumi.set(__self__, "source_uri", source_uri)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter(name="apiSpecId")
    def api_spec_id(self) -> pulumi.Input[str]:
        """
        Required. The ID to use for the spec, which will become the final component of the spec's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.
        """
        return pulumi.get(self, "api_spec_id")

    @api_spec_id.setter
    def api_spec_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_spec_id", value)

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "version_id")

    @version_id.setter
    def version_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "version_id", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts.
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter
    def contents(self) -> Optional[pulumi.Input[str]]:
        """
        Input only. The contents of the spec. Provided by API callers when specs are created or updated. To access the contents of a spec, use GetApiSpecContents.
        """
        return pulumi.get(self, "contents")

    @contents.setter
    def contents(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contents", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A detailed description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def filename(self) -> Optional[pulumi.Input[str]]:
        """
        A possibly-hierarchical name used to refer to the spec from other specs.
        """
        return pulumi.get(self, "filename")

    @filename.setter
    def filename(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filename", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "apigeeregistry.googleapis.com/" and cannot be changed.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> Optional[pulumi.Input[str]]:
        """
        A style (format) descriptor for this spec that is specified as a Media Type (https://en.wikipedia.org/wiki/Media_type). Possible values include "application/vnd.apigee.proto", "application/vnd.apigee.openapi", and "application/vnd.apigee.graphql", with possible suffixes representing compression types. These hypothetical names are defined in the vendor tree defined in RFC6838 (https://tools.ietf.org/html/rfc6838) and are not final. Content types can specify compression. Currently only GZip compression is supported (indicated with "+gzip").
        """
        return pulumi.get(self, "mime_type")

    @mime_type.setter
    def mime_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mime_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="sourceUri")
    def source_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The original source URI of the spec (if one exists). This is an external location that can be used for reference purposes but which may not be authoritative since this external resource may change after the spec is retrieved.
        """
        return pulumi.get(self, "source_uri")

    @source_uri.setter
    def source_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_uri", value)


class Spec(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 api_spec_id: Optional[pulumi.Input[str]] = None,
                 contents: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filename: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mime_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 source_uri: Optional[pulumi.Input[str]] = None,
                 version_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        CreateApiSpec creates a specified spec.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts.
        :param pulumi.Input[str] api_spec_id: Required. The ID to use for the spec, which will become the final component of the spec's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.
        :param pulumi.Input[str] contents: Input only. The contents of the spec. Provided by API callers when specs are created or updated. To access the contents of a spec, use GetApiSpecContents.
        :param pulumi.Input[str] description: A detailed description.
        :param pulumi.Input[str] filename: A possibly-hierarchical name used to refer to the spec from other specs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "apigeeregistry.googleapis.com/" and cannot be changed.
        :param pulumi.Input[str] mime_type: A style (format) descriptor for this spec that is specified as a Media Type (https://en.wikipedia.org/wiki/Media_type). Possible values include "application/vnd.apigee.proto", "application/vnd.apigee.openapi", and "application/vnd.apigee.graphql", with possible suffixes representing compression types. These hypothetical names are defined in the vendor tree defined in RFC6838 (https://tools.ietf.org/html/rfc6838) and are not final. Content types can specify compression. Currently only GZip compression is supported (indicated with "+gzip").
        :param pulumi.Input[str] name: Resource name.
        :param pulumi.Input[str] source_uri: The original source URI of the spec (if one exists). This is an external location that can be used for reference purposes but which may not be authoritative since this external resource may change after the spec is retrieved.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SpecArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        CreateApiSpec creates a specified spec.

        :param str resource_name: The name of the resource.
        :param SpecArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SpecArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 api_spec_id: Optional[pulumi.Input[str]] = None,
                 contents: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filename: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mime_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 source_uri: Optional[pulumi.Input[str]] = None,
                 version_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SpecArgs.__new__(SpecArgs)

            __props__.__dict__["annotations"] = annotations
            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            if api_spec_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_spec_id'")
            __props__.__dict__["api_spec_id"] = api_spec_id
            __props__.__dict__["contents"] = contents
            __props__.__dict__["description"] = description
            __props__.__dict__["filename"] = filename
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["mime_type"] = mime_type
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["source_uri"] = source_uri
            if version_id is None and not opts.urn:
                raise TypeError("Missing required property 'version_id'")
            __props__.__dict__["version_id"] = version_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["hash"] = None
            __props__.__dict__["revision_create_time"] = None
            __props__.__dict__["revision_id"] = None
            __props__.__dict__["revision_update_time"] = None
            __props__.__dict__["size_bytes"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["api_id", "api_spec_id", "location", "project", "version_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Spec, __self__).__init__(
            'google-native:apigeeregistry/v1:Spec',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Spec':
        """
        Get an existing Spec resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SpecArgs.__new__(SpecArgs)

        __props__.__dict__["annotations"] = None
        __props__.__dict__["api_id"] = None
        __props__.__dict__["api_spec_id"] = None
        __props__.__dict__["contents"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["filename"] = None
        __props__.__dict__["hash"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mime_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["revision_create_time"] = None
        __props__.__dict__["revision_id"] = None
        __props__.__dict__["revision_update_time"] = None
        __props__.__dict__["size_bytes"] = None
        __props__.__dict__["source_uri"] = None
        __props__.__dict__["version_id"] = None
        return Spec(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="apiSpecId")
    def api_spec_id(self) -> pulumi.Output[str]:
        """
        Required. The ID to use for the spec, which will become the final component of the spec's resource name. This value should be 4-63 characters, and valid characters are /a-z-/. Following AIP-162, IDs must not have the form of a UUID.
        """
        return pulumi.get(self, "api_spec_id")

    @property
    @pulumi.getter
    def contents(self) -> pulumi.Output[str]:
        """
        Input only. The contents of the spec. Provided by API callers when specs are created or updated. To access the contents of a spec, use GetApiSpecContents.
        """
        return pulumi.get(self, "contents")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Creation timestamp; when the spec resource was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A detailed description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filename(self) -> pulumi.Output[str]:
        """
        A possibly-hierarchical name used to refer to the spec from other specs.
        """
        return pulumi.get(self, "filename")

    @property
    @pulumi.getter
    def hash(self) -> pulumi.Output[str]:
        """
        A SHA-256 hash of the spec's contents. If the spec is gzipped, this is the hash of the uncompressed spec.
        """
        return pulumi.get(self, "hash")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "apigeeregistry.googleapis.com/" and cannot be changed.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> pulumi.Output[str]:
        """
        A style (format) descriptor for this spec that is specified as a Media Type (https://en.wikipedia.org/wiki/Media_type). Possible values include "application/vnd.apigee.proto", "application/vnd.apigee.openapi", and "application/vnd.apigee.graphql", with possible suffixes representing compression types. These hypothetical names are defined in the vendor tree defined in RFC6838 (https://tools.ietf.org/html/rfc6838) and are not final. Content types can specify compression. Currently only GZip compression is supported (indicated with "+gzip").
        """
        return pulumi.get(self, "mime_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="revisionCreateTime")
    def revision_create_time(self) -> pulumi.Output[str]:
        """
        Revision creation timestamp; when the represented revision was created.
        """
        return pulumi.get(self, "revision_create_time")

    @property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> pulumi.Output[str]:
        """
        Immutable. The revision ID of the spec. A new revision is committed whenever the spec contents are changed. The format is an 8-character hexadecimal string.
        """
        return pulumi.get(self, "revision_id")

    @property
    @pulumi.getter(name="revisionUpdateTime")
    def revision_update_time(self) -> pulumi.Output[str]:
        """
        Last update timestamp: when the represented revision was last modified.
        """
        return pulumi.get(self, "revision_update_time")

    @property
    @pulumi.getter(name="sizeBytes")
    def size_bytes(self) -> pulumi.Output[int]:
        """
        The size of the spec file in bytes. If the spec is gzipped, this is the size of the uncompressed spec.
        """
        return pulumi.get(self, "size_bytes")

    @property
    @pulumi.getter(name="sourceUri")
    def source_uri(self) -> pulumi.Output[str]:
        """
        The original source URI of the spec (if one exists). This is an external location that can be used for reference purposes but which may not be authoritative since this external resource may change after the spec is retrieved.
        """
        return pulumi.get(self, "source_uri")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "version_id")

