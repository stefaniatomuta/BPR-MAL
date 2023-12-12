import unittest
from unittest.mock import patch
from Commands.TermFrequencyCmds import *


class TermFrequencyCmdsTests(unittest.IsolatedAsyncioTestCase):
    @patch('Commands.TermFrequencyCmds.ForFrequencyCommand.execute')
    async def test_ForFrequencyCommand_is_called_once(self, mocked_command):
        file_name = ''
        instance = ForFrequencyCommand()
        await instance.execute(file_name)
        mocked_command.assert_called_once_with(file_name)

    @patch('Commands.TermFrequencyCmds.ForEachFrequencyCommand.execute')
    async def test_ForEachFrequencyCommand_is_called_once(self, mocked_command):
        file_name = ''
        instance = ForEachFrequencyCommand()
        await instance.execute(file_name)
        mocked_command.assert_called_once_with(file_name)

    @patch('Commands.TermFrequencyCmds.IfFrequencyCommand.execute')
    async def test_IfFrequencyCommand_is_called_once(self, mocked_command):
        file_name = ''
        instance = IfFrequencyCommand()
        await instance.execute(file_name)
        mocked_command.assert_called_once_with(file_name)

    @patch('Commands.TermFrequencyCmds.WhileFrequencyCommand.execute')
    async def test_WhileFrequencyCommand_is_called_once(self, mocked_command):
        file_name = ''
        instance = WhileFrequencyCommand()
        await instance.execute(file_name)
        mocked_command.assert_called_once_with(file_name)
