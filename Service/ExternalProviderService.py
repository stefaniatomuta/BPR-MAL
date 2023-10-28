from Helpers.RegexHelper import APICLIENT_PATTERN
from CodeBreakdownService import *

def get_usage_of_httpclient_var(file_name):
    var = get_matches_in_file(file_name,APICLIENT_PATTERN)
    usages = 0
    if var is not None:
        for match in var:
            usages += get_number_of_matches_in_file(file_name,match) - 2
    return usages