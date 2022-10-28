from todosapp.models import User
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
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

        user = User.find_user_by_email(data['email'])

        if user and User.verify_hash(data['password'], user.password):
            identity = {'id': user.id, 'name': user.name}
            access_token = create_access_token(identity=identity)
            refresh_token = create_refresh_token(identity=identity)
            return {'access_token': access_token, 'refresh_token': refresh_token}, 200
        else:
            return {'message': 'Invalid credentials'}, 401

# Register Class
class Register(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    # http method: post
    def post(self):
        self.parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
        self.parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        self.parser.add_argument('password', type=str, required=True, help='Password cannot be blank')

        data = self.parser.parse_args()

        if User.find_user_by_email(data['email']):
            return {'message': 'User with {} already exists'.format(data['email'])}, 400

        new_user = User(
            name=data['name'],
            email=data['email'],
            password=User.hash_password(data['password'])
        )
        new_user.save()
        return {'message': 'User {} was created'.format(data['email'])}, 201