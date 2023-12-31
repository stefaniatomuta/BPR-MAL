import fnmatch, re, os


def read_gitignore() -> list:
    gitignore_content = []
    modified_lines = []
    script_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    gitignore_path = os.path.join(script_directory, 'Config', '.gitignore')
    gitignore_path = gitignore_path.replace("\\", "/")

    with open(gitignore_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('['):
                process_square_bracket_line(line, modified_lines)
            else:
                modified_line = extract_git_ignore_files(line)
            if modified_line != line and modified_line is not None:
                modified_lines.append(modified_line)
        for line in lines:
            if not line.strip().startswith("#") and line.strip():
                gitignore_content.append(line.strip())
        gitignore_content.extend(modified_lines)

    return modified_lines


def process_square_bracket_line(line, modified_lines):
    match = re.match(r'\[([^\]]+)\](.*)', line)
    if match:
        first_letter, rest_of_line = match.group(1)[0], match.group(2)
        modified_lines.extend([first_letter + rest_of_line, first_letter.lower() + rest_of_line])


def extract_git_ignore_files(line: str) -> str:
    if line.startswith('*'):
        index = line.find('*')
        line = line[index + 1:].strip()
        if line.endswith('/\n'):
            line = line.rstrip('/\n')
        return line


def is_ignored(file_name, gitignore_content):
    for pattern in gitignore_content:
        if file_name.startswith(pattern):
            return True
        if file_name.endswith(('.dll', '.md', '.sln', '.DotSettings.user', '.css', '.js', '.xml', '.nupkg','.gitattributes')):
            return True
    return False


def should_ignore_dir(dir_path, gitignore_content):
    for pattern in gitignore_content:
        if pattern.endswith('/'):
            pattern = pattern.rstrip('/')
        if fnmatch.fnmatch(dir_path, pattern):
            return True
    return False
