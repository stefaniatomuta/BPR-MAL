import abc
from typing import Any


# abstract class as base class for the rest of the commanders
class Command(abc.ABC):
    def execute(self, file_name: str) -> Any:
        pass


class FilesCommand(abc.ABC):
    def execute(self, files: str) -> Any:
        pass
