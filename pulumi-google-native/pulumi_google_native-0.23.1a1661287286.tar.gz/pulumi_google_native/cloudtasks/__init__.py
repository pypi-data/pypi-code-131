# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_google_native.cloudtasks.v2 as __v2
    v2 = __v2
    import pulumi_google_native.cloudtasks.v2beta2 as __v2beta2
    v2beta2 = __v2beta2
    import pulumi_google_native.cloudtasks.v2beta3 as __v2beta3
    v2beta3 = __v2beta3
else:
    v2 = _utilities.lazy_import('pulumi_google_native.cloudtasks.v2')
    v2beta2 = _utilities.lazy_import('pulumi_google_native.cloudtasks.v2beta2')
    v2beta3 = _utilities.lazy_import('pulumi_google_native.cloudtasks.v2beta3')

