from Commands.CommandModel import *

from Service.FrameworkService import *


# finds matches in the csproj of the target frameworks
class EndOfLifeFrameworkCommand(FileNameRootCommand):
    def execute(self, folder_path, file_name: str) -> dict:
        return get_matches(file_name, folder_path)
