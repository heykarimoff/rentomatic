class RoomListRequestObject:
    def __bool__(self):
        return True

    @classmethod
    def from_dict(cls, adict):
        return cls()

