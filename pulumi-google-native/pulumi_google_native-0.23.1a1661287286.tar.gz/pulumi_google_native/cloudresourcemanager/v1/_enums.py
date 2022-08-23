# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AuditLogConfigLogType',
    'ProjectLifecycleState',
]


class AuditLogConfigLogType(str, Enum):
    """
    The log type that this config enables.
    """
    LOG_TYPE_UNSPECIFIED = "LOG_TYPE_UNSPECIFIED"
    """
    Default case. Should never be this.
    """
    ADMIN_READ = "ADMIN_READ"
    """
    Admin reads. Example: CloudIAM getIamPolicy
    """
    DATA_WRITE = "DATA_WRITE"
    """
    Data writes. Example: CloudSQL Users create
    """
    DATA_READ = "DATA_READ"
    """
    Data reads. Example: CloudSQL Users list
    """


class ProjectLifecycleState(str, Enum):
    """
    The Project lifecycle state. Read-only.
    """
    LIFECYCLE_STATE_UNSPECIFIED = "LIFECYCLE_STATE_UNSPECIFIED"
    """
    Unspecified state. This is only used/useful for distinguishing unset values.
    """
    ACTIVE = "ACTIVE"
    """
    The normal and active state.
    """
    DELETE_REQUESTED = "DELETE_REQUESTED"
    """
    The project has been marked for deletion by the user (by invoking DeleteProject) or by the system (Google Cloud Platform). This can generally be reversed by invoking UndeleteProject.
    """
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    """
    This lifecycle state is no longer used and not returned by the API.
    """
