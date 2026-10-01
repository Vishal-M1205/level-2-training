from models.member import Member
from repositories.member_repository import MemberRepository
from exceptions.member_exception import MemberException


class MemberService:

    def __init__(self, member_repository: MemberRepository):
        self.member_repository = member_repository

    def add_member(self, member: Member) -> None:
        existing_member = self.member_repository.get_by_id(member.member_id)

        if existing_member is not None:
            raise MemberException("Member ID already exists")

        self.member_repository.add(member)

    def get_member(self, member_id: str) -> Member:
        member = self.member_repository.get_by_id(member_id)

        if member is None:
            raise MemberException("No member found")

        return member

    def get_all_members(self) -> list[Member]:
        return self.member_repository.get_all()

    def update_member(self, member: Member) -> None:
        existing_member = self.member_repository.get_by_id(member.member_id)

        if existing_member is None:
            raise MemberException("No member found")

        self.member_repository.update(member)
