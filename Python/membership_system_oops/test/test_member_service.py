def test_get_member(member_service, member_data):

    service = member_service

    result = service.member_repository.get_by_id("M001")

    assert result == member_data
