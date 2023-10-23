from typing import Any

from Service.CodeBreakdownService import *
from Commands.CommandModel import Command

#this includes also comment lines
class CodeLinesCommand(Command):
    def execute(self, file_name: str) -> int:
       return get_lines_of_code(file_name)

class CommentLinesCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_comment_lines(file_name)

class MethodNumberCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_number_of_methods(file_name)