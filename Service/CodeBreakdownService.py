import re
from Helpers.RegexHelper import CODELINES_PATTERN,COMMENTS_PATTERN

def get_lines_of_code(file_name):
    with open(file_name, 'r', encoding='utf8', errors='ignore') as file:
        if file_name.endswith('.cs'):
            code = file.read()
            matches = re.findall(CODELINES_PATTERN, code, re.MULTILINE)
            return len(matches)
        else:
            return 0

def get_comment_lines(file_name):
    with open(file_name, 'r', encoding='utf8', errors='ignore') as file:
        if file_name.endswith('.cs'):
            code = file.read()
            matches = re.findall(COMMENTS_PATTERN, code, re.MULTILINE)
            return len(matches)
        else: return 0