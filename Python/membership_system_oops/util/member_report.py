from contextlib import redirect_stdout
from util.display import Display
import logging

logger = logging.getLogger(__name__)


class MemberReport:

    def __init__(self, member_service):
        self.member_service = member_service

    def generate_member_details_report(self):
        try:
            with open("member_details.txt", "w") as file:
                with redirect_stdout(file):
                    members = self.member_service.get_all_members()
                    Display.show_all_members(members)
            logger.info("Report generated successfully")
            Display.show_message("Report generated successfully")
        except Exception as e:
            logger.exception(e)
