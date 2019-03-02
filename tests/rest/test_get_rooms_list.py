import json
from unittest import mock

from rentomatic.domain.room import Room
from rentomatic.response_objects import response_objects as res

room_dict = {
    'code': '3251a5bd-86be-428d-8ae9-6e51a8048c33',
    'size': 200,
    'price': 10,
    'longitude': -0.09998975,
    'latitude': 51.75436293
}

room = Room.from_dict(room_dict)

rooms = [room]


@mock.patch('rentomatic.use_cases.room_list_use_case.RoomListUseCase')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(rooms)

    http_response = client.get('/rooms')

    assert json.loads(http_response.data.decode('UTF-8')) == [room_dict]

    mock_use_case().execute.assert_called()
    args, kwargs = mock_use_case().execute.call_args
    assert args[0].filters == {}

    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'


@mock.patch('rentomatic.use_cases.room_list_use_case.RoomListUseCase')
def test_get_with_filters(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(rooms)

    http_response = client.get('/rooms?filter_price__gt=2&filter_price__lt=6')

    assert json.loads(http_response.data.decode('UTF-8')) == [room_dict]

    mock_use_case().execute.assert_called()
    args, kwargs = mock_use_case().execute.call_args
    assert args[0].filters == {'price__gt': '2', 'price__lt': '6'}

    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'
