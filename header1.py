from typing import Optional
from fastapi import  FastAPI,Header
from fastapi.responses import JSONResponse
app = FastAPI()

@app.get("/headers/")
async def read_header(accept_language:Optional[str]=Header(None)):
    return {'Accept-Language':accept_language}

@app.get("/rspheader/")
def set_rsp_headers():
    content = {"message":"Hello FastAPI"}
    headers = {"X-Web-Framework":"FASTAPI","Content-Language":"en-US"}
    return JSONResponse(content=content,headers=headers)