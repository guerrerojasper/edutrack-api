import time
import uuid

from flask import Flask, request, g
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from app.utils import create_response
from app.logger import LogHandler

from app.config import LOGGER_NAME, DEBUG_MODE

logger = LogHandler(LOGGER_NAME, DEBUG_MODE)
logger.log_setup()

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

    # logger callback
    @app.before_request
    def log_request_info():
        g.start_time = time.time() # timer
        g.request_id = str(uuid.uuid4()) # unique request id

        logger.info(
            f'Request ID: {g.request_id}, Method: {request.method}, URL: {request.url}'
        )
    
    @app.after_request
    def log_response_info(response):
        duration = time.time() - g.start_time
        logger.info(
            f'Request ID: {g.request_id}, Status: {response.status_code}, Duration: {duration:.2f}s'
        )

        return response
    
    @app.teardown_request
    def log_teardown(exception=None):
        if exception:
            logger.error(f'Teardown error: {str(exception)}')

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

    logger.info('App Started')

    return app
