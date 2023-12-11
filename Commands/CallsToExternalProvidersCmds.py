from Commands.CommandModel import *
from Service.Analysis.ExternalProviderService import *


class ExternalAPICallsCommand(FilesCommand):
    def execute(self, files_roots: list) -> dict:
        return get_usings_nuget_matches(files_roots)


class HttpClientCallsCommand(FilesCommand):
    def execute(self, file_roots: list) -> Any:
        return get_usage_of_httpclient(file_roots)
