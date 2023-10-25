from Service.CodeBreakdownService import *
from Helpers.RegexHelper import INTERFACE_PATTERN,CLASS_PATTERN,COMMENTS_PATTERN,CODELINES_PATTERN,METHOD_PATTERN
from Commands.CommandModel import Command

#this includes also comment lines
class CodeLinesCommand(Command):
    def execute(self, file_name: str) -> int:
       return get_matches_in_file(file_name,CODELINES_PATTERN)

class CommentLinesCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_matches_in_file(file_name,COMMENTS_PATTERN)

class MethodNumberCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_matches_in_file(file_name,METHOD_PATTERN)

class ClassNumberCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_matches_in_file(file_name,CLASS_PATTERN)

class InterfaceNumberCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_matches_in_file(file_name,INTERFACE_PATTERN)