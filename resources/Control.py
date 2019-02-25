from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Control(Resource):
    @jwt_required
    def put(self, Action):
        #PUT: reconnect - reconnect to all
        #PUT: start - start connecting to all audio sinks in the current profile.
        # Don't, by default,
        #PUT: stop - disconnect from all audio sinks.
        pass

    def get(self):
        #Get current status, Started/not.
        pass

