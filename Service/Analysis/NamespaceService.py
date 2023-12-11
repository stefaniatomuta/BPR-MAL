from Helpers.RegexHelper import *
import re, os, aiofiles

directories_and_files = {}
files_and_namespaces = {}

async def get_directories(folder_path) -> dict:
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.cs') | file.endswith('.cshtml'):
                directories_and_files[root] = files
        
    for root, files in directories_and_files.items():
        for file_name in files:
            file_path = os.path.join(root, file_name)
            async with aiofiles.open(file_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
                code = await f.read()
                matches = re.findall(NAMESPACE, code, re.MULTILINE)
                for match in matches:
                    corresponding_file = os.path.relpath(root, folder_path).replace("\\", ".")
                    files_and_namespaces[corresponding_file] = match

    return files_and_namespaces


async def get_namespace_analysis(folder_path) -> int:
    global directories_and_files, files_and_namespaces
    violations = 0
    get_directories(folder_path)
    for file_name, m in files_and_namespaces.items():
        if file_name != m:
            violations += 1
    directories_and_files = {}
    files_and_namespaces = {}
    return violations

