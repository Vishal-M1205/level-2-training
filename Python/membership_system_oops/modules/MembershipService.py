from pathlib import Path
from modules.Config import config
from modules.JsonServices import JsonServices


class MembershipService:

    def __init__(self, filepath, data_service):
        self.filepath = filepath
        self.data_service = data_service

    def get_membership_details(self) -> list[dict]:
        data = self.data_service.read(self.filepath)
        return data

    def view_membership_plans(self) -> None:
        try:
            membership_data = self.data_service.read(self.filepath)
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
