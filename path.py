
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message":"Hello FastAPI"}

@app.get("/hello/{name}/{age}")
async def hello(name:str,age:int):
    return {"name":f"Hi {name} and {age} years old."}

