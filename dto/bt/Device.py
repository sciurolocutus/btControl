class Device:
    def __init__(self, address, name, nickname):
        self.address = address
        self.name = name
        self.nickname = nickname

    def __json__(self):
        return {
            'address': self.address,
            'name': self.name,
            'nickname': self.nickname
        }

    to_json = __json__