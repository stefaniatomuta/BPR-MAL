import os
def read_gitignore(file_name):
    gitignore_content = []
    modified_lines = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            modified_line = extract_git_ignore_files(line)
            if modified_line != line:
                modified_lines.append(modified_line)
        for line in lines:
            if not line.strip().startswith("#") and line.strip():
                gitignore_content.append(line.strip())
        gitignore_content.extend(modified_lines)

    return gitignore_content

def extract_git_ignore_files(line: str):
    if line.startswith('*'):
        index = line.find('*')
        line = line[index + 1:].strip()

