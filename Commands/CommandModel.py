import abc
from typing import Any


class FileNameCommand(abc.ABC):
    async def execute(self, file_name: str) -> Any:
        pass

class FilesCommand(abc.ABC):
    async def execute(self, file_roots: list) -> Any:
        pass

class FilesRootCommand(abc.ABC):
    async def execute(self, folder_path, file_roots: list) -> Any:
        pass

class FolderCommand(abc.ABC):
    async def execute(self, folder_path:str) -> Any:
        pass

class FileNameRootCommand(abc.ABC):
    async def execute(self, folder_path:str, file_name:str) -> Any:
        pass