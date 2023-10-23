from tkinter import filedialog as fd
import os
from CSVFileService import *
from Commands.FrameworkCmd import FrameworkCommand
from Commands.TermFrequencyCmds import *
from Commands.CodeBreakdownCmd import *
from Service import FrameworksService
def process_data_from_folder():
    commands = []
    # commands.append(FrameworkCommand())
    commands.append(ForFrequencyCommand())
    commands.append(IfFrequencyCommand())
    commands.append(ForEachFrequencyCommand())
    commands.append(WhileFrequencyCommand())
    commands.append(CodeLinesCommand())
    commands.append(CommentLinesCommand())
    commands.append(MethodNumberCommand())
    folder = fd.askdirectory()
    sums = {}

    for root,dirs,files in os.walk(folder):
        for file_name in files:
            for command in commands:
                file_path = os.path.join(root,file_name)
                analysis_results = command.execute(file_path)
                analysis_results = {}
                analysis_results.setdefault(type(command).__name__, 0)
                analysis_results[type(command).__name__] += command.execute(file_path)
                # for file, match in analysis_results.items():
                #     info = FrameworksService.EOL_API(match)
                #     print(info.isEndOfLife)

                for command_name, result in analysis_results.items():
                    if(command_name != 'FrameworkCommand'):
                        sums[str(command_name)] = sums.get(str(command_name),0)+ result
    print(sums)


    # write_row_to_csv(row)

process_data_from_folder()

