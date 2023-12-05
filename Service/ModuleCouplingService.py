import re
from Helpers.RegexHelper import *
from Service.CodeSimilarityService import *


def class_coupling_mapping(files) -> dict:
    class_coupling_list = {}
    for file_name in files:
        if file_name.endswith('.cs'):
            with open(file_name, 'r') as f:
                code = f.read()
                class_name = r'class (\w+)?'
                class_match = re.findall(class_name, code)
                if len(class_match) != 0:
                    matches = re.findall(CLASS_COUPLING, code)
                    list = []
                    for match in matches:
                        if match not in list:
                            list.append(match)
                    class_coupling_list[file_name] = (len(list))
    return class_coupling_list


def class_coupling_listing(folder_path, files) -> dict:
    class_coupling_list = {}
    for file_name in files:
        if file_name.endswith('.cs'):
            with open(file_name, 'r', encoding='utf8', errors='ignore') as f:
                code = f.read()
                file_base_name = file_name.replace(folder_path, "")
                class_name = r'class (\w+)?'
                class_match = re.findall(class_name, code)
                if len(class_match) != 0:
                    matches = re.findall(CLASS_COUPLING, code)
                    list = []
                    for match in matches:
                        if match not in list:
                            list.append(match)
                    class_coupling_list[file_base_name] = (len(list))
    return class_coupling_list
