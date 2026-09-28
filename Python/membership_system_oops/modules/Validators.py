class Validator:

    def __init__(self, filepath, data_service):
        self.filepath = filepath
        self.data_service = data_service

    def validateID(self, id: str, search=False) -> bool:
        if id.startswith("M") and len(id) == 4 and id[1:].isdigit():
            if not self.check_existing_user(id) or search:
                return True
            else:
                raise ValueError("ID already found")
        else:
            raise ValueError("Invalid ID : ID Starts with M then 3 digits")

    def check_existing_user(
        self,
        id: str,
    ) -> bool:
        data = self.data_service.read(self.filepath)
        is_found = any(d["member_id"] == id for d in data)
        return is_found
