from pydantic import BaseModel
from typing import Optional


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    gender: str


class StudentCreate(BaseModel):
    name: str
    age: int
    gender: str


"""
Botht the models StudentCreate and StudentUpdate are same.
But for a clear meaning in API and seperate Responsibility, need to create these models
"""


class StudentUpdate(BaseModel):
    name: str
    age: int
    gender: str


class StudentPatch(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
