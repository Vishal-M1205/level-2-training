from dataclasses import dataclass


@dataclass
class Member:
    member_id: str
    name: str
    phone: int
    age: int
    city: str
    membership_id: str
