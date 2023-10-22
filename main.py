from fastapi import FastAPI
from API.models import Result, Violation, Rule


app = FastAPI()
@app.post("/post")
async def upload_code(item: str):
    rule = Rule("Dependency","Wrong dependency", True)
    violation = Violation("Violation 1", "Wrong dependencies", "Medium", "Architecture", "public static...", rule)
    result = Result(0.2,[violation])
    return {"result": result}