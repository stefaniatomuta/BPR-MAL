from Commands.CommandModel import Command
from Service.ModuleCouplingService import *

class MetricsCommand(Command):
    def execute(self, file_name: str) -> list:
        return test(file_name)