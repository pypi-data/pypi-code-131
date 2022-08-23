import json
from typing import Iterator, List, Optional

from approvaltests.core.reporter import Reporter
from approvaltests.reporters.python_native_reporter import PythonNativeReporter
from approvaltests.reporters.generic_diff_reporter import (
    GenericDiffReporter,
)
from approvaltests.reporters.generic_diff_reporter_config import (
    GenericDiffReporterConfig,
    create_config,
)
from approvaltests.reporters.report_with_beyond_compare import (
    ReportWithBeyondCompare,
    ReportWithWinMerge,
)
from approvaltests.utils import get_adjacent_file


class NoConfigReporter(Reporter):
    def report(self, received_path: str, approved_path: str) -> bool:
        raise RuntimeError("This machine has no reporter configuration")


class GenericDiffReporterFactory:
    reporters: List[GenericDiffReporterConfig] = []

    def __init__(self) -> None:
        self.load(get_adjacent_file("reporters.json"))

    def add_default_reporter_config(self, config):
        self.reporters.insert(0, create_config(config))

    def list(self) -> List[str]:
        return [r.name for r in self.reporters]

    def get(self, reporter_name: str) -> Reporter:
        reporter = GenericDiffReporterFactory.get_reporter_programmmatically(
            reporter_name
        )
        return reporter or self.get_from_json_config(reporter_name)

    @staticmethod
    def get_reporter_programmmatically(reporter_name: str) -> Optional[Reporter]:
        reporters = {
            "BeyondCompare": ReportWithBeyondCompare,
            "WinMerge": ReportWithWinMerge,
            "PythonNative": PythonNativeReporter,
            "PythonNativeReporter": PythonNativeReporter,
        }
        clazz = reporters.get(reporter_name)
        return clazz and clazz()

    def get_from_json_config(self, reporter_name: str) -> Reporter:
        config = next((r for r in self.reporters if r.name == reporter_name), None)
        if not config:
            return NoConfigReporter()
        return self._create_reporter(config)

    @staticmethod
    def _create_reporter(config: GenericDiffReporterConfig) -> GenericDiffReporter:
        return GenericDiffReporter(config)

    def save(self, file_name: str) -> str:
        with open(file_name, "w", encoding="utf8") as file:
            json.dump(
                [reporter.serialize() for reporter in self.reporters],
                file,
                sort_keys=True,
                indent=2,
                separators=(",", ": "),
            )
        return file_name

    def load(self, file_name: str) -> List[GenericDiffReporterConfig]:
        with open(file_name, "r", encoding="utf8") as file:
            configs = json.load(file)
        self.reporters = [create_config(config) for config in configs]
        return self.reporters

    def get_first_working(self) -> Optional[GenericDiffReporter]:
        working = (i for i in self.get_all_reporters() if i.is_working())
        return next(working, None)

    def get_all_reporters(self) -> Iterator[GenericDiffReporter]:
        instances = (self._create_reporter(r) for r in self.reporters)
        return instances

    def remove(self, reporter_name: str) -> None:
        self.reporters = [r for r in self.reporters if r.name != reporter_name]
