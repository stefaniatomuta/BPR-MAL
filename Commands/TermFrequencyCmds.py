from Commands.CommandModel import *
from Service.Analysis.CodeBreakdownService import *
from Helpers.RegexHelper import *


class ForFrequencyCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, FOR_PATTERN)


class ForEachFrequencyCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, FOREACH_PATTERN)


class IfFrequencyCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, IF_PATTERN)


class WhileFrequencyCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, WHILE_PATTERN)
