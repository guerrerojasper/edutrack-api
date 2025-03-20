import pytest
import requests

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
def auth_tokens(client):
    # Create new user
    headers = {
        'X-API-KEY': 'a_very_secret_key'
    }
    new_user = {
        'first_name': 'Test',
        'last_name': 'Test',
        'job_title': 'Admin',
        'email': 'test@gmail.com',
        'password': '12345678'
    }
    response = client.post('/users/', headers=headers, json=new_user)
    assert response.status_code == 201

    login_data = {
        'email': 'test@gmail.com',
        'password': '12345678'
    }
    # Login as new user and get the access_token
    response = client.post('/login/', headers=headers, json=login_data)
    assert response.status_code == 200

    access_token = response.json['data']['access_token']

    return {
        'access_token': access_token
    }

@pytest.fixture
def auth_headers(auth_tokens):
    return {
        'Authorization': f'Bearer {auth_tokens['access_token']}',
        'X-API-KEY': 'a_very_secret_key'
    }