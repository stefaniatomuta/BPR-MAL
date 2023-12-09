from Service.CSVFileService import *
from Service.TransformService import *

def write_result(result, rules):
    result = transform_extracted_data(result)
    write_to_csv(result)



