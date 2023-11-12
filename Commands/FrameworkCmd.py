from Commands.CommandModel import *

from Service.FrameworkService import *


# finds matches in the csproj of the target frameworks
class EndOfLifeFrameworkCommand(FileNameCommand):
    def execute(self, file_name: str) -> int:
        return get_number_eod_frameworks(file_name)
