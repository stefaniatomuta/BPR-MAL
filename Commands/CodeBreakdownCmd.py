from Service.CodeBreakdownService import *
from Commands.CommandModel import Command

#this includes also comment lines
class CodeLinesCommand(Command):
    def execute(self, file_name: str) -> int:
       return get_lines_of_code(file_name)

class CommentLinesCommand(Command):
    def execute(self, file_name: str) -> int:
        with open(file_name, 'r', encoding='utf8', errors='ignore') as file:
            return get_comment_lines(file_name)