from pydantic import BaseModel, Field


class Member(BaseModel):
    member_id: str = Field(
        description="ID starts with M followed by 3 digits", examples=["M001"]
    )
    name: str
    phone: int
    age: int = Field(ge=18, le=100)
    city: str
    membership_id: str
