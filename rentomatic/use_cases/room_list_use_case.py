from rentomatic.response_objects import response_objects as res


class RoomListUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request_object):
        if not request_object:
            return res.ResponseFailure.build_from_invalid_request_object(request_object)

        try:
            rooms = self.repo.list(filters=request_object.filters)
        except Exception as exc:
            return res.ResponseFailure.build_system_error(f"{exc.__class__.__name__}: {exc}")

        return res.ResponseSuccess(rooms)
