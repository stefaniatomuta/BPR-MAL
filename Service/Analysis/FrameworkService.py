import re, aiofiles
from Helpers.RegexHelper import *
from Service.Analysis.EOLService import EOL_API


async def get_matches(file_name, folder_path) -> dict:
    patterns = [TARGET_FRAMEWORK, TARGET_FRAMEWORK_VERSION]
    file_matches = {}
    if file_name.endswith('.csproj'):
        async with aiofiles.open(file_name, 'r', encoding='utf8', errors='ignore') as f:
            code = await f.read()
            file_base_name = file_name.replace(folder_path, "")
            for pattern in patterns:
                matches = re.findall(pattern, code)
                for match in matches:
                    info = await EOL_API(match)
                    file_matches[file_base_name] = {'version': match, 'status': info.isEndOfLife if info else False}
    return file_matches
