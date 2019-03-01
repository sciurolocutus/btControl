from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from actions import ControlAction


class Control(Resource):
    putParser = reqparse.RequestParser()
    putParser.add_argument('action', type=str, required=True,
                           location='json',
                           help='START, STOP, or RECONNECT')

    @jwt_required
    def put(self):
        args = self.putParser.parse_args()
        action = ControlAction((args.action.lower()))
        if ControlAction.RECONNECT == action:
            # reconnect to all
            pass
        elif ControlAction.START == action:
            # start connecting to all audio sinks in the current profile.
            # (Don't, by default, connect to any)
            pass
        elif ControlAction.STOP == action:
            # disconnect from all audio sinks.
            pass

    def get(self):
        #Get current status, Started/not.
        pass

