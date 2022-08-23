# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from ._version import __version__
from .app import LabServerApp
from .handlers import LabConfig, LabHandler, add_handlers
from .licenses_app import LicensesApp
from .spec import get_openapi_spec, get_openapi_spec_dict  # noqa
from .translation_utils import translator
from .workspaces_app import WorkspaceExportApp, WorkspaceImportApp, WorkspaceListApp
from .workspaces_handler import WORKSPACE_EXTENSION, slugify

__all__ = [
    "__version__",
    "add_handlers",
    "LabConfig",
    "LabHandler",
    "LabServerApp",
    "LicensesApp",
    "SETTINGS_EXTENSION",
    "slugify",
    "translator",
    "WORKSPACE_EXTENSION",
    "WorkspaceExportApp",
    "WorkspaceImportApp",
    "WorkspaceListApp",
]


def _jupyter_server_extension_points():
    return [{"module": "jupyterlab_server", "app": LabServerApp}]
