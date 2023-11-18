import re

from Helpers.RegexHelper import *
from Service.EOLService import EOL_API


def get_matches(file_name) -> dict:
    patterns = [TARGET_FRAMEWORK, TARGET_FRAMEWORK_VERSION]
    file_matches = {}
    if file_name.endswith('.csproj'):
        with open(file_name, 'r', encoding='utf8') as f:
            code = f.read()
            for pattern in patterns:
                matches = re.findall(pattern, code)
                for match in matches:
                    file_matches[file_name] = match
    return file_matches


def get_number_eod_frameworks(file_name) -> int:
    count = []
    for file, match in get_matches(file_name).items():
        info = EOL_API(match)
        if info:
            if info.isEndOfLife:
                count.append(info)
    return len(count)
