import pytest

from app import create_app, db

@pytest.fixture
def client():
    app = create_app(
        config_class='app.config.TestConfig'
    )

    with app.test_client() as client:
        with app.app_context():
            db.create_all() # Create tables in the test database
        yield client

        with app.app_context():
            db.session.remove()
            db.drop_all() # Clean up after tests

@pytest.fixture
def auth_headers():
    return {
        'X-API-KEY': 'a_very_secret_key'
    }