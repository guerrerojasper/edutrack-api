from app.models import User

def test_invalid_api_key(client, auth_headers):
    """
        Test GET /usersn endpoint.
        Wrong API KEY
    """
    auth_headers['X-API-KEY'] = 'invalid_api_key'
    response = client.get('/users/', headers=auth_headers)
    assert response.status_code == 401

def test_unauthorized_access(client):
    """
        Test GET /usersn endpoint.
        No headers
    """
    response = client.get('/users/')
    assert response.status_code == 401