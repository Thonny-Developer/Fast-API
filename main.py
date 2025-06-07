from fastapi import FastAPI
from pydantic import BaseModel
import db

app = FastAPI()

class RequestSettings(BaseModel):
    key: str
    
class NewKeyRequestSettings(BaseModel):
    email: str

@app.api_route("/", methods=["POST"])
async def api_request(data: RequestSettings):
    
    status = db.GetKey(data.key)

    if status:
        found, data = status
        if found:
            return data
        else:
            return {'Error': "Key Not Found"}
    else:
        return {"Error": "Error in retrieving data"}

@app.post("/create")
async def newKey_request(data: NewKeyRequestSettings):
    if "@" not in data.email:
        return {'Error': "Wrong Email"}
    
    result = db.NewKey(data.email)

    if result:
        Status, Email, Key = result
        return {"Key": Key}
    else:
        return {'Error': "Something Went Wrong"}

# uvicorn main:app --reload
