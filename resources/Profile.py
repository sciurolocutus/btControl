from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Profile(Resource):
    def get(self):
        #Return a list of the devices in a given profile, or metadata info about the current profile.
        pass
