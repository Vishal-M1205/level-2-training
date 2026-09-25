from modules.json_services import read_json


def validateID(id: str, filepath, search=False) -> bool:
    if id.startswith("M") and len(id) == 4 and id[1:].isdigit():
        if not check_existing_user(id, filepath) or search:
            return True
        else:
            raise ValueError("ID already found")
    else:
        raise ValueError("Invalid ID : ID Starts with M then 3 digits")


def check_existing_user(id: str, filepath) -> bool:
    data = read_json(filepath)
    is_found = any(d["member_id"] == id for d in data)
    return is_found
