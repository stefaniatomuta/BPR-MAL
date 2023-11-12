import re


def get_number_of_matches_in_file(file_name, pattern):
    with open(file_name, 'r', encoding='utf8', errors='ignore') as file:
        if file_name.endswith('.cs'):
            code = file.read()
            matches = re.findall(pattern, code, re.MULTILINE)
            return len(matches)
        else:
            return 0


def get_matches_in_file(file_name, pattern):
    with open(file_name, 'r', encoding='utf8', errors='ignore') as file:
        if file_name.endswith('.cs'):
            code = file.read()
            matches = re.findall(pattern, code, re.MULTILINE)
            return matches
        else:
            return None


def get_matches_in_files(files, pattern):
    matches = [get_matches_in_file(file,pattern) for file in files]
    filteredList = []
    for item in matches:
        if item:
            filteredList.append(item)
    return filteredList