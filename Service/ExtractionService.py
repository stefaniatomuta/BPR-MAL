import uuid
from Commands.CodeBreakdownCmds import *
from Commands.FrameworkCmd import *
from Commands.InheritanceOverheadCmds import *
from Commands.MetricsCmd import *
from Commands.TermFrequencyCmds import *
from Helpers.GitIgnoreHelper import *
from Commands.CallsToExternalProvidersCmds import *
import os

commands = [EndOfLifeFrameworkCommand(), ForFrequencyCommand(), IfFrequencyCommand(),
            ForEachFrequencyCommand(), WhileFrequencyCommand(), CodeLinesCommand(), CommentLinesCommand(),
            MethodNumberCommand(), ClassNumberCommand(), InterfaceNumberCommand(), InheritanceDeclarationsCommand(),
            InheritanceDepthCommand(), ExternalAPICallsCommand(), HttpClientCallsCommand(), CodeSimilarityCommand(),
            UsingsNumberCommand(), ClassCouplingListingCommand(), CodeLinesPerFileCommand(), CommentLinesPerFileCommand()]

def get_rules(commands) -> list:
    return [type(command).__name__.rstrip("Command") for command in commands]

def process_data_from_folder(folder_path) -> ({},[]):
    rules = get_rules(commands)
    sums = {}
    gitignore_content = read_gitignore()
    extracted_files = []
    files_roots = []
    sums['Project_ID'] = uuid.uuid4()
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if not should_ignore_dir(d, gitignore_content)]
        for file_name in files:
            files_roots.append(os.path.join(root, file_name))
        extracted_files.extend([file for file in files_roots if not is_ignored(file, gitignore_content) and file not in extracted_files])

    for command in commands:
        command_name = type(command).__name__.rstrip("Command")
        if isinstance(command, FolderCommand):
            analysis_results = command.execute(folder_path)
            sums[command_name] = analysis_results
        if isinstance(command, FilesCommand):
            analysis_results = command.execute(files_roots)
            sums[command_name] = analysis_results
        if isinstance(command, FileNameCommand):
            for file_name in files_roots:
                analysis_results = command.execute(file_name)
                if isinstance(analysis_results, list) or isinstance(analysis_results, dict):
                    if len(analysis_results) != 0:
                        if command_name not in sums:
                            sums[command_name] = []
                        sums[command_name].append(analysis_results)

                if (isinstance(analysis_results, int)):
                    sums[command_name] = sums.get(str(command_name), 0) + analysis_results

    return sums,rules
