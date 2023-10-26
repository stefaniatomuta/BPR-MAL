from tkinter import filedialog as fd
import os
from CSVFileService import *
from Commands.FrameworkCmd import FrameworkCommand
from Commands.TermFrequencyCmds import *
from Commands.CodeBreakdownCmds import *
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
    folder = fd.askdirectory()
    sums = defaultdict(int)
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
                file_path = os.path.join(root, file_name)
                result = command.execute(file_path)
                if isinstance(result, list):
                    for result in result:
                        print(result)

    print(sums)

process_data_from_folder()

