from Service.CodeBreakdownService import *
from Helpers.RegexHelper import *
from Commands.CommandModel import *
from Service.CodeDuplicationService import *


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


class CodeDuplicationCommand(FolderCommand):
    def execute(self, folder_path: str) -> list:
        return get_code_similarity_values(folder_path)

class CodeLinesPerFileCommand(FileNameCommand):
    def execute(self, file_name: str) -> dict:
        return get_match_with_file(file_name, CODELINES_PATTERN)