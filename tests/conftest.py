from pprint import pprint
from typing import Generator

import pytest
import factory
from faker import Faker
from starlette.testclient import TestClient

from src.domain.entities.room import Room
from src.main import app

fake = Faker()
Faker.seed(0)


class RandomRoomFactory(factory.Factory):
    class Meta:
        model = Room

    code = fake.uuid4()
    size = fake.pyint(min_value=100, max_value=1000)
    price = fake.pyint(min_value=999990, max_value=9999999)
    longitude = fake.pyfloat(min_value=-180, max_value=180, right_digits=10)
    latitude = fake.pyfloat(min_value=-90, max_value=90, right_digits=10)


@pytest.fixture
def domain_rooms():
    return RandomRoomFactory.create_batch(10)


@pytest.fixture
def room_dicts(domain_rooms):
    result = [r.to_dict() for r in domain_rooms]
    pprint(result, indent=2)
    return result


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
