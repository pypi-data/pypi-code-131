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
    'GetDeviceResult',
    'AwaitableGetDeviceResult',
    'get_device',
    'get_device_output',
]

@pulumi.output_type
class GetDeviceResult:
    def __init__(__self__, blocked=None, config=None, credentials=None, gateway_config=None, last_config_ack_time=None, last_config_send_time=None, last_error_status=None, last_error_time=None, last_event_time=None, last_heartbeat_time=None, last_state_time=None, log_level=None, metadata=None, name=None, num_id=None, state=None):
        if blocked and not isinstance(blocked, bool):
            raise TypeError("Expected argument 'blocked' to be a bool")
        pulumi.set(__self__, "blocked", blocked)
        if config and not isinstance(config, dict):
            raise TypeError("Expected argument 'config' to be a dict")
        pulumi.set(__self__, "config", config)
        if credentials and not isinstance(credentials, list):
            raise TypeError("Expected argument 'credentials' to be a list")
        pulumi.set(__self__, "credentials", credentials)
        if gateway_config and not isinstance(gateway_config, dict):
            raise TypeError("Expected argument 'gateway_config' to be a dict")
        pulumi.set(__self__, "gateway_config", gateway_config)
        if last_config_ack_time and not isinstance(last_config_ack_time, str):
            raise TypeError("Expected argument 'last_config_ack_time' to be a str")
        pulumi.set(__self__, "last_config_ack_time", last_config_ack_time)
        if last_config_send_time and not isinstance(last_config_send_time, str):
            raise TypeError("Expected argument 'last_config_send_time' to be a str")
        pulumi.set(__self__, "last_config_send_time", last_config_send_time)
        if last_error_status and not isinstance(last_error_status, dict):
            raise TypeError("Expected argument 'last_error_status' to be a dict")
        pulumi.set(__self__, "last_error_status", last_error_status)
        if last_error_time and not isinstance(last_error_time, str):
            raise TypeError("Expected argument 'last_error_time' to be a str")
        pulumi.set(__self__, "last_error_time", last_error_time)
        if last_event_time and not isinstance(last_event_time, str):
            raise TypeError("Expected argument 'last_event_time' to be a str")
        pulumi.set(__self__, "last_event_time", last_event_time)
        if last_heartbeat_time and not isinstance(last_heartbeat_time, str):
            raise TypeError("Expected argument 'last_heartbeat_time' to be a str")
        pulumi.set(__self__, "last_heartbeat_time", last_heartbeat_time)
        if last_state_time and not isinstance(last_state_time, str):
            raise TypeError("Expected argument 'last_state_time' to be a str")
        pulumi.set(__self__, "last_state_time", last_state_time)
        if log_level and not isinstance(log_level, str):
            raise TypeError("Expected argument 'log_level' to be a str")
        pulumi.set(__self__, "log_level", log_level)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if num_id and not isinstance(num_id, str):
            raise TypeError("Expected argument 'num_id' to be a str")
        pulumi.set(__self__, "num_id", num_id)
        if state and not isinstance(state, dict):
            raise TypeError("Expected argument 'state' to be a dict")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def blocked(self) -> bool:
        """
        If a device is blocked, connections or requests from this device will fail. Can be used to temporarily prevent the device from connecting if, for example, the sensor is generating bad data and needs maintenance.
        """
        return pulumi.get(self, "blocked")

    @property
    @pulumi.getter
    def config(self) -> 'outputs.DeviceConfigResponse':
        """
        The most recent device configuration, which is eventually sent from Cloud IoT Core to the device. If not present on creation, the configuration will be initialized with an empty payload and version value of `1`. To update this field after creation, use the `DeviceManager.ModifyCloudToDeviceConfig` method.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def credentials(self) -> Sequence['outputs.DeviceCredentialResponse']:
        """
        The credentials used to authenticate this device. To allow credential rotation without interruption, multiple device credentials can be bound to this device. No more than 3 credentials can be bound to a single device at a time. When new credentials are added to a device, they are verified against the registry credentials. For details, see the description of the `DeviceRegistry.credentials` field.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="gatewayConfig")
    def gateway_config(self) -> 'outputs.GatewayConfigResponse':
        """
        Gateway-related configuration and state.
        """
        return pulumi.get(self, "gateway_config")

    @property
    @pulumi.getter(name="lastConfigAckTime")
    def last_config_ack_time(self) -> str:
        """
        [Output only] The last time a cloud-to-device config version acknowledgment was received from the device. This field is only for configurations sent through MQTT.
        """
        return pulumi.get(self, "last_config_ack_time")

    @property
    @pulumi.getter(name="lastConfigSendTime")
    def last_config_send_time(self) -> str:
        """
        [Output only] The last time a cloud-to-device config version was sent to the device.
        """
        return pulumi.get(self, "last_config_send_time")

    @property
    @pulumi.getter(name="lastErrorStatus")
    def last_error_status(self) -> 'outputs.StatusResponse':
        """
        [Output only] The error message of the most recent error, such as a failure to publish to Cloud Pub/Sub. 'last_error_time' is the timestamp of this field. If no errors have occurred, this field has an empty message and the status code 0 == OK. Otherwise, this field is expected to have a status code other than OK.
        """
        return pulumi.get(self, "last_error_status")

    @property
    @pulumi.getter(name="lastErrorTime")
    def last_error_time(self) -> str:
        """
        [Output only] The time the most recent error occurred, such as a failure to publish to Cloud Pub/Sub. This field is the timestamp of 'last_error_status'.
        """
        return pulumi.get(self, "last_error_time")

    @property
    @pulumi.getter(name="lastEventTime")
    def last_event_time(self) -> str:
        """
        [Output only] The last time a telemetry event was received. Timestamps are periodically collected and written to storage; they may be stale by a few minutes.
        """
        return pulumi.get(self, "last_event_time")

    @property
    @pulumi.getter(name="lastHeartbeatTime")
    def last_heartbeat_time(self) -> str:
        """
        [Output only] The last time an MQTT `PINGREQ` was received. This field applies only to devices connecting through MQTT. MQTT clients usually only send `PINGREQ` messages if the connection is idle, and no other messages have been sent. Timestamps are periodically collected and written to storage; they may be stale by a few minutes.
        """
        return pulumi.get(self, "last_heartbeat_time")

    @property
    @pulumi.getter(name="lastStateTime")
    def last_state_time(self) -> str:
        """
        [Output only] The last time a state event was received. Timestamps are periodically collected and written to storage; they may be stale by a few minutes.
        """
        return pulumi.get(self, "last_state_time")

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> str:
        """
        **Beta Feature** The logging verbosity for device activity. If unspecified, DeviceRegistry.log_level will be used.
        """
        return pulumi.get(self, "log_level")

    @property
    @pulumi.getter
    def metadata(self) -> Mapping[str, str]:
        """
        The metadata key-value pairs assigned to the device. This metadata is not interpreted or indexed by Cloud IoT Core. It can be used to add contextual information for the device. Keys must conform to the regular expression a-zA-Z+ and be less than 128 bytes in length. Values are free-form strings. Each value must be less than or equal to 32 KB in size. The total size of all keys and values must be less than 256 KB, and the maximum number of key-value pairs is 500.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource path name. For example, `projects/p1/locations/us-central1/registries/registry0/devices/dev0` or `projects/p1/locations/us-central1/registries/registry0/devices/{num_id}`. When `name` is populated as a response from the service, it always ends in the device numeric ID.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numId")
    def num_id(self) -> str:
        """
        [Output only] A server-defined unique numeric ID for the device. This is a more compact way to identify devices, and it is globally unique.
        """
        return pulumi.get(self, "num_id")

    @property
    @pulumi.getter
    def state(self) -> 'outputs.DeviceStateResponse':
        """
        [Output only] The state most recently received from the device. If no state has been reported, this field is not present.
        """
        return pulumi.get(self, "state")


class AwaitableGetDeviceResult(GetDeviceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeviceResult(
            blocked=self.blocked,
            config=self.config,
            credentials=self.credentials,
            gateway_config=self.gateway_config,
            last_config_ack_time=self.last_config_ack_time,
            last_config_send_time=self.last_config_send_time,
            last_error_status=self.last_error_status,
            last_error_time=self.last_error_time,
            last_event_time=self.last_event_time,
            last_heartbeat_time=self.last_heartbeat_time,
            last_state_time=self.last_state_time,
            log_level=self.log_level,
            metadata=self.metadata,
            name=self.name,
            num_id=self.num_id,
            state=self.state)


def get_device(device_id: Optional[str] = None,
               field_mask: Optional[str] = None,
               location: Optional[str] = None,
               project: Optional[str] = None,
               registry_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeviceResult:
    """
    Gets details about a device.
    """
    __args__ = dict()
    __args__['deviceId'] = device_id
    __args__['fieldMask'] = field_mask
    __args__['location'] = location
    __args__['project'] = project
    __args__['registryId'] = registry_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:cloudiot/v1:getDevice', __args__, opts=opts, typ=GetDeviceResult).value

    return AwaitableGetDeviceResult(
        blocked=__ret__.blocked,
        config=__ret__.config,
        credentials=__ret__.credentials,
        gateway_config=__ret__.gateway_config,
        last_config_ack_time=__ret__.last_config_ack_time,
        last_config_send_time=__ret__.last_config_send_time,
        last_error_status=__ret__.last_error_status,
        last_error_time=__ret__.last_error_time,
        last_event_time=__ret__.last_event_time,
        last_heartbeat_time=__ret__.last_heartbeat_time,
        last_state_time=__ret__.last_state_time,
        log_level=__ret__.log_level,
        metadata=__ret__.metadata,
        name=__ret__.name,
        num_id=__ret__.num_id,
        state=__ret__.state)


@_utilities.lift_output_func(get_device)
def get_device_output(device_id: Optional[pulumi.Input[str]] = None,
                      field_mask: Optional[pulumi.Input[Optional[str]]] = None,
                      location: Optional[pulumi.Input[str]] = None,
                      project: Optional[pulumi.Input[Optional[str]]] = None,
                      registry_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeviceResult]:
    """
    Gets details about a device.
    """
    ...
