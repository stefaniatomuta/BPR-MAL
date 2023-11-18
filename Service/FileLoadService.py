from CSVFileService import *
from CodeSimilarityService import get_code_similarity_values

def write_result(result, rules):
    result = process_code_similarity(result)
    write_column_headers_to_csv(rules)
    write_to_csv(result)
    print(result)

def process_code_similarity(result):
    result['CodeSimilarity'] = get_code_similarity_values(result['CodeSimilarity'])
    return result