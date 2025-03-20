from app.models import User

def test_create_user(client, auth_headers):
    """
        Test POST /users endpoint.
        Test DB get user query.
    """
    new_user = {
        'first_name': 'John',
        'last_name': 'Doe',
        'job_title': 'Admin',
        'email': 'johndoe@gmail.com',
        'password': '12345678'
    }
    response = client.post('/users/', headers=auth_headers, json=new_user)
    assert response.status_code == 201
    assert response.json['data']['first_name'] == 'John'
    assert response.json['data']['email'] == 'johndoe@gmail.com'

    user = User.query.filter(User.email == 'johndoe@gmail.com').first()
    assert user is not None
    assert user.first_name == 'John'

def test_get_users(client, auth_headers):
    """
        Test GET /users endpoint.
    """
    response = client.get('/users/', headers=auth_headers)
    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data'] != []
