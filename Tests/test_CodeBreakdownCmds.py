import unittest
from unittest.mock import patch
from Commands.CodeBreakdownCmds import *


class CodeBreakdownCmdsTests(unittest.IsolatedAsyncioTestCase):
    @patch('Commands.CodeBreakdownCmds.CodeLinesCommand.execute')
    async def test_CodeLinesCommand_is_called_once(self, mocked_command):
        file_name = ''
        instance = CodeLinesCommand()
        await instance.execute(file_name)
        mocked_command.assert_called_once_with(file_name)

    @patch('Commands.CodeBreakdownCmds.CommentLinesCommand.execute')
    async def test_CommentLinesCommand_is_called_once(self, mocked_command):
        file_name = ''
        instance = CommentLinesCommand()
        await instance.execute(file_name)
        mocked_command.assert_called_once_with(file_name)

    @patch('Commands.CodeBreakdownCmds.MethodNumberCommand.execute')
    async def test_MethodNumberCommand_is_called_once(self, mocked_command):
        file_name = ''
        instance = MethodNumberCommand()
        await instance.execute(file_name)
        mocked_command.assert_called_once_with(file_name)

    @patch('Commands.CodeBreakdownCmds.ClassNumberCommand.execute')
    async def test_ClassNumberCommand_is_called_once(self, mocked_command):
        file_name = ''
        instance = ClassNumberCommand()
        await instance.execute(file_name)
        mocked_command.assert_called_once_with(file_name)

    @patch('Commands.CodeBreakdownCmds.InterfaceNumberCommand.execute')
    async def test_InterfaceNumberCommand_is_called_once(self, mocked_command):
        file_name = ''
        instance = InterfaceNumberCommand()
        await instance.execute(file_name)
        mocked_command.assert_called_once_with(file_name)

    @patch('Commands.CodeBreakdownCmds.UsingsNumberCommand.execute')
    async def test_UsingsNumberCommand_is_called_once(self, mocked_command):
        file_name = ''
        instance = UsingsNumberCommand()
        await instance.execute(file_name)
        mocked_command.assert_called_once_with(file_name)

    @patch('Commands.CodeBreakdownCmds.CodeSimilarityCommand.execute')
    async def test_CodeSimilarityCommand_is_called_once(self, mocked_command):
        folder_path = ''
        instance = CodeSimilarityCommand()
        await instance.execute(folder_path)
        mocked_command.assert_called_once_with(folder_path)

    @patch('Commands.CodeBreakdownCmds.CodeLinesPerFileCommand.execute')
    async def test_CodeLinesPerFileCommand_is_called_once(self, mocked_command):
        file_name = ''
        folder_path = ''
        instance = CodeLinesPerFileCommand()
        await instance.execute(folder_path, file_name)
        mocked_command.assert_called_once_with(folder_path, file_name)

    @patch('Commands.CodeBreakdownCmds.CommentLinesPerFileCommand.execute')
    async def test_CommentLinesPerFileCommand_is_called_once(self, mocked_command):
        file_name = ''
        folder_path = ''
        instance = CommentLinesPerFileCommand()
        await instance.execute(folder_path, file_name)
        mocked_command.assert_called_once_with(folder_path, file_name)

    @patch('Commands.CodeBreakdownCmds.CSFilesCommand.execute')
    async def test_CSFilesCommand_is_called_once(self, mocked_command):
        file_name = ''
        instance = CSFilesCommand()
        await instance.execute(file_name)
        mocked_command.assert_called_once_with(file_name)