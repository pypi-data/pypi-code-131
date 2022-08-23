# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetKeyPairsPairResult',
]

@pulumi.output_type
class GetKeyPairsPairResult(dict):
    def __init__(__self__, *,
                 create_time: str,
                 id: str,
                 key_pair_finger_print: str,
                 key_pair_name: str,
                 version: str):
        """
        :param str create_time: The creation time of the key pair. The date format is in accordance with ISO8601 notation and uses UTC time. The format is yyyy-MM-ddTHH:mm:ssZ.
        :param str id: The ID of the Key Pair.
        :param str key_pair_finger_print: Fingerprint of the key pair.
        :param str key_pair_name: The name of the key pair.
        :param str version: The version number.
        """
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "key_pair_finger_print", key_pair_finger_print)
        pulumi.set(__self__, "key_pair_name", key_pair_name)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The creation time of the key pair. The date format is in accordance with ISO8601 notation and uses UTC time. The format is yyyy-MM-ddTHH:mm:ssZ.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Key Pair.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyPairFingerPrint")
    def key_pair_finger_print(self) -> str:
        """
        Fingerprint of the key pair.
        """
        return pulumi.get(self, "key_pair_finger_print")

    @property
    @pulumi.getter(name="keyPairName")
    def key_pair_name(self) -> str:
        """
        The name of the key pair.
        """
        return pulumi.get(self, "key_pair_name")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The version number.
        """
        return pulumi.get(self, "version")


