def filter_result(result,requested_rules) -> {}:
    filtered_result = []



def dispatch_command_matches(rules):
    matched_commands = []
    commands=[]
    for rule in rules:
        for command in commands:
            if rule.lower() in command.__class__.__name__.lower():
                if command not in matched_commands:
                    matched_commands.append(command)

    return matched_commands