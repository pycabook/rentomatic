import sqlalchemy
import sqlalchemy_utils

from rentomatic.repository.postgres_objects import Base, Room

setup = {
    'dbname': 'rentomaticdb',
    'user': 'postgres',
    'password': 'rentomaticdb',
    'host': 'localhost'
}

conn_str = "postgresql+psycopg2://{}:{}@{}/{}".format(
    setup['user'],
    setup['password'],
    setup['host'],
    setup['dbname']
)

engine = sqlalchemy.create_engine(conn_str)
sqlalchemy_utils.create_database(engine.url)
conn = engine.connect()

Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
session = DBSession()


data = [
    {
        'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
        'size': 215,
        'price': 39,
        'longitude': -0.09998975,
        'latitude': 51.75436293,
    },
    {
        'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
        'size': 405,
        'price': 66,
        'longitude': 0.18228006,
        'latitude': 51.74640997,
    },
    {
        'code': '913694c6-435a-4366-ba0d-da5334a611b2',
        'size': 56,
        'price': 60,
        'longitude': 0.27891577,
        'latitude': 51.45994069,
    },
    {
        'code': 'eed76e77-55c1-41ce-985d-ca49bf6c0585',
        'size': 93,
        'price': 48,
        'longitude': 0.33894476,
        'latitude': 51.39916678,
    }
]

for r in data:
    new_room = Room(
        code=r['code'],
        size=r['size'],
        price=r['price'],
        longitude=r['longitude'],
        latitude=r['latitude']
    )
    session.add(new_room)
    session.commit()
