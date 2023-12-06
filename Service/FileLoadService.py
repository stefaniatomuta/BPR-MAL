from Service.CSVFileService import *
from Service.TransformService import *

def write_result(result, rules):
    result = process_code_similarity(result)
    # write_column_headers_to_csv(rules)
    write_to_csv(result)



