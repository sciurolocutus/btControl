from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from actions.DeviceAction import DeviceAction
from models.DeviceModel import DeviceModel


class Device(Resource):
    putParser = reqparse.RequestParser()
    putParser.add_argument('action', type=str, required=True,
                           location='json',
                           help='START, STOP, or RECONNECT')

    @jwt_required
    def put(self):
        args = self.putParser.parse_args()
        action = DeviceAction((args.action.lower()))
        if DeviceAction.RECONNECT == action:
            # reconnect to all
            pass
        elif DeviceAction.START == action:
            # start connecting to all audio sinks in the current profile.
            # (Don't, by default, connect to any)
            pass
        elif DeviceAction.STOP == action:
            # disconnect from all audio sinks.
            pass

    def get(self):
        # Get current status, Started/not.
        pass


class DeviceList(Resource):
    def get(self):
        return DeviceModel.find_all()
        # Get list of registered devices.


class DeviceScan(Resource):
    def get(self):
        """
        GET /devices/scan
        Pull a list of visible BT devices using hcitool scan or the like.
        Note: actually use an adapter/client, to abstract that away.
        :return:
        """
