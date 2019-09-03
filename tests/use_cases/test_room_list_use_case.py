import pytest
import uuid
from unittest import mock

from rentomatic.domain import room as r
from rentomatic.use_cases import room_list_use_case as uc
from rentomatic.request_objects import room_list_request_object as req
from rentomatic.response_objects import response_objects as res


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
    request = req.RoomListRequestObject()

    response = room_list_use_case.execute(request)

    assert bool(response) is True
    repo.list.assert_called_once_with(filters=None)
    assert response.value == domain_rooms


def test_room_list_with_filters(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms
    room_list_use_case = uc.RoomListUseCase(repo)
    query_filters = {"code__eq": 5}
    request_object = req.RoomListRequestObject.from_dict({"filters": query_filters})

    response_object = room_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_once_with(filters=query_filters)
    assert response_object.value == domain_rooms


def test_room_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception("Database has fallen asleep")
    room_list_use_case = uc.RoomListUseCase(repo)
    request_object = req.RoomListRequestObject.from_dict({})

    response_object = room_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        "type": res.ResponseFailure.SYSTEM_ERROR,
        "message": "Exception: Database has fallen asleep",
    }


# def test_room_list_handles_bad_request():
#     repo = mock.Mock()
#     room_list_use_case = uc.RoomListUseCase(repo)
#     request_object = req.RoomListRequestObject.from_dict({"filters": 5})

#     response_object = room_list_use_case.execute(request_object)

#     assert bool(request_object) is False
#     assert response_object.value == {
#         "type": res.ResponseFailure.PARAMETERS_ERROR,
#         "message": "filters: Is not iterable",
#     }
