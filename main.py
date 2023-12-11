import multiprocessing
from Mediator.Consumer import *
from Mediator.Producer import *
from Handlers.RequestHandler import *
import asyncio

def start_processing(queue):
  asyncio.run(process_message(queue))

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    processer = multiprocessing.Process(target=start_processing, args=(queue,))
    processer.start()
    asyncio.run(consume_from_queue(queue))
