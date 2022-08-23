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
    'GetPhysicalConnectionsResult',
    'AwaitableGetPhysicalConnectionsResult',
    'get_physical_connections',
    'get_physical_connections_output',
]

@pulumi.output_type
class GetPhysicalConnectionsResult:
    """
    A collection of values returned by getPhysicalConnections.
    """
    def __init__(__self__, connections=None, id=None, ids=None, include_reservation_data=None, name_regex=None, names=None, output_file=None, status=None):
        if connections and not isinstance(connections, list):
            raise TypeError("Expected argument 'connections' to be a list")
        pulumi.set(__self__, "connections", connections)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if include_reservation_data and not isinstance(include_reservation_data, bool):
            raise TypeError("Expected argument 'include_reservation_data' to be a bool")
        pulumi.set(__self__, "include_reservation_data", include_reservation_data)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def connections(self) -> Sequence['outputs.GetPhysicalConnectionsConnectionResult']:
        return pulumi.get(self, "connections")

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
    @pulumi.getter(name="includeReservationData")
    def include_reservation_data(self) -> Optional[bool]:
        return pulumi.get(self, "include_reservation_data")

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
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetPhysicalConnectionsResult(GetPhysicalConnectionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPhysicalConnectionsResult(
            connections=self.connections,
            id=self.id,
            ids=self.ids,
            include_reservation_data=self.include_reservation_data,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            status=self.status)


def get_physical_connections(ids: Optional[Sequence[str]] = None,
                             include_reservation_data: Optional[bool] = None,
                             name_regex: Optional[str] = None,
                             output_file: Optional[str] = None,
                             status: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPhysicalConnectionsResult:
    """
    This data source provides the Express Connect Physical Connections of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.132.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.expressconnect.get_physical_connections(ids=["pc-2345678"])
    pulumi.export("expressConnectPhysicalConnectionId1", ids.connections[0].id)
    name_regex = alicloud.expressconnect.get_physical_connections(name_regex="^my-PhysicalConnection")
    pulumi.export("expressConnectPhysicalConnectionId2", name_regex.connections[0].id)
    ```


    :param Sequence[str] ids: A list of Physical Connection IDs.
    :param bool include_reservation_data: The include reservation data.
    :param str name_regex: A regex string to filter results by Physical Connection name.
    :param str status: Resources on Behalf of a State of the Resource Attribute Field.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['includeReservationData'] = include_reservation_data
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:expressconnect/getPhysicalConnections:getPhysicalConnections', __args__, opts=opts, typ=GetPhysicalConnectionsResult).value

    return AwaitableGetPhysicalConnectionsResult(
        connections=__ret__.connections,
        id=__ret__.id,
        ids=__ret__.ids,
        include_reservation_data=__ret__.include_reservation_data,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        status=__ret__.status)


@_utilities.lift_output_func(get_physical_connections)
def get_physical_connections_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                    include_reservation_data: Optional[pulumi.Input[Optional[bool]]] = None,
                                    name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                    output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                    status: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPhysicalConnectionsResult]:
    """
    This data source provides the Express Connect Physical Connections of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.132.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.expressconnect.get_physical_connections(ids=["pc-2345678"])
    pulumi.export("expressConnectPhysicalConnectionId1", ids.connections[0].id)
    name_regex = alicloud.expressconnect.get_physical_connections(name_regex="^my-PhysicalConnection")
    pulumi.export("expressConnectPhysicalConnectionId2", name_regex.connections[0].id)
    ```


    :param Sequence[str] ids: A list of Physical Connection IDs.
    :param bool include_reservation_data: The include reservation data.
    :param str name_regex: A regex string to filter results by Physical Connection name.
    :param str status: Resources on Behalf of a State of the Resource Attribute Field.
    """
    ...
