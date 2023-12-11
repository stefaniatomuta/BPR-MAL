import re, aiofiles

async def get_number_of_matches_in_file(file_name, pattern):
    async with aiofiles.open(file_name, 'r', encoding='utf8', errors='ignore') as file:
        if file_name.endswith('.cs'):
            code = await file.read()
            matches = re.findall(pattern, code, re.MULTILINE)
            return len(matches)
        else:
            return 0


async def get_matches_in_file(file_name, pattern):
    async with aiofiles.open(file_name, 'r', encoding='utf8', errors='ignore') as file:
        if file_name.endswith('.cs'):
            code = await file.read()
            matches = re.findall(pattern, code, re.MULTILINE)
            return matches
        else:
            return None


async def get_matches_in_files(files, pattern):
    matches = [get_matches_in_file(file, pattern) for file in files]
    filteredList = []
    for item in matches:
        if item:
            filteredList.append(item)
    return filteredList


async def get_match_with_file(folder_path, file_name, pattern) -> dict:
    async with aiofiles.open(file_name, 'r', encoding='utf8', errors='ignore') as file:
        if file_name.endswith('.cs'):
            code = await file.read()
            matches = re.findall(pattern, code, re.MULTILINE)
            relpath = file_name.replace(folder_path, "")
            return {relpath: len(matches)}
