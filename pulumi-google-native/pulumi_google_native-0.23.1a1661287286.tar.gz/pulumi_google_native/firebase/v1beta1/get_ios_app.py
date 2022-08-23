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
    'GetIosAppResult',
    'AwaitableGetIosAppResult',
    'get_ios_app',
    'get_ios_app_output',
]

@pulumi.output_type
class GetIosAppResult:
    def __init__(__self__, api_key_id=None, app_id=None, app_store_id=None, bundle_id=None, display_name=None, name=None, project=None, state=None, team_id=None):
        if api_key_id and not isinstance(api_key_id, str):
            raise TypeError("Expected argument 'api_key_id' to be a str")
        pulumi.set(__self__, "api_key_id", api_key_id)
        if app_id and not isinstance(app_id, str):
            raise TypeError("Expected argument 'app_id' to be a str")
        pulumi.set(__self__, "app_id", app_id)
        if app_store_id and not isinstance(app_store_id, str):
            raise TypeError("Expected argument 'app_store_id' to be a str")
        pulumi.set(__self__, "app_store_id", app_store_id)
        if bundle_id and not isinstance(bundle_id, str):
            raise TypeError("Expected argument 'bundle_id' to be a str")
        pulumi.set(__self__, "bundle_id", bundle_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if team_id and not isinstance(team_id, str):
            raise TypeError("Expected argument 'team_id' to be a str")
        pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> str:
        """
        The globally unique, Google-assigned identifier (UID) for the Firebase API key associated with the `IosApp`. Be aware that this value is the UID of the API key, _not_ the [`keyString`](https://cloud.google.com/api-keys/docs/reference/rest/v2/projects.locations.keys#Key.FIELDS.key_string) of the API key. The `keyString` is the value that can be found in the App's [configuration artifact](../../rest/v1beta1/projects.iosApps/getConfig). If `api_key_id` is not set in requests to [`iosApps.Create`](../../rest/v1beta1/projects.iosApps/create), then Firebase automatically associates an `api_key_id` with the `IosApp`. This auto-associated key may be an existing valid key or, if no valid key exists, a new one will be provisioned. In patch requests, `api_key_id` cannot be set to an empty value, and the new UID must have no restrictions or only have restrictions that are valid for the associated `IosApp`. We recommend using the [Google Cloud Console](https://console.cloud.google.com/apis/credentials) to manage API keys.
        """
        return pulumi.get(self, "api_key_id")

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> str:
        """
        Immutable. The globally unique, Firebase-assigned identifier for the `IosApp`. This identifier should be treated as an opaque token, as the data format is not specified.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="appStoreId")
    def app_store_id(self) -> str:
        """
        The automatically generated Apple ID assigned to the iOS app by Apple in the iOS App Store.
        """
        return pulumi.get(self, "app_store_id")

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> str:
        """
        Immutable. The canonical bundle ID of the iOS app as it would appear in the iOS AppStore.
        """
        return pulumi.get(self, "bundle_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The user-assigned display name for the `IosApp`.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the IosApp, in the format: projects/PROJECT_IDENTIFIER /iosApps/APP_ID * PROJECT_IDENTIFIER: the parent Project's [`ProjectNumber`](../projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [`ProjectId`](../projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google's [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for PROJECT_IDENTIFIER in any response body will be the `ProjectId`. * APP_ID: the globally unique, Firebase-assigned identifier for the App (see [`appId`](../projects.iosApps#IosApp.FIELDS.app_id)).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> str:
        """
        Immutable. A user-assigned unique identifier of the parent FirebaseProject for the `IosApp`.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The lifecycle state of the App.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> str:
        """
        The Apple Developer Team ID associated with the App in the App Store.
        """
        return pulumi.get(self, "team_id")


class AwaitableGetIosAppResult(GetIosAppResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIosAppResult(
            api_key_id=self.api_key_id,
            app_id=self.app_id,
            app_store_id=self.app_store_id,
            bundle_id=self.bundle_id,
            display_name=self.display_name,
            name=self.name,
            project=self.project,
            state=self.state,
            team_id=self.team_id)


def get_ios_app(ios_app_id: Optional[str] = None,
                project: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIosAppResult:
    """
    Gets the specified IosApp.
    """
    __args__ = dict()
    __args__['iosAppId'] = ios_app_id
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:firebase/v1beta1:getIosApp', __args__, opts=opts, typ=GetIosAppResult).value

    return AwaitableGetIosAppResult(
        api_key_id=__ret__.api_key_id,
        app_id=__ret__.app_id,
        app_store_id=__ret__.app_store_id,
        bundle_id=__ret__.bundle_id,
        display_name=__ret__.display_name,
        name=__ret__.name,
        project=__ret__.project,
        state=__ret__.state,
        team_id=__ret__.team_id)


@_utilities.lift_output_func(get_ios_app)
def get_ios_app_output(ios_app_id: Optional[pulumi.Input[str]] = None,
                       project: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIosAppResult]:
    """
    Gets the specified IosApp.
    """
    ...
