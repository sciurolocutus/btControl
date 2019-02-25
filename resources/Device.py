from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from bluetooth import *


class Device(Resource):
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

class DeviceList(Resource):
    def get(self):
        #Get list of registered devices.

class DeviceScan(Resource):
    def get(self):
        """
        GET /devices/scan
        Pull a list of visible BT devices using hcitool scan or the like.
        Note: actually use an adapter/client, to abstract that away.
        :return:
        """