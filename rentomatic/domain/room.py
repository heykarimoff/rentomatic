class Room:
    def __init__(self, code, size, price, longitude, latitude):
        self.code = code
        self.size = size
        self.price = price
        self.longitude = longitude
        self.latitude = latitude

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    @classmethod
    def from_dict(cls, adict):
        return cls(
            code=adict["code"],
            size=adict["size"],
            price=adict["price"],
            longitude=adict["longitude"],
            latitude=adict["latitude"],
        )

    def to_dict(self):
        return {
            "code": self.code,
            "size": self.size,
            "price": self.price,
            "longitude": self.longitude,
            "latitude": self.latitude,
        }
