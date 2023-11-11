from Commands.CommandModel import *
from Service.ModuleCouplingService import *


class ClassCouplingCommand(FileNameCommand):
    def execute(self, file_name: str) -> list:
        return class_coupling(file_name)
