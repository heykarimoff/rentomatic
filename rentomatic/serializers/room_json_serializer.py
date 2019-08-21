import json


class RoomJsonEncoder(json.JSONEncoder):
    def default(self, room):
        try:
            to_serialize = {
                'code': str(room.code),
                'size': str(room.size),
                'price': str(room.price),
                'longitude': str(room.longitude),
                'latitude': str(room.latitude),
            }
        except AttributeError:
            return super().default(room)