from todosapp.models import User, Todo
from flask_marshmallow import Schema


class UserSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'email')