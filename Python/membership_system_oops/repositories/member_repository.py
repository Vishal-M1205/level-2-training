import logging
from pathlib import Path

from models.member import Member
from repositories.json_repository import JsonRepository

logger = logging.getLogger(__name__)

class MemberRepository:

    def __init__(self, filepath: Path, data_repository: JsonRepository):
        self.filepath = filepath
        self.data_repository = data_repository

    def get_all(self) -> list[Member]:
        data = self.data_repository.read(self.filepath)

        return [Member(**member) for member in data]

    def get_by_id(self, member_id: str) -> Member | None:
        members = self.get_all()

        return next(
            (member for member in members if member.member_id == member_id), None
        )

    def add(self, member: Member) -> None:
        members = self.get_all()

        members.append(member)

        self.save_all(members)

    def update(self, updated_member: Member) -> None:
        members = self.get_all()

        for index, member in enumerate(members):
            if member.member_id == updated_member.member_id:
                members[index] = updated_member
                self.save_all(members)
                return

        msg = f"Member with ID {updated_member.member_id} not found"
        logger.error(msg)
        raise ValueError(msg)

    def save_all(self, members: list[Member]) -> None:
        data = [member.model_dump() for member in members]

        self.data_repository.write(self.filepath, data)
