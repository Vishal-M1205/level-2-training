import logging

logger = logging.getLogger(__name__)

class MembershipInput:

    def __init__(self, validator):
        self.validator = validator

    def get_membership_id(self):
        while True:
            membership_id = input("Enter Membership ID : ")
            try:
                if self.validator.validate_membership_id(membership_id=membership_id):
                    return membership_id
            except Exception as e:
                logger.exception(e)
