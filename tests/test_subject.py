from app.models import Subject

def test_get_subjects(client, auth_headers):
    """
        Test GET /subject endpoint.
        Test GET /subject/student endpoint.
    """
    response = client.get('/subject/', headers=auth_headers)
    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data'] == []

    response = client.get('/subject/student/1', headers=auth_headers)
    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data'] == []

def test_post_subject(client, auth_headers):
    """
        Test POST /subject endpoint.
        Test PATCH /subject endpoint.
        Test DELETE /subject endpoint.
        Test DB query.
    """
    # Add new subject
    new_subject = {
        'student_id': 1,
        'subject': 'English',
        'unit': '1',
        'status': 'PASSED',
        'final': 80,
        'first_grading': 80,
        'second_grading': 80,
        'third_grading': 80,
        'fourth_grading': 80
    }
    response = client.post('/subject/', headers=auth_headers, json=new_subject)
    assert response.status_code == 201
    assert response.json['data'][0]['subject'] == 'English'

    subject = Subject.query.filter(Subject.subject == 'English').first()
    assert subject is not None
    assert subject.subject == 'English'

    # Update subject
    subject_id = subject.subject_id
    patch_subject = {
        'student_id': 1,
        'subject': 'English',
        'unit': '1',
        'status': 'PASSED',
        'final': 90,
        'first_grading': 90,
        'second_grading': 90,
        'third_grading': 90,
        'fourth_grading': 90
    }
    response = client.patch(f'/subject/{subject_id}', headers=auth_headers, json=patch_subject)
    assert response.status_code == 201
    assert response.json['data'][0]['final'] == 90

    subject = Subject.query.filter(Subject.subject == 'English').first()
    assert subject is not None
    assert subject.final == 90

    # Delete subject
    response = client.delete(f'/subject/{subject_id}', headers=auth_headers)
    assert response.status_code == 204

    subject = Subject.query.filter(Subject.subject == 'Testing').first()
    assert subject is None
