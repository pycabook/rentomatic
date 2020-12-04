import pytest

from rentomatic.requests.room_list import build_room_list_request


def test_build_room_list_request_without_parameters():
    request = build_room_list_request()

    assert request.filters is None
    assert bool(request) is True


def test_build_room_list_request_with_empty_filters():
    request = build_room_list_request({})

    assert request.filters == {}
    assert bool(request) is True


def test_build_room_list_request_with_invalid_filters_parameter():
    request = build_room_list_request(filters=5)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "filters"
    assert bool(request) is False


def test_build_room_list_request_with_incorrect_filter_keys():
    request = build_room_list_request(filters={"a": 1})

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "filters"
    assert bool(request) is False


@pytest.mark.parametrize(
    "key", ["code__eq", "price__eq", "price__lt", "price__gt"]
)
def test_build_room_list_request_accepted_filters(key):
    filters = {key: 1}

    request = build_room_list_request(filters=filters)

    assert request.filters == filters
    assert bool(request) is True


@pytest.mark.parametrize("key", ["code__lt", "code__gt"])
def test_build_room_list_request_rejected_filters(key):
    filters = {key: 1}

    request = build_room_list_request(filters=filters)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "filters"
    assert bool(request) is False
