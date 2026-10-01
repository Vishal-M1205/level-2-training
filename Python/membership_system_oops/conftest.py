import pytest

from models.member import Member
from services.member_service import MemberService
from repositories.member_repository import MemberRepository
from repositories.json_repository import JsonRepository
from core.config import config

json_repository = JsonRepository()

member_repository = MemberRepository(
    filepath=config.members_file,
    json_repository=json_repository,
)


@pytest.fixture
def member_service():
    return MemberService(member_repository)


@pytest.fixture
def member_data():
    return Member(
        member_id="M001",
        name="Arun Kumar",
        phone="9876543210",
        age=25,
        city="Coimbatore",
        membership_id="MS001",
    )
