from fastapi import FastAPI
from pydantic import BaseModel, constr, Field
from Handlers.RequestHandler import process_request

app = FastAPI()


class RequestBody(BaseModel):
    path: constr(min_length=1, strip_whitespace=True)
    rules: list[str] = Field(min_length=1)


@app.post("/upload_code")
async def upload_code(body: RequestBody):
    result = process_request(body.path, body.rules)
    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
