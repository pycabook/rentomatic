import json
import uuid

from rentomatic.serializers import room_json_serializer as ser
from rentomatic.domain import room as r


def test_serialize_domain_room():
    code = uuid.uuid4()

    room = r.Room(
        code=code,
        size=200,
        price=10,
        longitude=-0.09998975,
        latitude=51.75436293
    )

    expected_json = """
        {{
            "code": "{}",
            "size": 200,
            "price": 10,
            "longitude": -0.09998975,
            "latitude": 51.75436293
        }}
    """.format(code)

    json_room = json.dumps(room, cls=ser.RoomJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)
