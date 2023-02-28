import json
from unittest import mock

from fastapi.testclient import TestClient


@mock.patch("src.application.rest.room.room_list_use_case")
def test_get(use_cas_mock, domain_rooms, room_dicts, client):

    use_cas_mock.return_value = domain_rooms

    response = client.get("/rooms/")

    assert response.status_code == 200


