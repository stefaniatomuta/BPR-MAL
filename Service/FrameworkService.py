import os
import re

from Helpers.RegexHelper import *
from Service.EOLService import EOL_API


def get_matches(file_name, folder_path) -> dict:
    patterns = [TARGET_FRAMEWORK, TARGET_FRAMEWORK_VERSION]
    file_matches = {}
    if file_name.endswith('.csproj'):
        with open(file_name, 'r', encoding='utf8', errors='ignore') as f:
            code = f.read()
            file_base_name = file_name.replace(folder_path, "")
            for pattern in patterns:
                matches = re.findall(pattern, code)
                for match in matches:
                    info = EOL_API(match)
                    file_matches[file_base_name] = {'version': match, 'status': info.isEndOfLife if info else False}
    return file_matches
