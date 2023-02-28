import json


class RoomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            to_serialize = {
                "code": str(obj.code),
                "size": obj.size,
                "price": obj.price,
                "latitude": obj.latitude,
                "longitude": obj.longitude
            }
            return to_serialize
        except AttributeError:
            return super().default(obj)

