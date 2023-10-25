from tkinter import filedialog as fd
import os
from CSVFileService import *
from Commands.FrameworkCmd import FrameworkCommand
from Commands.TermFrequencyCmds import *
from Commands.CodeBreakdownCmds import *
from Commands.InheritanceOverheadCmds import *
from Service import FrameworksService

def get_commands():
    commands = []
    # commands.append(FrameworkCommand())
    commands.append(ForFrequencyCommand())
    commands.append(IfFrequencyCommand())
    commands.append(ForEachFrequencyCommand())
    commands.append(WhileFrequencyCommand())
    commands.append(CodeLinesCommand())
    commands.append(CommentLinesCommand())
    commands.append(MethodNumberCommand())
    commands.append(ClassNumberCommand())
    commands.append(InterfaceNumberCommand())
    commands.append(InheritanceDeclarationsCommand())
    return commands
def process_data_from_folder():
    commands = get_commands()
    folder = fd.askdirectory()
    sums = {}
    csfiles = 0
    for root,dirs,files in os.walk(folder):
        for file_name in files:
            if file_name.endswith('.cs'):
                csfiles+=1
            for command in commands:
                file_path = os.path.join(root,file_name)
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

process_data_from_folder()

