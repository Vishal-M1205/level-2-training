class MemberValidator:

    @staticmethod
    def validate_id(member_id: str) -> None:
        if not member_id:
            raise ValueError("Member ID cannot be empty.")

        if not member_id.startswith("M"):
            raise ValueError("Member ID must start with 'M'.")

        if not member_id[1:].isdigit():
            raise ValueError("Member ID must contain numbers after 'M'.")

    @staticmethod
    def validate_name(name: str) -> None:
        if not name:
            raise ValueError("Name cannot be empty.")

        if not name.replace(" ", "").isalpha():
            raise ValueError("Name must contain only alphabets.")

    @staticmethod
    def validate_phone(phone: str) -> None:
        if not phone:
            raise ValueError("Phone number cannot be empty.")

        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits.")

        if len(phone) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")

    @staticmethod
    def validate_age(age: str) -> None:
        if not age:
            raise ValueError("Age cannot be empty.")

        if not age.isdigit():
            raise ValueError("Age must contain only numbers.")

        age = int(age)

        if not 18 <= age <= 100:
            raise ValueError("Age must be between 18 and 100.")
