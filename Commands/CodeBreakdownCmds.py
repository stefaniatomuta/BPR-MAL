from Service.Analysis.CodeBreakdownService import *
from Helpers.RegexHelper import *
from Commands.CommandModel import *
from Service.Analysis.CodeSimilarityService import *


# this includes also comment lines
class CodeLinesCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, CODELINES_PATTERN)


class CommentLinesCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, COMMENTS_PATTERN)


class MethodNumberCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, METHOD_PATTERN)


class ClassNumberCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, CLASS_PATTERN)


class InterfaceNumberCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, INTERFACE_PATTERN)


class UsingsNumberCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, USINGS_PATTERN)


class CodeSimilarityCommand(FolderCommand):
    def execute(self, folder_path: str) -> list:
        return get_code_similarity(folder_path)

class CodeLinesPerFileCommand(FileNameRootCommand):
    def execute(self, folder_path, file_name: str) -> dict:
        return get_match_with_file(folder_path, file_name, CODELINES_PATTERN)

class CommentLinesPerFileCommand(FileNameRootCommand):
    async def execute(self,folder_path, file_name: str) -> dict:
        return await get_match_with_file(folder_path, file_name, COMMENTS_PATTERN)

class CSFilesCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return 1 if file_name.endswith(".cs") else 0
