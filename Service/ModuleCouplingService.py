import re
from Helpers.RegexHelper import *


def class_coupling(file_name) -> list:
    class_coupling_list = []
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
                class_coupling_list.append(len(list))
    return class_coupling_list
