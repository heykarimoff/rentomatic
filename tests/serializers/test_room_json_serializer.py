import json
import uuid

from rentomatic.serializers import room_json_serializer as ser
from rentomatic.domain import room as r


def test_serialize_domain_room():
    code = uuid.uuid4()

    room = r.Room(code=code, size=200, price=10, longitude=-0.9998811, latitude=42.00118811)

    expected_json = (
        f"""{{"code": "{code}", "size": "200", "price": "10", "longitude": "-0.9998811", "latitude": "42.00118811"}}"""
    )

    assert expected_json == json.dumps(room, cls=ser.RoomJsonEncoder)
