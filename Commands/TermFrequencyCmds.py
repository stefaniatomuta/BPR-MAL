import re
from Helpers.RegexHelper import IF_PATTERN,FOREACH_PATTERN,FOR_PATTERN,WHILE_PATTERN
from Commands.CommandModel import Command

class ForFrequencyCommand(Command):
    def execute(self, file_name: str) -> int:
        with open(file_name, 'r', encoding='utf8', errors='ignore') as file:
            if file_name.endswith('.cs'):
                code = file.read()
                matches = re.findall(FOR_PATTERN, code, re.MULTILINE)
                return len(matches)

class ForEachFrequencyCommand(Command):
    def execute(self, file_name: str) -> int:
        with open(file_name, 'r', encoding='utf8', errors='ignore') as file:
            if file_name.endswith('.cs'):
                code = file.read()
                matches = re.findall(FOREACH_PATTERN, code, re.MULTILINE)
                return len(matches)


class IfFrequencyCommand(Command):
    def execute(self, file_name: str) -> int:
        with open(file_name, 'r', encoding='utf8', errors='ignore') as file:
            if file_name.endswith('.cs'):
                code = file.read()
                for_matches = re.findall(IF_PATTERN, code, re.MULTILINE)
                return len(for_matches)

class WhileFrequencyCommand(Command):
    def execute(self, file_name: str) -> int:
        with open(file_name, 'r', encoding='utf8', errors='ignore') as file:
            if file_name.endswith('.cs'):
                code = file.read()
                matches = re.findall(WHILE_PATTERN, code, re.MULTILINE)
                return len(matches)