from Service.CodeBreakdownService import *
from Helpers.RegexHelper import INHERITANCE_PATTERN
from Commands.CommandModel import Command
class InheritanceDeclarationsCommand(Command):
    def execute(self, file_name: str) -> int:
       return get_matches_in_file(file_name,INHERITANCE_PATTERN)