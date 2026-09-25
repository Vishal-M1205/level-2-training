from modules.config import APP
from modules.member_services import *
from modules.membership_services import *


def main():
    try:
        while True:
            print(f"""
{APP}

1. Add Membership
2. View Membership Plans
3. Search Member
4. View All Member
5. Exit

""")
            option = int(input("Enter a option : "))
            match option:
                case 1:
                    add_member()
                case 2:
                    view_membership_plans()
                case 3:
                    search_member()
                case 4:
                    view_all_members()
                case 5:
                    break
                case _:
                    print("Invalid option!")

    except Exception as e:
        print(e)


main()
