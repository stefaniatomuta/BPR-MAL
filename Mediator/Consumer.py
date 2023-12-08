import time
from Handlers.RequestHandler import process_request
from Mediator.Producer import send_to_rabbitmq
from Config.Config import *
import pika

async def process_message(requestQueue):
    while True:
        if not requestQueue.empty():
            print("Request received! Processing...")
            message = requestQueue.get()
            try:
                data = eval(message.decode())
                result = process_request(data['path'], data['rules'], data['correlation_id'])
                await send_to_rabbitmq(result)
                print("Processed result:", result)
            except Exception as e:
                print(f"Error processing message: {e}")
        time.sleep(5)


def consume_from_queue(requestQueue):
    print("Setting up consumer queue...")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    channel.queue_declare(queue=consumer_queue_name)

    def consume_callback(ch, method, properties, body):
        requestQueue.put(body)

    channel.basic_consume(queue=consumer_queue_name, on_message_callback=consume_callback, auto_ack=True)
    print('Consumer queue created! Listening for messages...')
    channel.start_consuming()
