from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class StudentName(BaseModel):
    name: str = 'ghost'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=11, default=0.0, description="this is cgpa") 

new_student = {'name': "arpit", 'age': 101, 'email': "abc@mail.com"}

student = StudentName(**new_student);

print(type(student))
print(student)

student_json = student.model_dump_json()

print(student_json)