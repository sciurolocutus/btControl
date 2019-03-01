from db import db


class DeviceModel(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80))  # human-given nickname
    name = db.Column(db.String(80))  # reported name
    addr = db.Column(db.String(80), nullable=False, unique=True)  # mac addr

    def __init__(self, address, name, nickname):
        self.nickname = nickname
        self.name = name
        self.addr = address

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, _name):
        return cls.query.filter_by(name=_name)

    @classmethod
    def find_by_nickname(cls, _nickname):
        return cls.query.filter_by(nickname=_nickname)

    @classmethod
    def find_by_addr(cls, _addr):
        return cls.query.filter_by(addr=_addr).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
