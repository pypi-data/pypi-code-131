# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AclAttachmentArgs', 'AclAttachment']

@pulumi.input_type
class AclAttachmentArgs:
    def __init__(__self__, *,
                 acl_id: pulumi.Input[str],
                 acl_type: pulumi.Input[str],
                 listener_id: pulumi.Input[str],
                 dry_run: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a AclAttachment resource.
        :param pulumi.Input[str] acl_id: The ID of an ACL.
        :param pulumi.Input[str] acl_type: The type of the ACL. Valid values: `white`, `black`. 
               - `white`: Only requests from IP addresses or address segments in the selected access control list are forwarded. The whitelist applies to scenarios where applications only allow specific IP addresses. There are certain business risks in setting up a whitelist. Once the whitelist is set, only the IP addresses in the whitelist can access global acceleration listeners. If whitelist access is enabled, but no IP is added to the access policy group, the global acceleration listener will not forward the request.
               - `black`: All requests from IP addresses or address segments in the selected access control list are not forwarded. Blacklists are applicable to scenarios where applications restrict access to specific IP addresses. If blacklist access is enabled and no IP is added to the access policy group, the global acceleration listener forwards all requests.
        :param pulumi.Input[str] listener_id: The ID of the listener.
        :param pulumi.Input[bool] dry_run: The dry run.
        """
        pulumi.set(__self__, "acl_id", acl_id)
        pulumi.set(__self__, "acl_type", acl_type)
        pulumi.set(__self__, "listener_id", listener_id)
        if dry_run is not None:
            pulumi.set(__self__, "dry_run", dry_run)

    @property
    @pulumi.getter(name="aclId")
    def acl_id(self) -> pulumi.Input[str]:
        """
        The ID of an ACL.
        """
        return pulumi.get(self, "acl_id")

    @acl_id.setter
    def acl_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_id", value)

    @property
    @pulumi.getter(name="aclType")
    def acl_type(self) -> pulumi.Input[str]:
        """
        The type of the ACL. Valid values: `white`, `black`. 
        - `white`: Only requests from IP addresses or address segments in the selected access control list are forwarded. The whitelist applies to scenarios where applications only allow specific IP addresses. There are certain business risks in setting up a whitelist. Once the whitelist is set, only the IP addresses in the whitelist can access global acceleration listeners. If whitelist access is enabled, but no IP is added to the access policy group, the global acceleration listener will not forward the request.
        - `black`: All requests from IP addresses or address segments in the selected access control list are not forwarded. Blacklists are applicable to scenarios where applications restrict access to specific IP addresses. If blacklist access is enabled and no IP is added to the access policy group, the global acceleration listener forwards all requests.
        """
        return pulumi.get(self, "acl_type")

    @acl_type.setter
    def acl_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_type", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Input[str]:
        """
        The ID of the listener.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> Optional[pulumi.Input[bool]]:
        """
        The dry run.
        """
        return pulumi.get(self, "dry_run")

    @dry_run.setter
    def dry_run(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dry_run", value)


@pulumi.input_type
class _AclAttachmentState:
    def __init__(__self__, *,
                 acl_id: Optional[pulumi.Input[str]] = None,
                 acl_type: Optional[pulumi.Input[str]] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AclAttachment resources.
        :param pulumi.Input[str] acl_id: The ID of an ACL.
        :param pulumi.Input[str] acl_type: The type of the ACL. Valid values: `white`, `black`. 
               - `white`: Only requests from IP addresses or address segments in the selected access control list are forwarded. The whitelist applies to scenarios where applications only allow specific IP addresses. There are certain business risks in setting up a whitelist. Once the whitelist is set, only the IP addresses in the whitelist can access global acceleration listeners. If whitelist access is enabled, but no IP is added to the access policy group, the global acceleration listener will not forward the request.
               - `black`: All requests from IP addresses or address segments in the selected access control list are not forwarded. Blacklists are applicable to scenarios where applications restrict access to specific IP addresses. If blacklist access is enabled and no IP is added to the access policy group, the global acceleration listener forwards all requests.
        :param pulumi.Input[bool] dry_run: The dry run.
        :param pulumi.Input[str] listener_id: The ID of the listener.
        :param pulumi.Input[str] status: The status of the resource.
        """
        if acl_id is not None:
            pulumi.set(__self__, "acl_id", acl_id)
        if acl_type is not None:
            pulumi.set(__self__, "acl_type", acl_type)
        if dry_run is not None:
            pulumi.set(__self__, "dry_run", dry_run)
        if listener_id is not None:
            pulumi.set(__self__, "listener_id", listener_id)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="aclId")
    def acl_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of an ACL.
        """
        return pulumi.get(self, "acl_id")

    @acl_id.setter
    def acl_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_id", value)

    @property
    @pulumi.getter(name="aclType")
    def acl_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the ACL. Valid values: `white`, `black`. 
        - `white`: Only requests from IP addresses or address segments in the selected access control list are forwarded. The whitelist applies to scenarios where applications only allow specific IP addresses. There are certain business risks in setting up a whitelist. Once the whitelist is set, only the IP addresses in the whitelist can access global acceleration listeners. If whitelist access is enabled, but no IP is added to the access policy group, the global acceleration listener will not forward the request.
        - `black`: All requests from IP addresses or address segments in the selected access control list are not forwarded. Blacklists are applicable to scenarios where applications restrict access to specific IP addresses. If blacklist access is enabled and no IP is added to the access policy group, the global acceleration listener forwards all requests.
        """
        return pulumi.get(self, "acl_type")

    @acl_type.setter
    def acl_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_type", value)

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> Optional[pulumi.Input[bool]]:
        """
        The dry run.
        """
        return pulumi.get(self, "dry_run")

    @dry_run.setter
    def dry_run(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dry_run", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the listener.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the resource.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class AclAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_id: Optional[pulumi.Input[str]] = None,
                 acl_type: Optional[pulumi.Input[str]] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Global Accelerator (GA) Acl Attachment resource.

        For information about Global Accelerator (GA) Acl Attachment and how to use it, see [What is Acl Attachment](https://www.alibabacloud.com/help/en/doc-detail/258295.html).

        > **NOTE:** Available in v1.150.0+.

        ## Import

        Global Accelerator (GA) Acl Attachment can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ga/aclAttachment:AclAttachment example <listener_id>:<acl_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_id: The ID of an ACL.
        :param pulumi.Input[str] acl_type: The type of the ACL. Valid values: `white`, `black`. 
               - `white`: Only requests from IP addresses or address segments in the selected access control list are forwarded. The whitelist applies to scenarios where applications only allow specific IP addresses. There are certain business risks in setting up a whitelist. Once the whitelist is set, only the IP addresses in the whitelist can access global acceleration listeners. If whitelist access is enabled, but no IP is added to the access policy group, the global acceleration listener will not forward the request.
               - `black`: All requests from IP addresses or address segments in the selected access control list are not forwarded. Blacklists are applicable to scenarios where applications restrict access to specific IP addresses. If blacklist access is enabled and no IP is added to the access policy group, the global acceleration listener forwards all requests.
        :param pulumi.Input[bool] dry_run: The dry run.
        :param pulumi.Input[str] listener_id: The ID of the listener.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AclAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Global Accelerator (GA) Acl Attachment resource.

        For information about Global Accelerator (GA) Acl Attachment and how to use it, see [What is Acl Attachment](https://www.alibabacloud.com/help/en/doc-detail/258295.html).

        > **NOTE:** Available in v1.150.0+.

        ## Import

        Global Accelerator (GA) Acl Attachment can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ga/aclAttachment:AclAttachment example <listener_id>:<acl_id>
        ```

        :param str resource_name: The name of the resource.
        :param AclAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AclAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_id: Optional[pulumi.Input[str]] = None,
                 acl_type: Optional[pulumi.Input[str]] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AclAttachmentArgs.__new__(AclAttachmentArgs)

            if acl_id is None and not opts.urn:
                raise TypeError("Missing required property 'acl_id'")
            __props__.__dict__["acl_id"] = acl_id
            if acl_type is None and not opts.urn:
                raise TypeError("Missing required property 'acl_type'")
            __props__.__dict__["acl_type"] = acl_type
            __props__.__dict__["dry_run"] = dry_run
            if listener_id is None and not opts.urn:
                raise TypeError("Missing required property 'listener_id'")
            __props__.__dict__["listener_id"] = listener_id
            __props__.__dict__["status"] = None
        super(AclAttachment, __self__).__init__(
            'alicloud:ga/aclAttachment:AclAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acl_id: Optional[pulumi.Input[str]] = None,
            acl_type: Optional[pulumi.Input[str]] = None,
            dry_run: Optional[pulumi.Input[bool]] = None,
            listener_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'AclAttachment':
        """
        Get an existing AclAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_id: The ID of an ACL.
        :param pulumi.Input[str] acl_type: The type of the ACL. Valid values: `white`, `black`. 
               - `white`: Only requests from IP addresses or address segments in the selected access control list are forwarded. The whitelist applies to scenarios where applications only allow specific IP addresses. There are certain business risks in setting up a whitelist. Once the whitelist is set, only the IP addresses in the whitelist can access global acceleration listeners. If whitelist access is enabled, but no IP is added to the access policy group, the global acceleration listener will not forward the request.
               - `black`: All requests from IP addresses or address segments in the selected access control list are not forwarded. Blacklists are applicable to scenarios where applications restrict access to specific IP addresses. If blacklist access is enabled and no IP is added to the access policy group, the global acceleration listener forwards all requests.
        :param pulumi.Input[bool] dry_run: The dry run.
        :param pulumi.Input[str] listener_id: The ID of the listener.
        :param pulumi.Input[str] status: The status of the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AclAttachmentState.__new__(_AclAttachmentState)

        __props__.__dict__["acl_id"] = acl_id
        __props__.__dict__["acl_type"] = acl_type
        __props__.__dict__["dry_run"] = dry_run
        __props__.__dict__["listener_id"] = listener_id
        __props__.__dict__["status"] = status
        return AclAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aclId")
    def acl_id(self) -> pulumi.Output[str]:
        """
        The ID of an ACL.
        """
        return pulumi.get(self, "acl_id")

    @property
    @pulumi.getter(name="aclType")
    def acl_type(self) -> pulumi.Output[str]:
        """
        The type of the ACL. Valid values: `white`, `black`. 
        - `white`: Only requests from IP addresses or address segments in the selected access control list are forwarded. The whitelist applies to scenarios where applications only allow specific IP addresses. There are certain business risks in setting up a whitelist. Once the whitelist is set, only the IP addresses in the whitelist can access global acceleration listeners. If whitelist access is enabled, but no IP is added to the access policy group, the global acceleration listener will not forward the request.
        - `black`: All requests from IP addresses or address segments in the selected access control list are not forwarded. Blacklists are applicable to scenarios where applications restrict access to specific IP addresses. If blacklist access is enabled and no IP is added to the access policy group, the global acceleration listener forwards all requests.
        """
        return pulumi.get(self, "acl_type")

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> pulumi.Output[Optional[bool]]:
        """
        The dry run.
        """
        return pulumi.get(self, "dry_run")

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Output[str]:
        """
        The ID of the listener.
        """
        return pulumi.get(self, "listener_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the resource.
        """
        return pulumi.get(self, "status")

