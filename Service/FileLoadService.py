from tkinter import filedialog as fd
from Commands.FrameworkCmd import FrameworkCommand
from Commands.TermFrequencyCmds import *
from Commands.CodeBreakdownCmds import *
from Commands.InheritanceOverheadCmds import *
from Helpers.GitIgnoreHelper import *
from Commands.MetricsCmd import *
from Commands.CallsToExternalProvidersCmds import *
from InheritanceService import *
from CodeBreakdownService import *
def get_commands():
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
    # commands.append(ClassInheritanceCommand())
    commands.append(ExternalAPICallsCommand())
    return commands

def process_data_from_folder():
    commands = get_commands()
    folder = fd.askdirectory()
    sums = {}
    dict_matches = {}
    class_matches = []
    csfiles = 0
    for root, dirs, files in os.walk(folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name.endswith('.cs'):
                csfiles += 1
                class_matches.extend(get_matches_in_file(file_path,CLASS_PATTERN))
            for command in commands:
                command_name = type(command).__name__
                analysis_results = command.execute(file_path)
                if(isinstance(analysis_results, list)):
                    if len(analysis_results) != 0:
                        if command_name not in dict_matches:
                            dict_matches[command_name] = []
                        dict_matches[command_name].extend(analysis_results)

                if(isinstance(analysis_results, int)):
                    sums[command_name] = sums.get(str(command_name), 0) + analysis_results

    print("inheritance tree max depth: " + repr(get_max_inheritance_depth(class_matches)))
    print(dict_matches)
    print(sums)

process_data_from_folder()

