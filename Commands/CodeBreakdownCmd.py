import re
from Helpers.RegexHelper import CODELINES_PATTERN,COMMENTS_PATTERN
from Commands.CommandModel import Command

#this includes also comment lines
class CodeLinesCommand(Command):
    def execute(self, file_name: str) -> int:
        with open(file_name, 'r', encoding='utf8', errors='ignore') as file:
            if file_name.endswith('.cs'):
                code = file.read()
                matches = re.findall(CODELINES_PATTERN, code, re.MULTILINE)
                return len(matches)

class CommentLinesCommand(Command):
    def execute(self, file_name: str) -> int:
        with open(file_name, 'r', encoding='utf8', errors='ignore') as file:
            if file_name.endswith('.cs'):
                code = file.read()
                matches = re.findall(COMMENTS_PATTERN, code, re.MULTILINE)
                return len(matches)