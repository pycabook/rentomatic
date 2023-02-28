import json
import uuid

from src.domain.entities.room import Room
from src.serializers.room import RoomJsonEncoder


def test_serialize_domain_room():

    code = uuid.uuid4()
    room = Room(
        code=code,
        size=100,
        price=10000,
        latitude=50.0,
        longitude=50.0
    )

    expected_json = f"""
        {{
        "code": "{code}",
        "size": 100,
        "price": 10000,
        "latitude": 50.0,
        "longitude": 50.0
        }}
    """

    json_room = json.dumps(room, cls=RoomJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)
