import logging

logger = logging.getLogger(__name__)


class MemberValidator:

    @staticmethod
    def validate_id(member_id: str) -> None:
        if not member_id:
            msg = "Member ID cannot be empty."
            print(msg)
            raise ValueError(msg)

        if len(member_id) < 4:
            msg = "Member ID must have 4 characters."
            print(msg)
            raise ValueError(msg)

        if not member_id.startswith("M"):
            msg = "Member ID must start with 'M'."
            print(msg)
            raise ValueError(msg)

        if not member_id[1:].isdigit():
            msg = "Member ID must contain numbers after 'M'."
            print(msg)
            raise ValueError(msg)

    @staticmethod
    def validate_name(name: str) -> None:
        if not name:
            msg = "Name cannot be empty."
            print(msg)
            raise ValueError(msg)

        if not name.replace(" ", "").isalpha():
            msg = "Name must contain only alphabets."
            print(msg)
            raise ValueError(msg)

    @staticmethod
    def validate_phone(phone: str) -> None:
        if not phone:
            msg = "Phone number cannot be empty."
            print(msg)
            raise ValueError(msg)

        if not phone.isdigit():
            msg = "Phone number must contain only digits."
            print(msg)
            raise ValueError(msg)

        if len(phone) != 10:
            msg = "Phone number must contain exactly 10 digits."
            print(msg)
            raise ValueError(msg)

    @staticmethod
    def validate_age(age: str) -> None:
        if not age:
            msg = "Age cannot be empty."
            print(msg)
            raise ValueError(msg)

        if not age.isdigit():
            msg = "Age must contain only numbers."
            print(msg)
            raise ValueError(msg)

        age = int(age)

        if not 18 <= age <= 100:
            msg = "Age must be between 18 and 100."
            print(msg)
            raise ValueError(msg)
