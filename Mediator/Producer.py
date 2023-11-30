from aio_pika import connect_robust, Message
from Config.Config import *
import json

async def send_to_rabbitmq(message):
    connection = await connect_robust(connection_url)
    
    channel = await connection.channel()
    await channel.default_exchange.publish(
        Message(body=json.dumps(message).encode()),
        routing_key = producer_queue_name
    )
    await connection.close()
