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
    'GetEntitlementResult',
    'AwaitableGetEntitlementResult',
    'get_entitlement',
    'get_entitlement_output',
]

@pulumi.output_type
class GetEntitlementResult:
    def __init__(__self__, association_info=None, commitment_settings=None, create_time=None, name=None, offer=None, parameters=None, provisioned_service=None, provisioning_state=None, purchase_order_id=None, suspension_reasons=None, trial_settings=None, update_time=None):
        if association_info and not isinstance(association_info, dict):
            raise TypeError("Expected argument 'association_info' to be a dict")
        pulumi.set(__self__, "association_info", association_info)
        if commitment_settings and not isinstance(commitment_settings, dict):
            raise TypeError("Expected argument 'commitment_settings' to be a dict")
        pulumi.set(__self__, "commitment_settings", commitment_settings)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if offer and not isinstance(offer, str):
            raise TypeError("Expected argument 'offer' to be a str")
        pulumi.set(__self__, "offer", offer)
        if parameters and not isinstance(parameters, list):
            raise TypeError("Expected argument 'parameters' to be a list")
        pulumi.set(__self__, "parameters", parameters)
        if provisioned_service and not isinstance(provisioned_service, dict):
            raise TypeError("Expected argument 'provisioned_service' to be a dict")
        pulumi.set(__self__, "provisioned_service", provisioned_service)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if purchase_order_id and not isinstance(purchase_order_id, str):
            raise TypeError("Expected argument 'purchase_order_id' to be a str")
        pulumi.set(__self__, "purchase_order_id", purchase_order_id)
        if suspension_reasons and not isinstance(suspension_reasons, list):
            raise TypeError("Expected argument 'suspension_reasons' to be a list")
        pulumi.set(__self__, "suspension_reasons", suspension_reasons)
        if trial_settings and not isinstance(trial_settings, dict):
            raise TypeError("Expected argument 'trial_settings' to be a dict")
        pulumi.set(__self__, "trial_settings", trial_settings)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="associationInfo")
    def association_info(self) -> 'outputs.GoogleCloudChannelV1AssociationInfoResponse':
        """
        Association information to other entitlements.
        """
        return pulumi.get(self, "association_info")

    @property
    @pulumi.getter(name="commitmentSettings")
    def commitment_settings(self) -> 'outputs.GoogleCloudChannelV1CommitmentSettingsResponse':
        """
        Commitment settings for a commitment-based Offer. Required for commitment based offers.
        """
        return pulumi.get(self, "commitment_settings")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time at which the entitlement is created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name of an entitlement in the form: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def offer(self) -> str:
        """
        The offer resource name for which the entitlement is to be created. Takes the form: accounts/{account_id}/offers/{offer_id}.
        """
        return pulumi.get(self, "offer")

    @property
    @pulumi.getter
    def parameters(self) -> Sequence['outputs.GoogleCloudChannelV1ParameterResponse']:
        """
        Extended entitlement parameters. When creating an entitlement, valid parameter names and values are defined in the Offer.parameter_definitions. The response may include the following output-only Parameters: - assigned_units: The number of licenses assigned to users. - max_units: The maximum assignable units for a flexible offer. - num_units: The total commitment for commitment-based offers.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="provisionedService")
    def provisioned_service(self) -> 'outputs.GoogleCloudChannelV1ProvisionedServiceResponse':
        """
        Service provisioning details for the entitlement.
        """
        return pulumi.get(self, "provisioned_service")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Current provisioning state of the entitlement.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="purchaseOrderId")
    def purchase_order_id(self) -> str:
        """
        Optional. This purchase order (PO) information is for resellers to use for their company tracking usage. If a purchaseOrderId value is given, it appears in the API responses and shows up in the invoice. The property accepts up to 80 plain text characters. This is only supported for Google Workspace entitlements.
        """
        return pulumi.get(self, "purchase_order_id")

    @property
    @pulumi.getter(name="suspensionReasons")
    def suspension_reasons(self) -> Sequence[str]:
        """
        Enumerable of all current suspension reasons for an entitlement.
        """
        return pulumi.get(self, "suspension_reasons")

    @property
    @pulumi.getter(name="trialSettings")
    def trial_settings(self) -> 'outputs.GoogleCloudChannelV1TrialSettingsResponse':
        """
        Settings for trial offers.
        """
        return pulumi.get(self, "trial_settings")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time at which the entitlement is updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetEntitlementResult(GetEntitlementResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEntitlementResult(
            association_info=self.association_info,
            commitment_settings=self.commitment_settings,
            create_time=self.create_time,
            name=self.name,
            offer=self.offer,
            parameters=self.parameters,
            provisioned_service=self.provisioned_service,
            provisioning_state=self.provisioning_state,
            purchase_order_id=self.purchase_order_id,
            suspension_reasons=self.suspension_reasons,
            trial_settings=self.trial_settings,
            update_time=self.update_time)


def get_entitlement(account_id: Optional[str] = None,
                    customer_id: Optional[str] = None,
                    entitlement_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEntitlementResult:
    """
    Returns the requested Entitlement resource. Possible error codes: * PERMISSION_DENIED: The customer doesn't belong to the reseller. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: The customer entitlement was not found. Return value: The requested Entitlement resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['customerId'] = customer_id
    __args__['entitlementId'] = entitlement_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:cloudchannel/v1:getEntitlement', __args__, opts=opts, typ=GetEntitlementResult).value

    return AwaitableGetEntitlementResult(
        association_info=__ret__.association_info,
        commitment_settings=__ret__.commitment_settings,
        create_time=__ret__.create_time,
        name=__ret__.name,
        offer=__ret__.offer,
        parameters=__ret__.parameters,
        provisioned_service=__ret__.provisioned_service,
        provisioning_state=__ret__.provisioning_state,
        purchase_order_id=__ret__.purchase_order_id,
        suspension_reasons=__ret__.suspension_reasons,
        trial_settings=__ret__.trial_settings,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_entitlement)
def get_entitlement_output(account_id: Optional[pulumi.Input[str]] = None,
                           customer_id: Optional[pulumi.Input[str]] = None,
                           entitlement_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEntitlementResult]:
    """
    Returns the requested Entitlement resource. Possible error codes: * PERMISSION_DENIED: The customer doesn't belong to the reseller. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: The customer entitlement was not found. Return value: The requested Entitlement resource.
    """
    ...
