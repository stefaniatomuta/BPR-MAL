from aio_pika import connect_robust
from Handlers.RequestHandler import process_request
from Mediator.Producer import send_to_rabbitmq
from Config.Config import *

async def process_message(message):
    async with message.process():
        try:
            data = eval(message.body.decode())
            result = process_request(data['path'], data['rules'], data['correlation_id'])
            await send_to_rabbitmq(result)
            print("Processing result:", result)
        except Exception as e:
            print(f"Error processing message: {e}")


async def consume_from_queue():
    connection = await connect_robust(connection_url)
    channel = await connection.channel()
    
    queue = await channel.declare_queue(consumer_queue_name)
    await queue.consume(process_message)


