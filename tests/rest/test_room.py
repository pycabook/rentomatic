import json
from pprint import pprint
from unittest import mock


@mock.patch("src.application.rest.room.room_list_use_case")
def test_get(use_cas_mock, domain_rooms, room_dicts, client):

    use_cas_mock.return_value = domain_rooms

    response = client.get("/rooms/")
    assert json.loads(response.json()) == room_dicts
    use_cas_mock.assert_called()
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'

