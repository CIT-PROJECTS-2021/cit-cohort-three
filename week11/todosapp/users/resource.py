from todosapp.models import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from todosapp.schemas.app_schemas import UserSchema


user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Users(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    # http method: get
    @jwt_required()
    def get(self, user_id=None):
        if user_id:
            if not user_id == get_jwt_identity():
                return {"message": "You can only view your own profile"}, 403
            # get a single user
            user = User.query.filter_by(id=user_id).first()
            if not user:
                return {'message': 'User with id {} does not exist'.format(user_id)}, 404

            return user_schema.dump(user), 200
        
        
        # get all users
        users = User.query.all()
        return users_schema.dump(users), 200