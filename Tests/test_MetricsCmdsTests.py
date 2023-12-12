import unittest
from unittest.mock import patch
from Commands.MetricsCmd import *

class MetricsCmdsTests(unittest.IsolatedAsyncioTestCase):
    @patch('Commands.MetricsCmd.ClassCouplingListingCommand.execute')
    async def test_ClassCouplingListingCommand_is_called_once(self, mocked_command):
        files = []
        folder_path = ''
        instance = ClassCouplingListingCommand()
        await instance.execute(folder_path, files)
        mocked_command.assert_called_once_with(folder_path, files)


if __name__ == '__main__':
    unittest.main()
