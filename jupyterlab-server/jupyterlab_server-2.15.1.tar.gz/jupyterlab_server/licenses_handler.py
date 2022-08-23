"""Manager and Tornado handlers for license reporting."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import csv
import io
import json
import mimetypes
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from tornado import gen, web
from traitlets import List, Unicode
from traitlets.config import LoggingConfigurable

from .config import get_federated_extensions
from .server import APIHandler

# this is duplicated in @juptyerlab/builder
DEFAULT_THIRD_PARTY_LICENSE_FILE = "third-party-licenses.json"
UNKNOWN_PACKAGE_NAME = "UNKNOWN"

if mimetypes.guess_extension("text/markdown") is None:  # pragma: no cover
    # for python <3.8 https://bugs.python.org/issue39324
    mimetypes.add_type("text/markdown", ".md")


class LicensesManager(LoggingConfigurable):
    """A manager for listing the licenses for all frontend end code distributed
    by an application and any federated extensions
    """

    executor = ThreadPoolExecutor(max_workers=1)

    third_party_licenses_files = List(
        Unicode(),
        default_value=[
            DEFAULT_THIRD_PARTY_LICENSE_FILE,
            f"static/{DEFAULT_THIRD_PARTY_LICENSE_FILE}",
        ],
        help="the license report data in built app and federated extensions",
    )

    @property
    def federated_extensions(self):
        """Lazily load the currrently-available federated extensions.

        This is expensive, but probably the only way to be sure to get
        up-to-date license information for extensions installed interactively.
        """
        labextensions_path = sum(
            [
                self.parent.labextensions_path,
                self.parent.extra_labextensions_path,
            ],
            [],
        )
        return get_federated_extensions(labextensions_path)

    @gen.coroutine
    def report_async(self, report_format="markdown", bundles_pattern=".*", full_text=False):
        """Asynchronous wrapper around the potentially slow job of locating
        and encoding all of the licenses
        """
        report = yield self.executor.submit(
            self.report,
            report_format=report_format,
            bundles_pattern=bundles_pattern,
            full_text=full_text,
        )
        return report

    def report(self, report_format, bundles_pattern, full_text):
        """create a human- or machine-readable report"""
        bundles = self.bundles(bundles_pattern=bundles_pattern)
        if report_format == "json":
            return self.report_json(bundles), "application/json"
        elif report_format == "csv":
            return self.report_csv(bundles), "text/csv"
        elif report_format == "markdown":
            return (
                self.report_markdown(bundles, full_text=full_text),
                "text/markdown",
            )

    def report_json(self, bundles):
        """create a JSON report
        TODO: SPDX
        """
        return json.dumps({"bundles": bundles}, indent=2, sort_keys=True)

    def report_csv(self, bundles):
        """create a CSV report"""
        outfile = io.StringIO()
        fieldnames = ["name", "versionInfo", "licenseId", "extractedText"]
        writer = csv.DictWriter(outfile, fieldnames=["bundle"] + fieldnames)
        writer.writeheader()
        for bundle_name, bundle in bundles.items():
            for package in bundle["packages"]:
                writer.writerow(
                    {
                        "bundle": bundle_name,
                        **{field: package.get(field, "") for field in fieldnames},
                    }
                )
        return outfile.getvalue()

    def report_markdown(self, bundles, full_text=True):
        """create a markdown report"""
        lines = []
        library_names = [
            len(package.get("name", UNKNOWN_PACKAGE_NAME))
            for bundle_name, bundle in bundles.items()
            for package in bundle.get("packages", [])
        ]
        longest_name = max(library_names) if library_names else 1

        for bundle_name, bundle in bundles.items():
            # TODO: parametrize template
            lines += [f"# {bundle_name}", ""]

            packages = bundle.get("packages", [])
            if not packages:
                lines += ["> No licenses found", ""]
                continue

            for package in packages:
                name = package.get("name", UNKNOWN_PACKAGE_NAME).strip()
                version_info = package.get("versionInfo", UNKNOWN_PACKAGE_NAME).strip()
                license_id = package.get("licenseId", UNKNOWN_PACKAGE_NAME).strip()
                extracted_text = package.get("extractedText", "")

                lines += [
                    "## "
                    + (
                        "\t".join(
                            [
                                f"""**{name}**""".ljust(longest_name),
                                f"""`{version_info}`""".ljust(20),
                                license_id,
                            ]
                        )
                    )
                ]

                if full_text:
                    if not extracted_text:
                        lines += ["", "> No license text available", ""]
                    else:
                        lines += ["", "", "<pre/>", extracted_text, "</pre>", ""]
        return "\n".join(lines)

    def license_bundle(self, path, bundle):
        """Return the content of a packages's license bundles"""
        bundle_json = {"packages": []}
        checked_paths = []

        for license_file in self.third_party_licenses_files:
            licenses_path = path / license_file
            self.log.debug("Loading licenses from %s", licenses_path)
            if not licenses_path.exists():
                checked_paths += [licenses_path]
                continue

            try:
                file_json = json.loads(licenses_path.read_text(encoding="utf-8"))
            except Exception as err:
                self.log.warning(
                    "Failed to open third-party licenses for %s: %s\n%s",
                    bundle,
                    licenses_path,
                    err,
                )
                continue

            try:
                bundle_json["packages"].extend(file_json["packages"])
            except Exception as err:
                self.log.warning(
                    "Failed to find packages for %s: %s\n%s",
                    bundle,
                    licenses_path,
                    err,
                )
                continue

        if not bundle_json["packages"]:
            self.log.warning("Third-party licenses not found for %s: %s", bundle, checked_paths)

        return bundle_json

    def app_static_info(self):
        """get the static directory for this app

        This will usually be in `static_dir`, but may also appear in the
        parent of `static_dir`.
        """
        path = Path(self.parent.static_dir)
        package_json = path / "package.json"
        if not package_json.exists():
            parent_package_json = path.parent / "package.json"
            if parent_package_json.exists():
                package_json = parent_package_json
            else:
                return None, None
        name = json.loads(package_json.read_text(encoding="utf-8"))["name"]
        return path, name

    def bundles(self, bundles_pattern=".*"):
        """Read all of the licenses
        TODO: schema
        """
        bundles = {
            name: self.license_bundle(Path(ext["ext_path"]), name)
            for name, ext in self.federated_extensions.items()
            if re.match(bundles_pattern, name)
        }

        app_path, app_name = self.app_static_info()
        if app_path is not None and re.match(bundles_pattern, app_name):
            bundles[app_name] = self.license_bundle(app_path, app_name)

        if not bundles:
            self.log.warning("No license bundles found at all")

        return bundles


class LicensesHandler(APIHandler):
    """A handler for serving licenses used by the application"""

    def initialize(self, manager: LicensesManager):
        super().initialize()
        self.manager = manager

    @web.authenticated
    async def get(self, _args):
        """Return all the frontend licenses"""
        full_text = bool(json.loads(self.get_argument("full_text", "true")))
        report_format = self.get_argument("format", "json")
        bundles_pattern = self.get_argument("bundles", ".*")
        download = bool(json.loads(self.get_argument("download", "0")))

        report, mime = await self.manager.report_async(
            report_format=report_format,
            bundles_pattern=bundles_pattern,
            full_text=full_text,
        )

        if download:
            filename = "{}-licenses{}".format(
                self.manager.parent.app_name.lower(), mimetypes.guess_extension(mime)
            )
            self.set_attachment_header(filename)
        self.write(report)
        await self.finish(_mime_type=mime)

    def finish(self, _mime_type, *args, **kwargs):
        """Overload the regular finish, which (sensibly) always sets JSON"""
        self.update_api_activity()
        self.set_header("Content-Type", _mime_type)
        return super(APIHandler, self).finish(*args, **kwargs)
