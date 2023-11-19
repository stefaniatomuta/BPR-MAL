from Helpers.CommandHelper import commands


def filter_result(result, requested_rules) -> {}:
    filtered_rules = dispatch_command_matches(requested_rules)
    filtered_results = {}
    for command in filtered_rules:
        command_name = command.__class__.__name__
        command_key = command_name.lower().rstrip('command')
        for resKey, resVal in result.items():
            if resKey.lower() == command_key:
                filtered_results[command_key] = resVal

    return filtered_results


def filter_code_similarity(result):
    return {outer_key: {inner_key: value for inner_key, value in inner_dict.items() if value > 15} for
            outer_key, inner_dict in result.items()}


def dispatch_command_matches(rules):
    matched_commands = []
    for rule in rules:
        for command in commands:
            if rule.lower() in command.__class__.__name__.lower():
                if command not in matched_commands:
                    matched_commands.append(command)

    return matched_commands
