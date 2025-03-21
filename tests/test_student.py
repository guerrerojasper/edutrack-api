from app.models import Student

def test_post_student(client, auth_headers):
    """
        Test POST /student endpoint.
        Test DB query.
        Test PATCH /student endpoint.
    """
    # Add new student
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

    # Update student 
    student_id = student.student_id
    patch_student = {
        'name': 'Testing',
        'school': 'AMACC',
        'grade': '12',
        'section': 'A',
        'adviser': 'Mr. John Doe',
        'rank': '1',
        'school_year': '2023-2024',
        'total_year': '12'
    }
    response = client.patch(f'/student/{student_id}', headers=auth_headers, json=patch_student)
    assert response.status_code == 201
    assert response.json['data'][0]['name'] == 'Testing'

    student = Student.query.filter(Student.name == 'Testing').first()
    assert student is not None
    assert student.name == 'Testing'

    # Delete student
    response = client.delete(f'/student/{student_id}', headers=auth_headers)
    assert response.status_code == 204
    student = Student.query.filter(Student.name == 'Testing').first()
    assert student is None
    

def test_get_student(client, auth_headers):
    """
        Test GET /student endpoint.
    """
    response = client.get('/student/', headers=auth_headers)
    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data'] == []