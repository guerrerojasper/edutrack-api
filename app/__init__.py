from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
api = Api(
    version='1.0',
    title='EduTrack API',
    description='EduTrack API endpoints',
    doc='/swagger'
)

def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    if config_class:
        app.config.from_object(config_class)

    db.init_app(app)
    api.init_app(app)

    from app.register_routes import register_routes
    register_routes()

    migrate = Migrate(app, db)

    return app
