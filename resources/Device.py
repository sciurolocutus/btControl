from flask import jsonify
from flask_restful import Resource, reqparse

from models.DeviceModel import DeviceModel


class Device(Resource):
    def get(self, deviceId):
        """
        Get current status, Started/not.
        :return:
        """
        pass


class DeviceList(Resource):
    def get(self):
        return DeviceModel.find_all()
        # Get list of registered devices.


class DeviceScan(Resource):
    def __init__(self, **kwargs):
        self.bt_adapter = kwargs['bt_adapter']

    def get(self):
        """
        GET /devices/scan
        Pull a list of visible BT devices using hcitool scan or the like.
        Note: actually use an adapter/client, to abstract that away.
        :return:
        """
        response = jsonify(self.bt_adapter.list_bt_devices())
        response.status_code = 200
        return response
