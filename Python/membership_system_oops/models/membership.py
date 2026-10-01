from dataclasses import dataclass


@dataclass
class Membership:
    membership_id: str
    plan_name: str
    duration_months: int
    price: float
    features: list[str]
    status: str
