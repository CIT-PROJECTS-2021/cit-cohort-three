from todosapp.models import User, Todo
from flask_marshmallow import Schema
from flask_marshmallow.sqla import SQLAlchemyAutoSchema


class UserSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'email')


class TodoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        include_fk = True