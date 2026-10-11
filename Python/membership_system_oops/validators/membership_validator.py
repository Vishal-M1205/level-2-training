import logging
from exceptions.membership_exception import MembershipException

logger = logging.getLogger(__name__)

class MembershipValidator:

    @staticmethod
    def validate_membership_id(membership_id: str):
        if (
            membership_id.startswith("MS")
            and len(membership_id) == 5
            and membership_id[2:].isdigit()
        ):
            return membership_id
        else:
            msg = "Invalid format of ID (eg:MS001)"
            logger.error(msg)
            raise MembershipException(msg)
