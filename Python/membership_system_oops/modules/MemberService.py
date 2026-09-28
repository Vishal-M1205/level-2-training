from modules.Config import config
from modules.Validators import Validator
from modules.JsonServices import JsonServices
from modules.MembershipService import MembershipService
from dataclasses import dataclass
from pathlib import Path


@dataclass
class MemberService:
    filepath: Path
    validator_service: object
    config_data: object
    membership_service: object
    data_service: object

    member_id: int = None
    member_name: str = None
    member_mobile_no: int = None
    member_age: int = None

    def get_member_id(self, search=False) -> str:
        while True:
            try:
                self.member_id = input("Enter Member ID : ")
                if self.validator_service.validateID(self.member_id, search):
                    return self.member_id
            except ValueError as e:
                print(e)

    def get_member_name(self) -> str:
        while True:
            try:
                self.member_name = input("Enter name : ")
                if self.member_name.replace(" ", "").isalpha():
                    return self.member_name
                else:
                    raise ValueError("Member name should have alphabet only")
            except ValueError as e:
                print(e)

    def get_member_mobile_no(self) -> int:
        while True:
            try:
                self.member_mobile_no = input("Enter Mobile No : ")
                if len(self.member_mobile_no) == 10 and self.member_mobile_no.isdigit():
                    return int(self.member_mobile_no)
                else:
                    raise TypeError("Mob.No should only have 10 digits")
            except TypeError as e:
                print(e)

    def get_member_age(self) -> int:
        while True:
            try:
                self.member_age = input("Enter Age : ")
                if self.member_age.isdigit():
                    if int(self.member_age) >= 18 and int(self.member_age) <= 100:
                        return int(self.member_age)
                    else:
                        raise ValueError(
                            "Age should be greater than 18 and less than 100"
                        )
                else:
                    raise ValueError("Invalid Age")
            except Exception as e:
                print(e)

    def get_member_city(self) -> str:
        while True:
            try:
                for i, city in enumerate(self.config_data.cities, start=1):
                    print(f"{i}. {city}")
                option = input("Enter the option")
                if option.isdigit():
                    if int(option) > 0 and int(option) <= len(self.config_data.cities):
                        return self.config_data.cities[int(option) - 1]
                    else:
                        raise ValueError("Invalid option")
                else:
                    raise TypeError("Option should be Integer")
            except Exception as e:
                print(e)

    def get_membership_id(self) -> str:
        plan_details = self.membership_service.get_membership_details()
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

    def add_member(self) -> None:
        try:
            member_id = self.get_member_id()
            member_name = self.get_member_name()
            member_mobile_no = self.get_member_mobile_no()
            member_age = self.get_member_age()
            member_city = self.get_member_city()
            membership_id = self.get_membership_id()

            data = {
                "member_id": member_id,
                "name": member_name,
                "phone": member_mobile_no,
                "age": member_age,
                "city": member_city,
                "membership_id": membership_id,
            }

            self.data_service.write(self.filepath, data)
        except Exception as e:
            print(e)

    def view_all_members(self) -> None:
        try:
            member_data = self.data_service.read(self.filepath)
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

    def view_member(self, member: dict) -> None:
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

    def search_member(self) -> None:
        try:
            search_id = self.get_member_id(search=True)
            member_data = self.data_service.read(self.filepath)

            result = [m for m in member_data if m["member_id"] == search_id]
            if result:
                self.view_member(result[0])
            else:
                raise Exception("No user found !")
        except Exception as e:
            print(e)

    def update_member_detail(self):
        try:
            update_id = self.get_member_id(search=True)
            member_data = self.data_service.read(self.filepath)
            for member in member_data:
                if member["member_id"] == update_id:
                    member_name = self.get_member_name()
                    member_mobile_no = self.get_member_mobile_no()
                    member_age = self.get_member_age()
                    member_city = self.get_member_city()

                    member["name"] = member_name
                    member["phone"] = member_mobile_no
                    member["age"] = member_age
                    member["city"] = member_city
                    self.data_service.write(self.filepath, member_data, append=False)
                    break
        except Exception as e:
            print(e)
