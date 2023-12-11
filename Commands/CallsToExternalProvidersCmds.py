from Commands.CommandModel import *
from Service.Analysis.ExternalProviderService import *


class ExternalAPICallsCommand(FilesCommand):
    async def execute(self, files_roots: list) -> dict:
        return await get_usings_nuget_matches(files_roots)


class HttpClientCallsCommand(FilesCommand):
    async def execute(self, file_roots: list) -> Any:
        return await get_usage_of_httpclient(file_roots)
