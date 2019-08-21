import pytest
import uuid
from unittest import mock

from rentomatic.domain import room as r
from rentomatic.use_cases import room_list_use_case as uc


@pytest.fixture
def domain_rooms():
    room1 = r.Room(code=uuid.uuid4(), size=215, price=39, longitude=-0.09998975, latitude=51.753642921)
    room2 = r.Room(code=uuid.uuid4(), size=405, price=66, longitude=-3.09998975, latitude=-1.753642921)
    room3 = r.Room(code=uuid.uuid4(), size=56, price=60, longitude=-0.29898975, latitude=71.753642921)
    room4 = r.Room(code=uuid.uuid4(), size=93, price=48, longitude=-0.10008975, latitude=81.753642921)

    return [room1, room2, room3, room4]


def test_room_list_without_parameters(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms
    room_list_use_case = uc.RoomListUseCase(repo)

    result = room_list_use_case.execute()

    repo.list.assert_called_once_with()
    assert result == domain_rooms
