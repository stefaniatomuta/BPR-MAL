from fastapi import FastAPI
from pydantic import BaseModel, constr, Field
from Service.FileLoadService import process_data_from_folder

app = FastAPI()


class RequestBody(BaseModel):
    path: constr(min_length=1, strip_whitespace=True)
    rules: list[str] = Field(min_length=1)


@app.post("/upload_code")
async def upload_code(body: RequestBody):
    process_data_from_folder(body.path, body.rules)
    return
