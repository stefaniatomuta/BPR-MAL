from aio_pika import connect_robust, Message
from Config.Config import *

async def send_to_rabbitmq(message):
    connection = await connect_robust(connection_url)
    channel = await connection.channel()
    await channel.default_exchange.publish(
        Message(body=str(message).encode()),
        routing_key = queue_name,
    )
    await connection.close()
