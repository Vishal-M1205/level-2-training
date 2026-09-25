import json


def read_json(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"{filepath} : not found")
    except json.JSONDecodeError:
        print(f"{filepath} : wrong JSON Format")


def write_json(filepath, payload):
    try:
        data = read_json(filepath)
        data.append(payload)
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print(f"{filepath} : not found")
    except json.JSONDecodeError:
        print(f"{filepath} : wrong JSON Format")
    else:
        print(f"{filepath} updated successfully")
