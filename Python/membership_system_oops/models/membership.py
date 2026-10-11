from pydantic import BaseModel, Field


class Membership(BaseModel):
    membership_id: str = Field(description="ID start with MS and followed by 3 digits")
    plan_name: str
    duration_months: int
    price: float
    features: str | list[str]
    status: str
