import logging
from models.member import Member
from repositories.member_repository import MemberRepository
from exceptions.member_exception import MemberException
from typing import Optional

logger = logging.getLogger(__name__)


class MemberService:

    def __init__(self, member_repository: MemberRepository):
        self.member_repository = member_repository

    def add_member(self, member: Member) -> None:
        existing_member: Optional[Member] = self.member_repository.get_by_id(
            member.member_id
        )

        if existing_member is not None:
            msg = "Member ID already exists"
            logger.error(msg)
            raise MemberException(msg)

        self.member_repository.add(member)

    def get_member(self, member_id: str) -> Member:
        member: Optional[Member] = self.member_repository.get_by_id(member_id)

        if member is None:
            msg = "No member found"
            logger.error(msg)
            raise MemberException(msg)

        return member

    def get_all_members(self) -> list[Member]:
        return self.member_repository.get_all()

    def update_member(self, member: Member) -> None:
        existing_member: Optional[Member] = self.member_repository.get_by_id(
            member.member_id
        )

        if existing_member is None:
            msg = "No member found"
            logger.error(msg)
            raise MemberException(msg)

        self.member_repository.update(member)
