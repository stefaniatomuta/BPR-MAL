from aio_pika import connect_robust
from Handlers.RequestHandler import process_request
from Config.Config import *

async def process_message(message):
    async with message.process():
        try:
            data = eval(message.body.decode())
            result = process_request(data['path'], data['rules'])
            print("Processing result:", result)
        except Exception as e:
            print(f"Error processing message: {e}")


async def consume_from_queue():
    connection = await connect_robust(connection_url)
    channel = await connection.channel()
    
    queue = await channel.declare_queue(queue_name)
    await queue.consume(process_message)


