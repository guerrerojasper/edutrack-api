from app.models import Student

def test_post_student(client, auth_headers):
    """
        Test POST /student endpoint.
        Test DB query.
    """
    new_student = {
        'name': 'Test',
        'school': 'AMACC',
        'grade': '12',
        'section': 'A',
        'adviser': 'Mr. John Doe',
        'rank': '1',
        'school_year': '2023-2024',
        'total_year': '12'
    }
    response = client.post('/student/', headers=auth_headers, json=new_student)
    assert response.status_code == 201
    assert response.json['data'][0]['name'] == 'Test'

    student = Student.query.filter(Student.name == 'Test').first()
    assert student is not None
    assert student.name == 'Test'

def test_get_student(client, auth_headers):
    """
        Test GET /student endpoint.
    """
    response = client.get('/student/', headers=auth_headers)
    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data'] == []