from Commands.CommandModel import Command
from Service.CodeBreakdownService import *
from Helpers.RegexHelper import FOR_PATTERN,FOREACH_PATTERN,IF_PATTERN,WHILE_PATTERN

class ForFrequencyCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, FOR_PATTERN)

class ForEachFrequencyCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, FOREACH_PATTERN)


class IfFrequencyCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, IF_PATTERN)

class WhileFrequencyCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_number_of_matches_in_file(file_name, WHILE_PATTERN)