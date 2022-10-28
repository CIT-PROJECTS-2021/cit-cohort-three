import os
from sqlalchemy import MetaData
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_mail import Mail
from flask_migrate import Migrate



convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
ma = Marshmallow()
migrate = Migrate()
api = Api()
jwt = JWTManager()
mail = Mail()
cors = CORS()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "weowiueroieufm"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todos.db"
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    from .errors.handlers import errors
    app.register_blueprint(errors)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user['id']

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        from todosapp.models import User
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()


    return app



from .auth import auth_routes
from .users import user_routes
from .todos import todos_routes


auth_routes(api)
user_routes(api)
todos_routes(api)