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
            ClassInheritanceCommand(), ExternalAPICallsCommand()]


def dispatch_command_matches(rules):
    matched_commands = []
    for rule in rules:
        for command in commands:
            if rule.lower() in command.__class__.__name__.lower().rstrip("command"):
                matched_commands.append(command)

    return matched_commands


def process_data_from_folder(folder_path, rules):
    processed_commands = dispatch_command_matches(rules)
    sums = {}
    dict_matches = {}
    class_matches = []
    csfiles = 0
    gitignore_content = read_gitignore()

    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if not should_ignore_dir(d, gitignore_content)]
        files = [file for file in files if not is_ignored(file, gitignore_content)]
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name.endswith('.cs'):
                csfiles += 1
                class_matches.extend(get_matches_in_file(file_path, CLASS_PATTERN))
            for command in processed_commands:
                command_name = type(command).__name__
                analysis_results = command.execute(file_path)
                if (isinstance(analysis_results, list)):
                    if len(analysis_results) != 0:
                        if command_name not in dict_matches:
                            dict_matches[command_name] = []
                        dict_matches[command_name].extend(analysis_results)

                if (isinstance(analysis_results, int)):
                    sums[command_name] = sums.get(str(command_name), 0) + analysis_results

    # print("inheritance tree max depth: " + repr(get_max_inheritance_depth(class_matches)))
    # print(dict_matches)
    print(sums)
