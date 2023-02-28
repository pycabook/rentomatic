import json
import uuid

from src.domain.entities.room import Room
from src.serializers.room import RoomJsonEncoder


def test_room_model_init():
    code = uuid.uuid4()
    room = Room(
        code=code,
        size=100,
        price=10000,
        latitude=50.0,
        longitude=50.0
    )

    assert room.code == code
    assert room.size == 100
    assert room.price == 10000
    assert room.latitude == 50.0
    assert room.longitude == 50.0


def test_room_from_dict():
    code = uuid.uuid4()
    initial_data = {
        "code": code,
        "size": 100,
        "price": 10000,
        "latitude": 50.0,
        "longitude": 50.0
    }

    room = Room.from_dict(initial_data)

    assert room.code == code
    assert room.size == 100
    assert room.price == 10000
    assert room.latitude == 50.0
    assert room.longitude == 50.0


def test_room_to_dict():
    code = uuid.uuid4()
    initial_data = {
        "code": code,
        "size": 100,
        "price": 10000,
        "latitude": 50.0,
        "longitude": 50.0
    }
    room = Room.from_dict(initial_data)

    assert room.to_dict() == initial_data


def test_room_model_comparison():
    initial_data = {
        "code": uuid.uuid4(),
        "size": 100,
        "price": 10000,
        "latitude": 50.0,
        "longitude": 50.0
    }

    room_one = Room.from_dict(initial_data)
    room_two = Room.from_dict(initial_data)

    assert room_one == room_two


