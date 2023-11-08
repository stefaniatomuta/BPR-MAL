from Commands.FrameworkCmd import *
from Commands.TermFrequencyCmds import *
from Commands.CodeBreakdownCmds import *
from Commands.InheritanceOverheadCmds import *
from Helpers.GitIgnoreHelper import *
from Commands.MetricsCmd import *
from Commands.CallsToExternalProvidersCmds import *
import os

commands = [MetricsCommand(), FrameworkCommand(), ForFrequencyCommand(), IfFrequencyCommand(),
            ForEachFrequencyCommand(), WhileFrequencyCommand(), CodeLinesCommand(), CommentLinesCommand(),
            MethodNumberCommand(), ClassNumberCommand(), InterfaceNumberCommand(), InheritanceDeclarationsCommand(),
            ClassInheritanceCommand(), ExternalAPICallsCommand(), HttpClientCallsCommand()]


def dispatch_command_matches(rules):
    matched_commands = []
    for rule in rules:
        for command in commands:
            if rule.lower() in command.__class__.__name__.lower().rstrip("command"):
                if command not in matched_commands:
                    matched_commands.append(command)

    return matched_commands


def process_data_from_folder(folder_path, rules):
    processed_commands = dispatch_command_matches(rules)
    sums = {}
    dict_matches = {}
    gitignore_content = read_gitignore()
    extracted_files = []
    files_roots = []
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if not should_ignore_dir(d, gitignore_content)]
        for file_name in files:
            files_roots.append(os.path.join(root, file_name))
        extracted_files.extend([file for file in files_roots if not is_ignored(file, gitignore_content)])

    for command in processed_commands:
        command_name = type(command).__name__
        if isinstance(command, FilesCommand):
            analysis_results = command.execute(files_roots)
            sums[command_name] = analysis_results
        if isinstance(command, FileNameCommand):
            for file_name in files_roots:
                analysis_results = command.execute(file_name)
                if (isinstance(analysis_results, list)):
                    if len(analysis_results) != 0:
                        if command_name not in dict_matches:
                            dict_matches[command_name] = []
                        dict_matches[command_name].extend(analysis_results)

                if (isinstance(analysis_results, int)):
                    sums[command_name] = sums.get(str(command_name), 0) + analysis_results

    print(sums)


process_data_from_folder(folder_path=r"C:/Users/user/Desktop/BPR-FE",
                         rules=["ClassNumber", "InterfaceNumber", "ExternalAPICalls", "HttpClientCalls"])
