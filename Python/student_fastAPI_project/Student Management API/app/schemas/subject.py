from pydantic import BaseModel, Field
from typing import Optional


class SubjectResponse(BaseModel):
    id: int = Field(description="ID is auto generated in postgres")
    name: str = Field(min_length=3)


class SubjectCreate(BaseModel):
    name: str = Field(min_length=3)


class SubjectUpdate(BaseModel):
    name: str = Field(min_length=3)


class SubjectPatch(BaseModel):
    name: Optional[str] = Field(min_length=3, default=None)
