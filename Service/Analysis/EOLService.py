import aiohttp
from API.eodl_models import FrameworkInfo, FrameworkDetails

# Service for EODL integration
mappings = {
    "dotnet ": "net",
    "dotnet": "netstandard",
    "dotnetcore": "netcoreapp",
    "dotnetfx": "v"
}


def frameworks_mappings(value):
    for key, val in mappings.items():
        if val.strip(' ') == value:
            return key.strip(' ')
    return None


def type_and_cycle_splitter(target_framework) -> FrameworkInfo:
    digits = next((i for i, char in enumerate(target_framework) if char.isdigit()), len(target_framework))
    type = target_framework[:digits]
    cycle = target_framework[digits:]
    type = frameworks_mappings(type)
    return FrameworkInfo(type, cycle, 1)


async def EOL_API(target_framework) -> FrameworkInfo:
    info = type_and_cycle_splitter(target_framework)
    url = f"https://endoflife.date/api/{info.type}/{info.cycle}.json"
    # request = requests.get(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                # data = json.loads(response.text)
                data = await response.json()
                details = FrameworkDetails(data['releaseDate'], data['eol'], data['lts'])
                info.isEndOfLife = details.end_of_life()
                return info
            else:
                print(f"Request to {url} failed with status code {response.status_code}")
