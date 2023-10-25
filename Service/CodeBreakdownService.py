import re
def get_matches_in_file(file_name, pattern):
    with open(file_name, 'r', encoding='utf8', errors='ignore') as file:
        if file_name.endswith('.cs'):
            code = file.read()
            matches = re.findall(pattern, code, re.MULTILINE)
            return len(matches)
        else:
            return 0