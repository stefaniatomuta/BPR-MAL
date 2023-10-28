# number of APi calls in a file?
# authentication calls
# database calls -> what if they use frameworks?
# number of 3rd party libraries -> how exactly
from Commands.CommandModel import Command
from Service.ExternalProviderService import *

class ExternalAPICallsCommand(Command):
    def execute(self, file_name: str) -> int:
        return get_usage_of_httpclient_var(file_name)