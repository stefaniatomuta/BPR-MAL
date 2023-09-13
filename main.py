from fastapi import FastAPI
from API.models import Result, Violation

app = FastAPI()
@app.post("/post")
async def upload_code(item: str):
    violation = Violation("Violation 1", "Wrong dependencies", "Medium", "Architecture", "public static...")
    result = Result(0.2,[violation])
    return {"result": result}