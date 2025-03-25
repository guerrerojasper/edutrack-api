from app.models import EventLog


def test_post_event_log(client, auth_headers):
    """
        Test POST /event_log endpoint.
        Test PATCH /event_log endpoint.
        Test DELETE /event_log endpoint.
        Test DB query.
    """
    # Add new event
    new_event_log = {
        'action': 'Update Student details',
        'user_name': 'admin1',
        'date_time': '2025-03-25 09:00:00'
    }
    response = client.post('/event_log/', headers=auth_headers, json=new_event_log)
    assert response.status_code == 201
    assert response.json['data'][0]['user_name'] == 'admin1'

    event_log = EventLog.query.filter(EventLog.user_name == 'admin1').first()
    assert event_log is not None
    assert event_log.user_name == 'admin1'

    # Update event 
    event_log_id = event_log.event_log_id
    patch_event_log = {
        'action': 'Add Student details',
        'user_name': 'admin1',
        'date_time': '2025-03-25 09:00:00'
    }
    response = client.patch(f'/event_log/{event_log_id}', headers=auth_headers, json=patch_event_log)
    assert response.status_code == 201
    assert response.json['data'][0]['action'] == 'Add Student details'

    event_log = EventLog.query.filter(EventLog.user_name == 'admin1').first()
    assert event_log is not None
    assert event_log.action == 'Add Student details'

    # Delete event
    response = client.delete(f'/event_log/{event_log_id}', headers=auth_headers)
    assert response.status_code == 204

    event_log = EventLog.query.filter(EventLog.user_name == 'admin1').first()
    assert event_log is None
    
def test_get_event(client, auth_headers):
    """
        Test GET /event_log endpoint.
    """
    response = client.get('/event_log/', headers=auth_headers)
    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data'] == []