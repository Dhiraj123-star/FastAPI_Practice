from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI,Request

app= FastAPI()

templates = Jinja2Templates(directory='Templates')

@app.get("/hello/{name}",response_class=HTMLResponse)
async def hello(request:Request,name:str):
    return templates.TemplateResponse("hello.html",{"request":request,"name":name})