import os
from flask import Flask
from .config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_login import LoginManager

# db variable initialization
db = SQLAlchemy()

# Marshmallow initialization
ma = Marshmallow()

# initialize migrate 
migrate = Migrate()

# Login manager
login_manager = LoginManager()

TEMPLATES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


def create_app():
    app = Flask(__name__, template_folder=TEMPLATES_FOLDER)
    app.config.from_object(app_config['development'])
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    from .views.fruits_view import views as fruits_views
    from .views.hacker_news import hviews as hacker_news_views
    from .views.cbs_view import cviews as cbs_views
    from .views.users import userviews as users_views
    from .views.todos_view import todos as todos_views

    app.register_blueprint(fruits_views)
    app.register_blueprint(hacker_news_views)
    app.register_blueprint(cbs_views)
    app.register_blueprint(users_views)
    app.register_blueprint(todos_views)

    return app