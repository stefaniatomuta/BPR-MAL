from fastapi import FastAPI
from API.models import Result, Violation, Rule


app = FastAPI()
@app.post("/post")
async def upload_code(item: str):
    rule = Rule("Dependency","Wrong dependency", True)
    violation = Violation("Violation 1", "Wrong dependencies", "Medium", "Architecture", "public static...", rule)
    result = Result(0.2,[violation])
    return {"result": result}

import json

j = {"cycle": "4.8.1", "releaseDate": "2022-08-09", "eol": "false", "lts": "false"}
class FrameworkDetails:
    def __init__(self, cycle, releaseDate, eol, lts):
        self.cycle = cycle
        self.releaseDate = releaseDate
        self.eol = eol
        self.lts = lts
class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

p = Payload(j)

print(p.data)