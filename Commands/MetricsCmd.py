from Commands.CommandModel import *
from Service.Analysis.ModuleCouplingService import *


class ClassCouplingListingCommand(FilesRootCommand):
    async def execute(self, folder_path, files: list) -> dict:
        return await class_coupling_listing(folder_path, files)
