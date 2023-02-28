from src.domain.entities.room import Room
from src.repositories.memrepo import MemRepo


def test_repository_list_without_parameters(room_dicts):

    repo = MemRepo(room_dicts)
    rooms = [Room.from_dict(d) for d in room_dicts]

    assert repo.list() == rooms
