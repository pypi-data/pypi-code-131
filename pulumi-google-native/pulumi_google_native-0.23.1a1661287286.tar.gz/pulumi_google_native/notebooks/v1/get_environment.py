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
    'GetEnvironmentResult',
    'AwaitableGetEnvironmentResult',
    'get_environment',
    'get_environment_output',
]

@pulumi.output_type
class GetEnvironmentResult:
    def __init__(__self__, container_image=None, create_time=None, description=None, display_name=None, name=None, post_startup_script=None, vm_image=None):
        if container_image and not isinstance(container_image, dict):
            raise TypeError("Expected argument 'container_image' to be a dict")
        pulumi.set(__self__, "container_image", container_image)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if post_startup_script and not isinstance(post_startup_script, str):
            raise TypeError("Expected argument 'post_startup_script' to be a str")
        pulumi.set(__self__, "post_startup_script", post_startup_script)
        if vm_image and not isinstance(vm_image, dict):
            raise TypeError("Expected argument 'vm_image' to be a dict")
        pulumi.set(__self__, "vm_image", vm_image)

    @property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> 'outputs.ContainerImageResponse':
        """
        Use a container image to start the notebook instance.
        """
        return pulumi.get(self, "container_image")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time at which this environment was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A brief description of this environment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name of this environment for the UI.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of this environment. Format: `projects/{project_id}/locations/{location}/environments/{environment_id}`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="postStartupScript")
    def post_startup_script(self) -> str:
        """
        Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path. Example: `"gs://path-to-file/file-name"`
        """
        return pulumi.get(self, "post_startup_script")

    @property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> 'outputs.VmImageResponse':
        """
        Use a Compute Engine VM image to start the notebook instance.
        """
        return pulumi.get(self, "vm_image")


class AwaitableGetEnvironmentResult(GetEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnvironmentResult(
            container_image=self.container_image,
            create_time=self.create_time,
            description=self.description,
            display_name=self.display_name,
            name=self.name,
            post_startup_script=self.post_startup_script,
            vm_image=self.vm_image)


def get_environment(environment_id: Optional[str] = None,
                    location: Optional[str] = None,
                    project: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnvironmentResult:
    """
    Gets details of a single Environment.
    """
    __args__ = dict()
    __args__['environmentId'] = environment_id
    __args__['location'] = location
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:notebooks/v1:getEnvironment', __args__, opts=opts, typ=GetEnvironmentResult).value

    return AwaitableGetEnvironmentResult(
        container_image=__ret__.container_image,
        create_time=__ret__.create_time,
        description=__ret__.description,
        display_name=__ret__.display_name,
        name=__ret__.name,
        post_startup_script=__ret__.post_startup_script,
        vm_image=__ret__.vm_image)


@_utilities.lift_output_func(get_environment)
def get_environment_output(environment_id: Optional[pulumi.Input[str]] = None,
                           location: Optional[pulumi.Input[str]] = None,
                           project: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnvironmentResult]:
    """
    Gets details of a single Environment.
    """
    ...
