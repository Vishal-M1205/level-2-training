import pytest
from validators.member_validator import MemberValidator


@pytest.mark.parametrize(
    "mobile_number",
    [
        pytest.param("", id="empty_phone"),
        pytest.param("98765", id="less_than_10_digits"),
        pytest.param("98765432101", id="more_than_10_digits"),
        pytest.param("98765abcde", id="contains_letters"),
    ],
)
def test_invalid_mobile_number(mobile_number):
    with pytest.raises(ValueError):
        assert MemberValidator.validate_phone(mobile_number)
