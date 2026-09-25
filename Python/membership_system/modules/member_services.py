from modules.config import MEMBERS_FILE, MEMBERSHIPS_FILE, CITIES
from modules.validators import validateID
from modules.json_services import read_json, write_json
from modules.membership_services import get_membership_details


def get_member_id(search=False) -> str:
    while True:
        try:
            member_id = input("Enter Member ID : ")
            if validateID(member_id, MEMBERS_FILE, search):
                return member_id
        except ValueError as e:
            print(e)


def get_member_name() -> str:
    while True:
        try:
            member_name = input("Enter name : ")
            if member_name.replace(" ", "").isalpha():
                return member_name
            else:
                raise ValueError("Member name should have alphabet only")
        except ValueError as e:
            print(e)


def get_member_mobile_no() -> int:
    while True:
        try:
            member_mobile_no = input("Enter Mobile No : ")
            if len(member_mobile_no) == 10 and member_mobile_no.isdigit():
                return int(member_mobile_no)
            else:
                raise TypeError("Mob.No should only have 10 digits")
        except TypeError as e:
            print(e)


def get_member_age() -> int:
    while True:
        try:
            member_age = input("Enter Age : ")
            if member_age.isdigit():
                if int(member_age) >= 18 and int(member_age) <= 100:
                    return int(member_age)
                else:
                    raise ValueError("Age should be greater than 18 and less than 100")
            else:
                raise ValueError("Invalid Age")
        except Exception as e:
            print(e)


def get_member_city(city_data: list[str]) -> str:
    while True:
        try:
            for i, city in enumerate(city_data, start=1):
                print(f"{i}. {city}")
            option = input("Enter the option")
            if option.isdigit():
                if int(option) > 0 and int(option) <= len(city_data):
                    return city_data[int(option) - 1]
                else:
                    raise ValueError("Invalid option")
            else:
                raise TypeError("Option should be Integer")
        except Exception as e:
            print(e)


def get_membership_id() -> str:
    plan_details = get_membership_details(MEMBERSHIPS_FILE)
    while True:
        try:
            for i, plan in enumerate(plan_details, start=1):
                print(f"{i}.")
                print(f"""
                {'=' * 45}
                {i}. {plan['plan_name']} MEMBERSHIP
                Duration : {plan['duration_months']} months
                Price    : {plan['price']}
                Features : {plan['features']}
                {'=' * 45}
                """)

            option = input("Enter the option : ")
            if option.isdigit():
                if int(option) > 0 and int(option) <= len(plan_details):
                    return plan_details[int(option) - 1]["membership_id"]
                else:
                    raise ValueError("Invalid option")
            else:
                raise TypeError("Option should be Integer")
        except Exception as e:
            print(e)


def add_member() -> None:
    try:
        member_id = get_member_id()
        member_name = get_member_name()
        member_mobile_no = get_member_mobile_no()
        member_age = get_member_age()
        member_city = get_member_city(CITIES)
        membership_id = get_membership_id()

        data = {
            "member_id": member_id,
            "name": member_name,
            "phone": member_mobile_no,
            "age": member_age,
            "city": member_city,
            "membership_id": membership_id,
        }

        write_json(MEMBERS_FILE, data)
    except Exception as e:
        print(e)


def view_all_members() -> None:
    try:
        member_data = read_json(MEMBERS_FILE)
        for i, member in enumerate(member_data, start=1):
            print(f"{i}.")
            print(f"""
                {'=' * 45}
                ID : {member['member_id']} 
                Name : {member['name']} 
                Mobile No    : {member['phone']}
                Age : {member['age']}
                City : {member["city"]},
                Membership ID : {member["membership_id"]}
                {'=' * 45}
                """)

    except Exception as e:
        print(e)


def view_member(member: dict) -> None:
    print(f"""
            {'=' * 45}
            ID : {member['member_id']} 
            Name : {member['name']} 
            Mobile No    : {member['phone']}
            Age : {member['age']}
            City : {member["city"]},
            Membership ID : {member["membership_id"]}
            {'=' * 45}
                """)


def search_member() -> None:
    try:
        search_id = get_member_id(search=True)
        member_data = read_json(MEMBERS_FILE)

        result = [m for m in member_data if m["member_id"] == search_id]
        if result:
            view_member(result[0])
        else:
            raise Exception("No user found !")
    except Exception as e:
        print(e)


def update_member_detail():
    try:
        update_id = get_member_id(search=True)
        member_data = read_json(MEMBERS_FILE)
        for member in member_data:
            if member["member_id"] == update_id:
                member_name = get_member_name()
                member_mobile_no = get_member_mobile_no()
                member_age = get_member_age()
                member_city = get_member_city(CITIES)

                member["name"] = member_name
                member["phone"] = member_mobile_no
                member["age"] = member_age
                member["city"] = member_city
                write_json(MEMBERS_FILE, member_data, append=False)
                break
    except Exception as e:
        print(e)
