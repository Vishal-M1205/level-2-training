from modules.Config import config
from modules.MemberService import MemberService
from modules.MembershipService import MembershipService
from modules.Validators import Validator
from modules.JsonServices import JsonServices

member_data_path = config.members_file
membership_data_path = config.memberships_file

data_service = JsonServices()

member_valditor_service = Validator(
    filepath=member_data_path, data_service=data_service
)

member_service = MemberService(
    filepath=member_data_path,
    validator_service=member_valditor_service,
    config_data=config,
    data_service=data_service,
)

membership_service = MembershipService(
    filepath=membership_data_path,
    data_service=data_service,
    member_service=member_service,
)

member_service.membership_service = membership_service


def main():
    try:
        while True:
            print(f"""
{config.app}

1. Add Membership
2. View Membership Plans
3. Search Member
4. View All Member
5. Update Member
6. Count of Members in Each Membership
7. View Amount earned in memberships
8. Exit

""")
            option = int(input("Enter a option : "))
            match option:
                case 1:
                    member_service.add_member()
                case 2:
                    membership_service.view_membership_plans()
                case 3:
                    member_service.search_member()
                case 4:
                    member_service.view_all_members()
                case 5:
                    member_service.update_member_detail()
                case 6:
                    membership_service.view_no_members_in_membership()
                case 7:
                    membership_service.view_amount_earned_in_membership()
                case 8:
                    break
                case _:
                    print("Invalid option!")

    except Exception as e:
        print(e)


main()
