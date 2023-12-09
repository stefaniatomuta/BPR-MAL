def transform_extracted_data(result):
    result['CodeSimilarity'] = get_list_values_from_sub_dict(result['CodeSimilarity'])
    result['ClassCouplingListing'] = get_list_values_from_dict(result['ClassCouplingListing'])
    result['EndOfLifeFramework'] = count_true_statuses(result['EndOfLifeFramework'])
    result['ExternalAPICalls'] = get_list_values_from_dict(result['ExternalAPICalls'])
    result['CodeLinesPerFile'] = get_from_list(result['CodeLinesPerFile'])
    result['CommentLinesPerFile'] = get_from_list(result['CommentLinesPerFile'])
    return result

def get_from_list(data):
    return [value for dictionary in data for value in dictionary.values() if isinstance(value, (int, float))]


def count_true_statuses(data):
    count = 0
    for item in data:
        for _, value in item.items():
            if value.get("status") is True:
                count += 1
    return count


def get_list_values_from_dict(dict):
    return list(dict.values())


def get_list_values_from_sub_dict(dict):
    all_values = [value for sub_dict in dict.values() for value in sub_dict.values()]
    return list(dict.fromkeys(all_values))
