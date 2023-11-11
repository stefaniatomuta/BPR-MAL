import abc
from typing import Any


# abstract class as base class for the commanders that uses file_name
class FileNameCommand(abc.ABC):
    def execute(self, file_name: str) -> Any:
        pass


# abstract class as base class for the commanders that uses files
class FilesCommand(abc.ABC):
    def execute(self, file_roots: list) -> Any:
        pass
