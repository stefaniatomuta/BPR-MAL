from tkinter import filedialog as fd
import os
from CSVFileService import *
from Commands.FrameworkCmd import FrameworkCommand
from Commands.TermFrequencyCmds import *
from Commands.CodeBreakdownCmd import *
from Service import FrameworksService

def process_data_from_folder():
    commands = []
    commands.append(FrameworkCommand())
    commands.append(ForFrequencyCommand())
    commands.append(IfFrequencyCommand())
    commands.append(ForEachFrequencyCommand())
    commands.append(WhileFrequencyCommand())
    commands.append(CodeLinesCommand())
    folder = fd.askdirectory()


    for root,dirs,files in os.walk(folder):
        for file_name in files:
            for command in commands:
                file_path = os.path.join(root,file_name)
                analysis_results = command.execute(file_path)
                # for file, match in analysis_results.items():
                #     info = FrameworksService.EOL_API(match)
                #     print(info.isEndOfLife)
                print(analysis_results)


    # write_row_to_csv(row)

process_data_from_folder()

