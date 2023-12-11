from Service.ETL.ExtractionService import *
from Service.ETL.FileLoadService import *
from Service.Helpers.CommandHandlerService import *
from Service.MAL.MLService import *

TrainModel = False

async def process_request(folder_path, request_rules, correlation_id):
    extraction_result, all_rules = await process_data_from_folder(folder_path)
    intact_extraction = extraction_result
    processed_result = filter_result(intact_extraction, request_rules)
    processed_result['correlationId'] = correlation_id
    if processed_result.get('codesimilarity'):
        processed_result['codesimilarity'] = filter_code_similarity(processed_result['codesimilarity'])
    if TrainModel:
        write_result(extraction_result, all_rules)
    processed_result['technicaldebtlabel'] = predict(extraction_result)
    return processed_result

async def automate_data_insertion(root_folder):
    for folder in os.listdir(root_folder):
        folder_path = os.path.join(root_folder,folder)
        extraction_result, all_rules = await process_data_from_folder(folder_path)
        write_result(extraction_result,all_rules)

def test_mal(root_folder):
    for folder in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder)
        process_request(folder_path, [""])
