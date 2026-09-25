from pathlib import Path
from modules.config import MEMBERSHIPS_FILE
from modules.json_services import read_json


def get_membership_details(filepath: Path) -> list[dict]:
    data = read_json(filepath)
    return data


def view_membership_plans() -> None:
    try:
        membership_data = read_json(MEMBERSHIPS_FILE)
        for i, plan in enumerate(membership_data, start=1):
            print(f"{i}.")
            print(f"""
                {'=' * 45}
                {i}. {plan['plan_name']} MEMBERSHIP
                Duration : {plan['duration_months']} months
                Price    : {plan['price']}
                Features : {plan['features']}
                {'=' * 45}
                """)

    except Exception as e:
        print(e)
