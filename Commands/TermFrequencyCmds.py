from Commands.CommandModel import Command
from Service.TermFrequencyService import *

class ForFrequencyCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_number_of_fors_in_file(file_name)

class ForEachFrequencyCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_number_of_foreaches_in_file(file_name)


class IfFrequencyCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_number_of_ifs_in_file(file_name)

class WhileFrequencyCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_number_of_whiles_in_file(file_name)