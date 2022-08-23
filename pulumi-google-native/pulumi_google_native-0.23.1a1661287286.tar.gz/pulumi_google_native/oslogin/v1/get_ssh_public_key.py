# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetSshPublicKeyResult',
    'AwaitableGetSshPublicKeyResult',
    'get_ssh_public_key',
    'get_ssh_public_key_output',
]

@pulumi.output_type
class GetSshPublicKeyResult:
    def __init__(__self__, expiration_time_usec=None, fingerprint=None, key=None, name=None):
        if expiration_time_usec and not isinstance(expiration_time_usec, str):
            raise TypeError("Expected argument 'expiration_time_usec' to be a str")
        pulumi.set(__self__, "expiration_time_usec", expiration_time_usec)
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="expirationTimeUsec")
    def expiration_time_usec(self) -> str:
        """
        An expiration time in microseconds since epoch.
        """
        return pulumi.get(self, "expiration_time_usec")

    @property
    @pulumi.getter
    def fingerprint(self) -> str:
        """
        The SHA-256 fingerprint of the SSH public key.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Public key text in SSH format, defined by RFC4253 section 6.6.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The canonical resource name.
        """
        return pulumi.get(self, "name")


class AwaitableGetSshPublicKeyResult(GetSshPublicKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSshPublicKeyResult(
            expiration_time_usec=self.expiration_time_usec,
            fingerprint=self.fingerprint,
            key=self.key,
            name=self.name)


def get_ssh_public_key(ssh_public_key_id: Optional[str] = None,
                       user_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSshPublicKeyResult:
    """
    Retrieves an SSH public key.
    """
    __args__ = dict()
    __args__['sshPublicKeyId'] = ssh_public_key_id
    __args__['userId'] = user_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:oslogin/v1:getSshPublicKey', __args__, opts=opts, typ=GetSshPublicKeyResult).value

    return AwaitableGetSshPublicKeyResult(
        expiration_time_usec=__ret__.expiration_time_usec,
        fingerprint=__ret__.fingerprint,
        key=__ret__.key,
        name=__ret__.name)


@_utilities.lift_output_func(get_ssh_public_key)
def get_ssh_public_key_output(ssh_public_key_id: Optional[pulumi.Input[str]] = None,
                              user_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSshPublicKeyResult]:
    """
    Retrieves an SSH public key.
    """
    ...
