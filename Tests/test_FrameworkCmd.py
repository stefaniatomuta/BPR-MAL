import unittest
from unittest.mock import patch
from Commands.FrameworkCmd import *


class FrameworkCmdTests(unittest.IsolatedAsyncioTestCase):
    @patch('Commands.FrameworkCmd.EndOfLifeFrameworkCommand.execute')
    async def test_EndOfLifeFrameworkCommand_is_called_once(self, mocked_command):
        file_name = ''
        folder_path = ''
        instance = EndOfLifeFrameworkCommand()
        await instance.execute(file_name,folder_path)
        mocked_command.assert_called_once_with(file_name, folder_path)


if __name__ == '__main__':
    unittest.main()
