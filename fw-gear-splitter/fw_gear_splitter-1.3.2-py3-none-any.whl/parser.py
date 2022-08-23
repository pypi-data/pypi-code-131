"""Parser module to parse gear config.json."""
import typing as t
from pathlib import Path

from flywheel_gear_toolkit import GearToolkitContext


def parse_config(
    gear_context: GearToolkitContext,
) -> t.Tuple[Path, bool, t.List[str], bool]:
    """Parses gear_context config.json file.

    Returns:
        Tuple[Path, bool, t.List[str]]: tuple containing,
            - Path of dicom input
            - extract_localizer
            - group_by (unique tags to split archive on)
            - zip_single (Zip single dicoms)
    """

    # INPUTS
    dcm_path = Path(gear_context.get_input_path("dicom"))

    # CONFIG
    extract_localizer = gear_context.config.get("extract_localizer")
    zip_single_raw = gear_context.config.get("zip-single-dicom", "match")
    # Zip single is set to True on "match", False otherwise ("no")
    zip_single = zip_single_raw == "match"
    if gear_context.config.get("group_by", ""):
        group_by = gear_context.config.get("group_by").split(",")
    else:
        group_by = None

    return (dcm_path, extract_localizer, group_by, zip_single)
