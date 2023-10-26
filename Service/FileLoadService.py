from tkinter import filedialog as fd
import os
from CSVFileService import *
from Commands.FrameworkCmd import FrameworkCommand
from Commands.TermFrequencyCmds import *
from Commands.CodeBreakdownCmds import *
from Commands.InheritanceOverheadCmds import *
from Service import FrameworksService
from Service.InheritanceService import get_max_inheritance_depth

def get_commands():
from Service import EOLService
from Helpers.GitIgnoreHelper import *
from Commands.MetricsCmd import *
from collections import defaultdict
import inspect
def process_data_from_folder():
    commands = []
    commands.append(MetricsCommand())
    commands.append(FrameworkCommand())
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
    commands.append(ClassInheritanceCommand())
    return commands

def process_data_from_folder():
    commands = get_commands()
    folder = fd.askdirectory()
    sums = defaultdict(int)
    sums = {}
    class_matches = []
    csfiles = 0
    # for entry in os.scandir(folder):
    #     if entry.name == '.gitignore':
    #         content = read_gitignore(entry.path)
    #         print(len(content))
    #         for lin in content:
    #             print(lin)

    for root, dirs, files in os.walk(folder):
        for file_name in files:
            if file_name.endswith('.cs'):
                csfiles += 1
            for command in commands:
                file_path = os.path.join(root,file_name)
                analysis_results = command.execute(file_path)
                for file, match in analysis_results.items():
                    info = FrameworksService.EOL_API(match)
                    print(info.isEndOfLife)
                if(isinstance(analysis_results, list)):
                    class_matches.extend(analysis_results)
                if(isinstance(analysis_results, int)):
                    command_name = type(command).__name__
                    sums[command_name] = sums.get(str(command_name),0)+ analysis_results
    print("inheritance tree max depth: " + repr(get_max_inheritance_depth(class_matches)))
    print(sums)

process_data_from_folder()

