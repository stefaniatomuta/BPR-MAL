from Service.Analysis.CodeBreakdownService import *
from Service.Analysis.InheritanceService import *
from Helpers.RegexHelper import *
from Commands.CommandModel import *


class InheritanceDeclarationsCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, INHERITANCE_PATTERN)


class InheritanceDepthCommand(FilesCommand):
    def execute(self, files: list) -> int:
        try:
            matches = get_matches_in_files(files, CLASS_PATTERN)
            return get_max_inheritance_depth(matches)
        except RecursionError:
            return 0
