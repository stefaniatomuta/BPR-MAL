def calculate_depth(class_name, class_matches):
    class_depths = get_class_depths(class_matches)
    if class_name not in class_depths:
        return 0
    return 1 + calculate_depth(class_depths[class_name],class_matches)

def get_class_depths(class_matches):
    class_depths = {}
    for class_match in class_matches:
        class_name, base_class = class_match[0]
        if base_class:
            class_depths[class_name] = base_class
    return class_depths

async def get_max_inheritance_depth(class_matches):
    max_depth = 0
    if len(class_matches):
        max_depth = max([calculate_depth(clas, class_matches) for clas in get_class_depths(class_matches).keys()])
    return max_depth

