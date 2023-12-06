import multiprocessing
from pydantic import BaseModel, constr, Field
from Mediator.Consumer import *
from Mediator.Producer import *
import asyncio

class RequestBody(BaseModel):
    path: constr(min_length=1, strip_whitespace=True)
    rules: list[str] = Field(min_length=1)

def start_processing(queue):
  asyncio.run(process_message(queue))

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    processer = multiprocessing.Process(target=start_processing, args=(queue,))
    processer.start()
    asyncio.run(consume_from_queue(queue))
