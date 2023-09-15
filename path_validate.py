from fastapi import FastAPI,Path
app = FastAPI()

@app.get("/hello/{name}")
async def hello(name:str=Path(...,min_length=3,max_length=10)):
    return {"name":name}

@app.get("/hello/{name}/{age}")
async def hello(*,name:str=Path(...,min_length=3,max_length=10),age:int=Path(...,ge=1,le=100)):
    return {"name":name,"age":age}