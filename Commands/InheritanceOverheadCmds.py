from Service.CodeBreakdownService import *
from Helpers.RegexHelper import *
from Commands.CommandModel import *


class InheritanceDeclarationsCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, INHERITANCE_PATTERN)


class ClassInheritanceCommand(FilesCommand):
    def execute(self, files: list) -> list:
        return get_matches_in_file(files, CLASS_PATTERN)
