from pathlib import Path


class MembershipService:

    def __init__(self, filepath: Path, data_service: object, member_service: object):
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

    def count_members_in_membership(self) -> dict:

        member_data = self.member_service.get_all_member_data()

        count_data = {}

        for member in member_data:
            if count_data.get(member["membership_id"], None):
                count_data[member["membership_id"]] += 1
            else:
                count_data[member["membership_id"]] = 1

        return count_data

    def view_no_members_in_membership(self):
        membership_data = self.get_membership_details()

        count_data = self.count_members_in_membership()

        for data in membership_data:
            data["count"] = count_data[data["membership_id"]]
            print("=" * 45)
            print(data["membership_id"])
            print(data["plan_name"])
            print(data["count"])
            print("=" * 45)

    def calc_amount_earned_in_membership(self):

        membership_data = self.get_membership_details()

        membership_price_data = {
            m["membership_id"]: m["price"] for m in membership_data
        }

        count_data = self.count_members_in_membership()

        amount_per_membership = {
            id: membership_price_data[id] * count_data[id] for id in count_data
        }

        total = sum(amount_per_membership.values())

        amount_per_membership.update({"total": total})

        return amount_per_membership

    def view_amount_earned_in_membership(self):

        amount_per_membership = self.calc_amount_earned_in_membership()

        membership_data = self.get_membership_details()

        for member in membership_data:
            print("=" * 40)
            print(f"Plan name : {member["plan_name"]}")
            print(f"Amount earned : {amount_per_membership[member["membership_id"]]}")

        print("=" * 40)
        print(f"Total : {amount_per_membership["total"]}")
