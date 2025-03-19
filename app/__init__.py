from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from app.utils import create_response

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
    jwt = JWTManager(app)

    # jwt custom callback
    @jwt.unauthorized_loader
    def unauthorized_callback(error):
        return create_response('error', 'Missing or Invalid Token.', None, 401)
    
    @jwt.expired_token_loader
    def expired_toke_callback(jwt_header, jwt_payload):
        return create_response('error', 'Token has expired.', None, 401)
    
    from app.register_routes import register_routes
    register_routes()

    migrate = Migrate(app, db)

    return app
