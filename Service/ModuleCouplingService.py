import re
from Helpers.RegexHelper import *

def test(file_name) -> dict:
    class_coupling_values = {}
    if file_name.endswith('.cs'):
        with open(file_name, 'r') as f:
            code = f.read()
            class_name = r'class (\w+)?'
            class_match = re.findall(class_name, code)
            if len(class_match) != 0:
                exp = CLASS_COUPLING
                matches = re.findall(exp, code)
                class_name = class_match[0]
                list = []
                for match in matches:
                    if match not in list:
                        list.append(match)
                        class_coupling_values[class_name] = len(list)

    return class_coupling_values