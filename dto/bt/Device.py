from flask_restful import fields, marshal_with

resource_fields = {
    'address': fields.String,
    'name': fields.String,
    'nickname': fields.String
}


@marshal_with(resource_fields)
class Device:
    def __init__(self, address, name, nickname):
        self.address = address
        self.name = name
        self.nickname = nickname

    @classmethod
    def from_device_model(cls, device_model):
        return Device(device_model.addr, device_model.name, device_model.nickname)

    def __json__(self):
        return {
            'address': self.address,
            'name': self.name,
            'nickname': self.nickname
        }

    to_json = __json__
