#!/usr/bin/env python

from rentomatic.repository import memrepo as mr
from rentomatic.use_cases import room_list_use_case as uc

room1 = {
    'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
    'size': 215,
    'price': 39,
    'longitude': -0.09998975,
    'latitude': 51.75436293,
}

room2 = {
    'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
    'size': 405,
    'price': 66,
    'longitude': 0.18228006,
    'latitude': 51.74640997,
}

room3 = {
    'code': '913694c6-435a-4366-ba0d-da5334a611b2',
    'size': 56,
    'price': 60,
    'longitude': 0.27891577,
    'latitude': 51.45994069,
}

repo = mr.MemRepo([room1, room2, room3])
use_case = uc.RoomListUseCase(repo)

result = use_case.execute()

print([room.to_dict() for room in result])
