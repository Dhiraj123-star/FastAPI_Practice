from fastapi import FastAPI,Cookie
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/cookie/")
def create_cookie():
    content = {"message":"cookie is set"}
    response = JSONResponse(content=content)
    response.set_cookie(key="username",value="Dhiraj")
    return response

@app.get("/readcookie/")
async def read_cookie(username:str=Cookie(None)):
    return {"username":username}