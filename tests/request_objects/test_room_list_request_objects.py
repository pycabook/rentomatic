from rentomatic.request_objects import room_list_request_object as req


def test_build_room_list_request_object_without_parameters():
    request = req.RoomListRequestObject()

    assert bool(request) is True


def test_build_room_list_request_object_from_empty_dict():
    request = req.RoomListRequestObject.from_dict({})

    assert bool(request) is True
