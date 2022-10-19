import os
from flask import Flask
from .config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# db variable initialization
db = SQLAlchemy()

# Marshmallow initialization
ma = Marshmallow()

# initialize migrate 
migrate = Migrate()

TEMPLATES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')


def create_app():
    app = Flask(__name__, template_folder=TEMPLATES_FOLDER)
    app.config.from_object(app_config['development'])
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from .views.fruits_view import views

    app.register_blueprint(views)

    return app