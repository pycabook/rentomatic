from pprint import pprint

from src.domain.entities.room import Room
from src.repositories.memrepo import MemRepo
from src.use_cases.room_list import room_list_use_case


def main():
    room_dicts = [
        {
            'code': 'e3e70682-c209-4cac-a29f-6fbed82c07cd',
            'latitude': -12.8451636615,
            'longitude': -47.6382010853,
            'price': 1679205,
            'size': 530
        },
        {
            'code': 'e3e70682-c209-4cac-a29f-6fbed82c07cd',
            'latitude': -12.8451636615,
            'longitude': -47.6382010853,
            'price': 1679205,
            'size': 530
        },
        {
            'code': 'e3e70682-c209-4cac-a29f-6fbed82c07cd',
            'latitude': -12.8451636615,
            'longitude': -47.6382010853,
            'price': 1679205,
            'size': 530
        },
        {
            'code': 'e3e70682-c209-4cac-a29f-6fbed82c07cd',
            'latitude': -12.8451636615,
            'longitude': -47.6382010853,
            'price': 1679205,
            'size': 530
        },
        {
            'code': 'e3e70682-c209-4cac-a29f-6fbed82c07cd',
            'latitude': -12.8451636615,
            'longitude': -47.6382010853,
            'price': 1679205,
            'size': 530
        },
        {
            'code': 'e3e70682-c209-4cac-a29f-6fbed82c07cd',
            'latitude': -12.8451636615,
            'longitude': -47.6382010853,
            'price': 1679205,
            'size': 530
        },
        {
            'code': 'e3e70682-c209-4cac-a29f-6fbed82c07cd',
            'latitude': -12.8451636615,
            'longitude': -47.6382010853,
            'price': 1679205,
            'size': 530
        },
        {
            'code': 'e3e70682-c209-4cac-a29f-6fbed82c07cd',
            'latitude': -12.8451636615,
            'longitude': -47.6382010853,
            'price': 1679205,
            'size': 530
        },
        {
            'code': 'e3e70682-c209-4cac-a29f-6fbed82c07cd',
            'latitude': -12.8451636615,
            'longitude': -47.6382010853,
            'price': 1679205,
            'size': 530
        },
        {
            'code': 'e3e70682-c209-4cac-a29f-6fbed82c07cd',
            'latitude': -12.8451636615,
            'longitude': -47.6382010853,
            'price': 1679205,
            'size': 530
        }
    ]

    repo = MemRepo(room_dicts)
    result = room_list_use_case(repo)
    pprint(result, indent=2)


if __name__ == '__main__':
    main()
