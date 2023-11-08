# number of APi calls in a file?
# authentication calls
# database calls -> what if they use frameworks?
# number of 3rd party libraries -> how exactly
from Commands.CommandModel import FilesCommand
from Service.ExternalProviderService import *


class ExternalAPICallsCommand(FilesCommand):
    def execute(self, files: str) -> int:
        return get_usage_of_httpclient_var(files)
