import unittest
from unittest.mock import MagicMock, patch
from Mediator.Producer import send_to_rabbitmq

class TestGenericProducer(unittest.TestCase):
    async def test_publish_message(self):
        with patch('aio_pika.connect_robust') as mock_connect_robust:
            mock_connection = MagicMock()
            mock_channel = MagicMock()

            mock_connect_robust.return_value = mock_connection
            mock_connection.channel.return_value = mock_channel
            mock_channel.default_exchange = MagicMock()

            message = {"data": "Send analysis"}
            await send_to_rabbitmq(message)

            mock_connect_robust.assert_called_once()
            mock_connection.channel.assert_called_once()
            mock_channel.default_exchange.publish.assert_called_once()

if __name__ == '__main__':
    unittest.main()