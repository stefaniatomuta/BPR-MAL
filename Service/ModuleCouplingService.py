import re
from Helpers.RegexHelper import *

def test(file_name) -> list:
    class_coupling_values = {}
    class_coupling_list = []
    if file_name.endswith('.cs'):
        with open(file_name, 'r') as f:
            code = f.read()
            class_name = r'class (\w+)?'
            class_matches = re.findall(class_name, code)
            if len(class_matches) != 0:
                matches = re.findall(CLASS_COUPLING, code)
                list = []
                for match in matches:
                    if match not in list:
                        list.append(match)
                        class_coupling_values[class_name] = len(list)
        for key, val in class_coupling_values.items():
            class_coupling_list.append(val)
    return class_coupling_list