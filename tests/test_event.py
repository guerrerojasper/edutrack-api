from app.models import Event


def test_post_event(client, auth_headers):
    """
        Test POST /event endpoint.
        Test PATCH /event endpoint.
        Test DELETE /event endpoint.
        Test DB query.
    """
    # Add new event
    new_event = {
        'event_title': 'Test Event',
        'date': '2025-03-28',
        'time': '09:00',
        'desc': 'Test event desc.',
        'location': 'Test City'
    }
    response = client.post('/event/', headers=auth_headers, json=new_event)
    assert response.status_code == 201
    assert response.json['data'][0]['event_title'] == 'Test Event'

    event = Event.query.filter(Event.event_title == 'Test Event').first()
    assert event is not None
    assert event.desc == 'Test event desc.'

    # Update event 
    event_id = event.event_id
    patch_event = {
        'event_title': 'Test Event',
        'date': '2025-03-30',
        'time': '09:00',
        'desc': 'Test event desc.',
        'location': 'Test City'
    }
    response = client.patch(f'/event/{event_id}', headers=auth_headers, json=patch_event)
    assert response.status_code == 201
    assert response.json['data'][0]['date'] == '2025-03-30'

    event = Event.query.filter(Event.event_title == 'Test Event').first()
    assert event is not None
    assert event.date == '2025-03-30'

    # Delete event
    response = client.delete(f'/event/{event_id}', headers=auth_headers)
    assert response.status_code == 204

    event = Event.query.filter(Event.event_title == 'Test Event').first()
    assert event is None
    
def test_get_event(client, auth_headers):
    """
        Test GET /event endpoint.
    """
    response = client.get('/event/', headers=auth_headers)
    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data'] == []