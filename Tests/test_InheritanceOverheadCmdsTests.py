import unittest
from unittest.mock import patch
from Commands.InheritanceOverheadCmds import *

class InheritanceOverheadCmdsTests(unittest.IsolatedAsyncioTestCase):
    @patch('Commands.InheritanceOverheadCmds.InheritanceDeclarationsCommand.execute')
    async def test_InheritanceDeclarationsCommand_is_called_once(self, mocked_command):
        file_name = ''
        instance = InheritanceDeclarationsCommand()
        await instance.execute(file_name)
        mocked_command.assert_called_once_with(file_name)

    @patch('Commands.InheritanceOverheadCmds.InheritanceDepthCommand.execute')
    async def test_InheritanceDepthCommand_is_called_once(self, mocked_command):
        files = []
        instance = InheritanceDepthCommand()
        await instance.execute(files)
        mocked_command.assert_called_once_with(files)


if __name__ == '__main__':
    unittest.main()
