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

class FilesRootCommand(abc.ABC):
    def execute(self, folder_path, file_roots: list) -> Any:
        pass

class FolderCommand(abc.ABC):
    def execute(self, folder_path:str) -> Any:
        pass

class FileNameRootCommand(abc.ABC):
    def execute(self, folder_path:str, file_name:str) -> Any:
        pass