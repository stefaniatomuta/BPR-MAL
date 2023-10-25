import re
from Helpers.RegexHelper import IF_PATTERN,FOREACH_PATTERN,FOR_PATTERN,WHILE_PATTERN

def get_number_of_ifs_in_file(file_path):
    with open(file_path, 'r', encoding='utf8', errors='ignore') as file:
        if file_path.endswith('.cs'):
            code = file.read()
            for_matches = re.findall(IF_PATTERN, code, re.MULTILINE)
            return len(for_matches)
        else:
            return 0


def get_number_of_fors_in_file(file_path):
    with open(file_path, 'r', encoding='utf8', errors='ignore') as file:
        if file_path.endswith('.cs'):
            code = file.read()
            matches = re.findall(FOR_PATTERN, code, re.MULTILINE)
            return len(matches)
        else:
            return 0

def get_number_of_foreaches_in_file(file_path):
    with open(file_path, 'r', encoding='utf8', errors='ignore') as file:
        if file_path.endswith('.cs'):
            code = file.read()
            matches = re.findall(FOREACH_PATTERN, code, re.MULTILINE)
            return len(matches)
        else:
            return 0


def get_number_of_whiles_in_file(file_path):
    with open(file_path, 'r', encoding='utf8', errors='ignore') as file:
        if file_path.endswith('.cs'):
            code = file.read()
            matches = re.findall(WHILE_PATTERN, code, re.MULTILINE)
            return len(matches)
        else:
            return 0
