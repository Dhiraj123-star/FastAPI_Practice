from fastapi import FastAPI,Body
from typing import List
from pydantic import BaseModel,Field

app = FastAPI()

class Student(BaseModel):
    id :int
    name:str =Field(None,title='name of the student',max_length=20)
    subjects :List[str]=[]

@app.post("/students/")
async def student_data(s1:Student):
    return s1


@app.post("/student/")
async def student_detail(name:str=Body(...),age:int=Body(...)):
    return {"name":name,"age":age}

@app.post("/student/{college}")
async def student_data(college:str,age:int,student:Student):
    retval = {"college":college,"age":age,**student.model_dump()}

    return retval