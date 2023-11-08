from Commands.CommandModel import *
from Service.ModuleCouplingService import *


class MetricsCommand(FileNameCommand):
    def execute(self, file_name: str) -> list:
        return module_coupling(file_name)
