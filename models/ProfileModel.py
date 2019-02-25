from db import db

"""
Define profile and profile_device.
These will define which profiles are active, and which devices they want to connect to.
"""



class ProfileModel(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.TinyInt(1))
    name = db.Column(db.String(80))