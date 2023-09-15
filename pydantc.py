from typing import List
from pydantic import BaseModel

class Student(BaseModel):
    id:int
    name:str
    subjects :List[str]=[]



# data = {
#     'id':1,
#     'name':'Rahul',
#     'subjects':['Computer Applications','Data structure','Programming']
# }

# s1 = Student(**data)

# print(s1.model_dump())


data2 = {
    'id':[12,4],
    'name':'Rohit',
    'subjects':['Computer science','Maths']
}

s2 = Student(**data2)

print(s2)