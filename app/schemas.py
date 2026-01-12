from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    username: str
    password: str
    role: str


class EmployeeCreate(BaseModel):
    name: str
    email: str
    role: str
    responsibilities: str
    join_date: date


class EmployeeOut(BaseModel):
    id: int
    name: str
    email: str
    role: str
    responsibilities: str
    active: bool
