from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource

from .dto import UserDto
from .service import UserService

api = UserDto.api
data_resp = UserDto.data_resp


@api.route("/")
class UserGet(Resource):
    @jwt_required
    def get(self):
        """ Get a specific user's data by their id """
        return UserService.get_user_data(get_jwt_identity())

    @api.expect(api, validate=True)
    @jwt_required
    def put(self):
        requested_data = request.get_json()
        return UserService.update_user(get_jwt_identity(), requested_data)
