from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int

class Student(StudentCreate):
    id : int
