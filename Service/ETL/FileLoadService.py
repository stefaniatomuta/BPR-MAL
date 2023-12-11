from Service.ETL.CSVFileService import *
from Service.ETL.TransformService import *

def write_result(result, rules):
    result = transform_extracted_data(result)
    write_to_csv(result)


