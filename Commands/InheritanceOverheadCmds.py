from Service.CodeBreakdownService import *
from Helpers.RegexHelper import INHERITANCE_PATTERN,CLASS_PATTERN
from Commands.CommandModel import Command
class InheritanceDeclarationsCommand(Command):
    def execute(self, file_name: str) -> int:
       return get_number_of_matches_in_file(file_name, INHERITANCE_PATTERN)

class ClassInheritanceCommand(Command):
    def execute(self, file_name: str) -> list:
        return get_matches_in_file(file_name,CLASS_PATTERN)