from Service.CodeBreakdownService import *
from Helpers.RegexHelper import *
import re

nuget_packages = []


def get_usage_of_httpclient(files):
    usages = 0
    for file_name in files:
        matches = get_matches_in_file(file_name, APICLIENT_PATTERN)
        if matches is not None:
            for match in matches:
                usages += get_number_of_matches_in_file(file_name, match) - 2
    return usages


def get_usage_of_nuget_packages(file_roots) -> list:
    package_matches = []
    for file_name in file_roots:
        if file_name.endswith('.csproj'):
            with open(file_name, 'r', encoding='utf8', errors='ignore') as f:
                code = f.read()
                matches = re.findall(CSPROJ_PACKAGE_REFERENCE, code)
                for match in matches:
                    if match not in package_matches:
                        package_matches.append(match)
    return package_matches


def extend_nuget_packages(nugets_per_csproj) -> list:
    set1 = set(nuget_packages)
    set2 = set(nugets_per_csproj)
    nugets_to_add = set2.difference(set1)
    nuget_packages.extend(nugets_to_add)
    return nuget_packages


def get_all_nuget_packages(file_roots):
    packages = get_usage_of_nuget_packages(file_roots)
    extend_nuget_packages(packages)


def get_usings_nuget_matches(files_roots: list) -> dict:
    global nuget_packages
    nuget_matches = {}
    get_all_nuget_packages(files_roots)
    for nuget in nuget_packages:
        pattern = r'using ' + nuget
        usage_count = 0
        for file_name in files_roots:
            if file_name.endswith('.cs'):
                with open(file_name, 'r',encoding='utf8',errors='ignore') as f:
                    code = f.read()
                    matches = re.findall(pattern, code)
                    usage_count += len(matches)

            nuget_matches[nuget] = usage_count
    nuget_packages = []
    return nuget_matches
