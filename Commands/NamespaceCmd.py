from Commands.CommandModel import *
from Service.Analysis.NamespaceService import *


class MismatchedNamespaceCommand(FolderCommand):
    def execute(self,folder_path: str) -> int:
        return get_namespace_analysis(folder_path)
