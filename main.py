from pydantic import BaseModel, constr, Field
from Mediator.Consumer import *
from Mediator.Producer import *
import asyncio

class RequestBody(BaseModel):
    path: constr(min_length=1, strip_whitespace=True)
    rules: list[str] = Field(min_length=1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(consume_from_queue())
    loop.run_forever()
