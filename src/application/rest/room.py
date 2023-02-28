import json

from fastapi import APIRouter, Depends, FastAPI

from src.application.config import Settings, get_settings
from src.domain import entities
from src.repositories.memrepo import MemRepo
from src.serializers.room import RoomJsonEncoder
from src.use_cases.room_list import room_list_use_case


rooms = [
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 215,
        "price": 39,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    },
    {
        "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
        "size": 405,
        "price": 66,
        "longitude": 0.18228006,
        "latitude": 51.74640997,
    },
    {
        "code": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
        "size": 93,
        "price": 48,
        "longitude": 0.33894476,
        "latitude": 51.39916678,
    },
]

room_router = APIRouter(
    prefix="/rooms", tags=["rooms"]
)


@room_router.get("/")
async def info(settings: Settings = Depends(get_settings)):
    repo = MemRepo(rooms)
    print(repo)
    result = room_list_use_case(repo)
    print(result)

    return json.dumps(result, cls=RoomJsonEncoder)

