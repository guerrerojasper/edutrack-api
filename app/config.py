import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'a_very_secret_key')
LOGGER_NAME = os.environ.get('LOGGER_NAME', 'EDUTRACK_API')
DEBUG_MODE = os.environ.get('DEBUG_MODE', True)


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///edutrack.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = SECRET_KEY

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory database for testing

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/production_db'