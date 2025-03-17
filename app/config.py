import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'a_very_secret_key')


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///edutrack.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory database for testing

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/production_db'