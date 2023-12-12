import unittest
from unittest.mock import patch
from Commands.CallsToExternalProvidersCmds import *
class CallsToExternalProviversCmdsTests(unittest.IsolatedAsyncioTestCase):
    @patch('Commands.CallsToExternalProvidersCmds.ExternalAPICallsCommand.execute')
    async def test_ExternalApiCallsCommand_is_called_once(self,mocked_command):
        files_roots = []
        instance = ExternalAPICallsCommand()
        await instance.execute(files_roots)
        mocked_command.assert_called_once_with(files_roots)

    @patch('Commands.CallsToExternalProvidersCmds.HttpClientCallsCommand.execute')
    async def test_HttpClientCallsCommand_is_called_once(self, mocked_command):
        files_roots = []
        instance = HttpClientCallsCommand()
        await instance.execute(files_roots)
        mocked_command.assert_called_once_with(files_roots)