import json
import requests
from API.eodl_models import FrameworkInfo, FrameworkDetails

# Service for EODL integration
mappings = {
    "dotnet": "net",
    "dotnetcore": "netcoreapp",
    "dotnetfx": "v"
}

def frameworks_mappings(value):
    for key, val in mappings.items():
        if val == value:
            return key
    return None
def type_and_cycle_splitter(target_framework) -> FrameworkInfo:
    digits = next((i for i, char in enumerate(target_framework) if char.isdigit()), len(target_framework))
    type = target_framework[:digits]
    cycle = target_framework[digits:]
    type = frameworks_mappings(type)
    return FrameworkInfo(type, cycle, None)

def EOL_API(target_framwework) -> FrameworkInfo:
    info = type_and_cycle_splitter(target_framwework)
    url = f"https://endoflife.date/api/{info.type}/{info.cycle}.json"
    request = requests.get(url)
    if request.status_code == 200:
        data = json.loads(request.text)
        details = FrameworkDetails(data['releaseDate'], data['eol'], data['lts'])
        info.isEndOfLife = details.end_of_life()
        return info
    else:
        print(f"Request to {url} failed with status code {request.status_code}")

