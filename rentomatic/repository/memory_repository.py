from rentomatic.domain import room as r


class MemoryRepo:
    def __init__(self, data):
        self.data = data

    def list(self):
        return [r.Room.from_dict(i) for i in self.data]
