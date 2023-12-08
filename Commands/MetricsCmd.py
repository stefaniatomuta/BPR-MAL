from Commands.CommandModel import *
from Service.ModuleCouplingService import *


class ClassCouplingListingCommand(FilesRootCommand):
    def execute(self, folder_path, files: list) -> dict:
        return class_coupling_listing(folder_path, files)
