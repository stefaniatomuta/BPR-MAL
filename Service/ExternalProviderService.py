from Helpers.RegexHelper import APICLIENT_PATTERN
from Service.CodeBreakdownService import get_number_of_matches_in_file, get_matches_in_file
from Helpers.RegexHelper import *
import re

nuget_packages = []


def get_usage_of_httpclient_var(file_name):
    var = get_matches_in_file(file_name, APICLIENT_PATTERN)
    usages = 0
    if var is not None:
        for match in var:
            usages += get_number_of_matches_in_file(file_name, match) - 2
    return usages


def get_usage_of_nuget_packages(file_name) -> list:
    package_matches = []
    if file_name.endswith('.csproj'):
        with open(file_name, 'r') as f:
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


def get_all_nuget_packages(file_name):
    if file_name.endswith('.csproj'):
        packages = get_usage_of_nuget_packages(file_name)
        extend_nuget_packages(packages)


def get_usings_nuget_matches(file_name) -> dict:
    nuget_matches = {}
    get_all_nuget_packages(file_name)
    for nuget in nuget_packages:
        pattern = r'using ' + nuget
        if file_name.endswith('.cs'):
            with open(file_name, 'r') as f:
                code = f.read()
                package_matches = []
                matches = re.findall(pattern, code)
                for match in matches:
                    if match not in package_matches:
                        package_matches.append(match)
                nuget_matches[nuget] = len(package_matches)

    return nuget_matches
