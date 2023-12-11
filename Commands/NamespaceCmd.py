from Commands.CommandModel import *
from Service.Analysis.NamespaceService import *


class MismatchedNamespaceCommand(FolderCommand):
    async def execute(self,folder_path: str) -> int:
        return await get_namespace_analysis(folder_path)
