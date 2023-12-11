from Commands.CommandModel import *
from Service.Analysis.FrameworkService import *


class EndOfLifeFrameworkCommand(FileNameRootCommand):
    async def execute(self, folder_path, file_name: str) -> dict:
        return await get_matches(file_name, folder_path)
