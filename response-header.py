from typing import List
from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class student(BaseModel):
    id :int
    name:str = Field(None,title='Name of the student',max_length=14)
    marks :List[int]=[]
    percent_marks :float


class percent(BaseModel):
    id :int 
    name:str = Field(None,title='Name of the student',max_length=12)
    percent_marks :float

@app.post("/marks",response_model=percent)
async def get_percent(s1:student):
    s1.percent_marks=sum(s1.marks)/len(s1.marks)
    return s1