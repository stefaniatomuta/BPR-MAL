from Service.ExtractionService import *
from Service.FileLoadService import *
from Service.CommandHandlerService import *


##TODO: once the ML part is ready add a service that deals with that and is called here to return the value together with the rest
def process_request(folder_path, request_rules):
    extraction_result, all_rules = process_data_from_folder(folder_path)
    res = filter_result(extraction_result, request_rules)
    return res
    # write_result(extraction_result, all_rules)
