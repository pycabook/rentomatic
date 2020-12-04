from rentomatic.requests.room_list import RoomListRequest


def test_build_room_list_request_without_parameters():
    request = RoomListRequest()

    assert bool(request) is True


def test_build_room_list_request_from_empty_dict():
    request = RoomListRequest.from_dict({})

    assert bool(request) is True
