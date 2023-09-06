from fastapi import FastAPI

app = FastAPI()
@app.post("/post")
async def upload_code(item: str):
    return {"item": item}