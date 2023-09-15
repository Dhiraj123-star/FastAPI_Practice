from fastapi import FastAPI 
app = FastAPI()

@app.get("/hello")
async def hello(name:str,age:int):
    return {"hello":f"{name} and {age} years old."}