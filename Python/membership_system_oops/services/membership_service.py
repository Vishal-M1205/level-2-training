import logging
from models.membership import Membership
from repositories.membership_repository import MembershipRepository
from repositories.member_repository import MemberRepository
from exceptions.membership_exception import MembershipException
from typing import *
from functools import cache

logger = logging.getLogger(__name__)


class MembershipService:

    Membership_List: TypeAlias = list[Membership]

    def __init__(
        self,
        membership_repository: MembershipRepository,
        member_repository: MemberRepository,
    ):
        self.membership_repository = membership_repository
        self.member_repository = member_repository

    def get_membership_plans(self) -> Membership_List:
        return self.membership_repository.get_all()

    def get_membership(self, membership_id: str) -> Membership:
        membership = self.membership_repository.get_by_id(membership_id)

        if membership is None:
            msg = "Membership plan not found"
            logger.error(msg)
            raise MembershipException(msg)

        return membership

    def count_members_in_membership(self) -> dict[str, int]:
        members = self.member_repository.get_all()

        count_data: dict[str, int] = {}

        for member in members:
            membership_id = member.membership_id

            count_data[membership_id] = count_data.get(membership_id, 0) + 1

        return count_data

    def calculate_amount_earned(self) -> dict[str, float]:
        memberships = self.membership_repository.get_all()
        member_counts = self.count_members_in_membership()

        revenue: dict[str, float] = {}

        for membership in memberships:
            membership_id = membership.membership_id
            count = member_counts.get(membership_id, 0)

            revenue[membership_id] = membership.price * count

        revenue["total"] = sum(revenue.values())

        return revenue

    @cache
    def find_top_3_membership_plans(self) -> Membership_List:
        memberships = self.membership_repository.get_all()

        sorted_membership = sorted(memberships, key=lambda x: x.price, reverse=True)

        return sorted_membership[:3]

    @cache
    def membership_plans_below_3000(self) -> Membership_List:
        memberships = self.membership_repository.get_all()

        below_3000 = filter(lambda x: x.price <= 3000, memberships)

        return list(below_3000)
