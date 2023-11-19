from Commands.CommandModel import *
from Service.ModuleCouplingService import *


class ClassCouplingCommand(FilesCommand):
    def execute(self, files: list) -> dict:
        return class_coupling_mapping(files)


class ClassCouplingListingCommand(FilesCommand):
    def execute(self, files: list) -> dict:
        return class_coupling_listing(files)
