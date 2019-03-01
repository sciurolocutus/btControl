from flask import jsonify
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.DeviceModel import DeviceModel
from dto.bt.Device import Device as DeviceDTO


class Device(Resource):
    def get(self, device_address):
        device_model = DeviceModel.find_by_addr(device_address)
        return [DeviceDTO(device_model.addr, device_model.name, device_model.nickname)]


class DeviceList(Resource):
    postParser = reqparse.RequestParser()
    #TODO: add mac address validation
    postParser.add_argument('address', type=str, required=True,
                           location='json',
                           help='mac address of the bluetooth device')
    postParser.add_argument('name', type=str, required=True,
                            location='json',
                            help='name of the bluetooth device')
    postParser.add_argument('nickname', type=str, required=False,
                            location='json',
                            help='nickname of the bluetooth device')
    def get(self):
        return [DeviceDTO(d.addr, d.name, d.nickname) for d in DeviceModel.find_all()]
        # Get list of registered devices.

    def post(self):
        args = self.postParser.parse_args()
        device = DeviceModel(args.address, args.name, args.nickname)
        try:
            device.save_to_db()
        except:
            return {'message': 'An error occurred creating the device'}, 500

        deviceDto = DeviceDTO(device.addr, device.name, device.nickname)
        response = jsonify(deviceDto)
        response.status_code = 201
        return response


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
