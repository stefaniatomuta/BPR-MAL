import unittest
from unittest.mock import patch
from Commands.NamespaceCmd import *
class NamespaceCmdTests(unittest.IsolatedAsyncioTestCase):
    @patch('Commands.NamespaceCmd.MismatchedNamespaceCommand.execute')
    async def test_MismatchedNamespaceCommand_is_called_once(self, mocked_command):
        folder_path = ''
        instance = MismatchedNamespaceCommand()
        await instance.execute(folder_path)
        mocked_command.assert_called_once_with(folder_path)


if __name__ == '__main__':
    unittest.main()
