from Service.ExtractionService import *
from Service.FileLoadService import *
from Service.CommandHandlerService import *

TrainModel = False

##TODO: once the ML part is ready add a service that deals with that and is called here to return the value together with the rest
def process_request(folder_path, request_rules):
    extraction_result, all_rules = process_data_from_folder(folder_path)
    intact_extraction = extraction_result
    processed_result = filter_result(intact_extraction, request_rules)
    if processed_result.get('codesimilarity'):
        processed_result['codesimilarity'] = filter_code_similarity(processed_result['codesimilarity'])
    if TrainModel:
        write_result(extraction_result, all_rules)
    return processed_result

def automate_data_insertion(root_folder):
    for folder in os.listdir(root_folder):
        folder_path = os.path.join(root_folder,folder)
        extraction_result, all_rules = process_data_from_folder(folder_path)
        write_result(extraction_result,all_rules)

