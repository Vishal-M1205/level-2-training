from core.config import config

from repositories.csv_repository import CSVRepository
from repositories.member_repository import MemberRepository
from repositories.membership_repository import MembershipRepository

from services.member_service import MemberService
from services.membership_service import MembershipService

from validators.member_validator import MemberValidator
from validators.membership_validator import MembershipValidator

from util.member_input import MemberInput
from util.membership_input import MembershipInput
from util.display import Display


def main() -> None:

    csv_repository = CSVRepository()

    member_repository = MemberRepository(
        filepath=config.members_file,
        data_repository=csv_repository,
    )

    membership_repository = MembershipRepository(
        filepath=config.memberships_file,
        data_repository=csv_repository,
    )

    member_service = MemberService(
        member_repository=member_repository,
    )

    membership_service = MembershipService(
        membership_repository=membership_repository,
        member_repository=member_repository,
    )

    member_validator = MemberValidator()

    member_input = MemberInput(
        validator=member_validator,
        config=config,
        membership_service=membership_service,
    )

    membership_validator = MembershipValidator()
    membership_input = MembershipInput(validator=membership_validator)

    while True:

        print("""

      MEMBERSHIP SYSTEM


1. Add Member
2. View Membership Plans
3. Search Member
4. View All Members
5. Update Member
6. View Members Per Membership
7. View Amount Earned
8. Top 3 Membership Plan
9. Membership Plans below 3000
10. Search Membership Plan
11. Exit
""")

        option = input("Enter your option: ").strip()

        try:

            if option == "1":

                member = member_input.get_new_member()

                member_service.add_member(member)

                Display.show_message("Member added successfully.")

            elif option == "2":

                memberships = membership_service.get_membership_plans()

                Display.show_membership_plans(memberships)

            elif option == "3":

                member_id = member_input.get_member_id()

                member = member_service.get_member(member_id)

                Display.show_member(member)

            elif option == "4":

                members = member_service.get_all_members()

                Display.show_all_members(members)

            elif option == "5":

                member_id = member_input.get_member_id(search=True)

                existing_member = member_service.get_member(member_id)

                updated_member = member_input.get_updated_member(existing_member)

                member_service.update_member(updated_member)

                Display.show_message("Member updated successfully.")

            elif option == "6":

                counts = membership_service.count_members_in_membership()

                memberships = membership_service.get_membership_plans()

                Display.show_membership_counts(
                    counts,
                    memberships,
                )

            elif option == "7":

                revenue = membership_service.calculate_amount_earned()

                memberships = membership_service.get_membership_plans()

                Display.show_membership_revenue(
                    revenue,
                    memberships,
                )

            elif option == "8":
                top_3 = membership_service.find_top_3_membership_plans()
                Display.show_membership_plans(top_3)

            elif option == "9":
                below_3000 = membership_service.membership_plans_below_3000()
                Display.show_membership_plans(below_3000)

            elif option == "10":
                membership_id = membership_input.get_membership_id()
                result = membership_service.get_membership(membership_id)
                Display.show_membership_plans([result])

            elif option == "11":
                csv_repository.read(config.members_file)

            else:
                print("Invalid option. Please try again.")

        except Exception as error:

            Display.show_error(error)


if __name__ == "__main__":
    main()
