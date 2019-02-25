from flask import Flask, request, jsonify
from flask_restful import Api
from flask_jwt import JWT

from db import db
from exceptions.ValidationException import ValidationException
from resources import Control, Profile, Device
from resources.Device import DeviceList
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Very secret password.'
app.url_map.strict_slashes = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)


@app.errorhandler(ValidationException)
def handle_validation_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.after_request
def add_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response


#api.add_resource(SinkList, '/sinks')
#api.add_resource(HubList, '/hubs')  #for when I've got multi-device synchronized playing. For now, only report the self.
api.add_resource(Control, '/control')  #For starting/stopping connections


api.add_resource(DeviceList, '/devices')
api.add_resource(Device, '/devices/<int:deviceId>')



api.add_resource(Profile, '/profiles')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
