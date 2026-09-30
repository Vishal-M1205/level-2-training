from models.member import Member
from models.membership import Membership


class Display:

    @staticmethod
    def show_member(member: Member) -> None:
        print(f"""
{'=' * 45}
ID : {member.member_id}
Name : {member.name}
Mobile No : {member.phone}
Age : {member.age}
City : {member.city}
Membership ID : {member.membership_id}
{'=' * 45}
""")

    @staticmethod
    def show_all_members(members: list[Member]) -> None:
        if not members:
            print("No members found.")
            return

        for index, member in enumerate(members, start=1):
            print(f"\n{index}.")
            Display.show_member(member)

    @staticmethod
    def show_membership_plans(
        memberships: list[Membership],
    ) -> None:

        if not memberships:
            print("No membership plans available.")
            return

        for index, membership in enumerate(memberships, start=1):
            print(f"""
{'=' * 45}
{index}. {membership.plan_name.upper()} MEMBERSHIP
Duration : {membership.duration_months} months
Price : {membership.price}
Features : {membership.features}
{'=' * 45}
""")

    @staticmethod
    def show_membership_counts(
        membership_counts: dict[str, int],
        memberships: list[Membership],
    ) -> None:

        if not memberships:
            print("No membership plans available.")
            return

        for membership in memberships:
            count = membership_counts.get(
                membership.membership_id,
                0,
            )

            print(f"""
{'=' * 45}
Membership : {membership.plan_name}
Members : {count}
{'=' * 45}
""")

    @staticmethod
    def show_membership_revenue(
        revenue: dict[str, float],
        memberships: list[Membership],
    ) -> None:

        if not memberships:
            print("No membership plans available.")
            return

        for membership in memberships:
            amount = revenue.get(
                membership.membership_id,
                0,
            )

            print(f"""
{'=' * 40}
Plan name : {membership.plan_name}
Amount earned  : {amount}
{'=' * 40}
""")

        print(f"Total : {revenue.get('total', 0)}")

    @staticmethod
    def show_message(message: str) -> None:
        print(message)

    @staticmethod
    def show_error(error: Exception) -> None:
        print(f"Error: {error}")
