from pathlib import Path

from models.membership import Membership
from repositories.json_repository import JsonRepository


class MembershipRepository:

    def __init__(
        self,
        filepath: Path,
        json_repository: JsonRepository,
    ):
        self.filepath = filepath
        self.json_repository = json_repository

    def get_all(self) -> list[Membership]:
        data = self.json_repository.read(self.filepath)

        return [Membership(**membership) for membership in data]

    def get_by_id(
        self,
        membership_id: str,
    ) -> Membership | None:

        memberships = self.get_all()

        #! generator expression
        return next(
            (
                membership
                for membership in memberships
                if membership.membership_id == membership_id
            ),
            None,
        )
