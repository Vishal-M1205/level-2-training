from pathlib import Path
from modules.Config import config
from modules.JsonServices import JsonServices


class MembershipService:

    def __init__(self, filepath, data_service, member_service):
        self.filepath = filepath
        self.data_service = data_service
        self.member_service = member_service

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

    def count_members_in_membership(self):

        member_data = self.member_service.get_all_member_data()

        membership_data = self.get_membership_details()

        count_data = {}

        for member in member_data:
            if count_data.get(member["membership_id"], None):
                count_data[member["membership_id"]] += 1
            else:
                count_data[member["membership_id"]] = 1

        for data in membership_data:
            data["count"] = count_data[data["membership_id"]]
            print("=" * 45)
            print(data["membership_id"])
            print(data["plan_name"])
            print(data["count"])
            print("=" * 45)
