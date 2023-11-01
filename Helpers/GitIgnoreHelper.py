import os
import fnmatch
import re


def read_gitignore(file_name) -> list:
    gitignore_content = []
    modified_lines = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('['):
                regex = r'\[([^\]]+)\](.*)'
                match = re.search(regex, line)
                first_letter = match.group(1)[0]
                second_letter = match.group(1)[1]
                upperCase = first_letter + match.group(2)
                modified_lines.append(upperCase)
                lowerCase = second_letter + match.group(2)
                modified_lines.append(lowerCase)
            else:
                modified_line = extract_git_ignore_files(line)
            if modified_line != line and modified_line is not None:
                modified_lines.append(modified_line)
        for line in lines:
            if not line.strip().startswith("#") and line.strip():
                gitignore_content.append(line.strip())
        gitignore_content.extend(modified_lines)

    return modified_lines


def extract_git_ignore_files(line: str) -> str:
    if line.startswith('*'):
        index = line.find('*')
        line = line[index + 1:].strip()
        return line


def is_ignored(file_name, gitignore_content):
    for pattern in gitignore_content:
        if file_name.startswith(pattern):
            return True
    return False


def should_ignore_dir(dir_path, gitignore_content):
    for pattern in gitignore_content:
        if dir_path.startswith(pattern):
            return True
    return False
