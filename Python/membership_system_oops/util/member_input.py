import logging
from models.member import Member

logger = logging.getLogger(__name__)

class MemberInput:

    def __init__(self, validator, cities, membership_service):
        self.validator = validator
        self.cities = cities
        self.membership_service = membership_service

    def get_member_id(self) -> str:
        while True:
            member_id = input("Enter Member ID: ").strip()
            try:
                self.validator.validate_id(member_id)
                return member_id
            except ValueError as e:
                logger.exception(e)

    def get_member_name(self) -> str:
        while True:
            name = input("Enter name: ").strip()
            try:
                self.validator.validate_name(name)
                return name
            except ValueError as e:
                logger.exception(e)

    def get_member_mobile_no(self) -> str:
        while True:
            phone = input("Enter Mobile No: ").strip()
            try:
                self.validator.validate_phone(phone)
                return phone
            except ValueError as e:
                logger.exception(e)

    def get_member_age(self) -> int:
        while True:
            age = input("Enter Age: ").strip()
            try:
                self.validator.validate_age(age)
                return int(age)
            except ValueError as e:
                logger.exception(e)

    def get_member_city(self) -> str:
        cities = self.cities

        while True:
            for i, city in enumerate(cities, start=1):
                print(f"{i}. {city}")

            option = input("Enter the option: ").strip()

            if option.isdigit() and 1 <= int(option) <= len(cities):
                return cities[int(option) - 1]

            print("Invalid option. Please select a valid city.")

    def get_membership_id(self) -> str:
        plans = self.membership_service.get_membership_plans()

        if not plans:
            msg = "No membership plans available"
            logger.error(msg)
            raise ValueError(msg)

        while True:
            for i, plan in enumerate(plans, start=1):
                print(f"""
{'=' * 45}
{i}. {plan.plan_name} MEMBERSHIP
Duration : {plan.duration_months} months
Price    : {plan.price}
Features : {plan.features}
{'=' * 45}
""")

            option = input("Enter the option: ").strip()

            if option.isdigit() and 1 <= int(option) <= len(plans):
                return plans[int(option) - 1].membership_id

            print("Invalid option. Please select a valid plan.")

    def get_new_member(self) -> Member:
        return Member(
            member_id=self.get_member_id(),
            name=self.get_member_name(),
            phone=self.get_member_mobile_no(),
            age=self.get_member_age(),
            city=self.get_member_city(),
            membership_id=self.get_membership_id(),
        )

    def get_updated_member(self, existing: Member) -> Member:
        print("Enter the updated member details:")

        return Member(
            member_id=existing.member_id,
            name=self.get_member_name(),
            phone=self.get_member_mobile_no(),
            age=self.get_member_age(),
            city=self.get_member_city(),
            membership_id=existing.membership_id,
        )
