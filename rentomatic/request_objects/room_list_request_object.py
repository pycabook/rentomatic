class RoomListRequestObject:
    @classmethod
    def from_dict(cls, adict):
        return cls()

    def __bool__(self):
        return True
