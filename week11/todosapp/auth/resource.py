from todosapp.models import User
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    create_refresh_token,
    get_jwt_identity,
    # jwt_refresh_token_required,
    # get_jwt_claims
)
from flask_restful import Resource, reqparse


# @view.route('/login', methods=['POST'])

# Login Class
class Login(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    # http method: post
    def post(self):
        self.parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        self.parser.add_argument('password', type=str, required=True, help='Password cannot be blank')

        data = self.parser.parse_args()

        return {'message': 'Login Successful'}, 200