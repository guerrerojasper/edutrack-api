from app import db
from app.models import Event


def get_events():
    events = Event.query.all()

    return events

def create_event(**kwargs):
    event = Event(
        event_title=kwargs['event_title'],
        date=kwargs['date'],
        time=kwargs['time'],
        desc=kwargs['desc'],
        location=kwargs['location']
    )

    db.session.add(event)
    db.session.commit()

    return event

def get_event(id):
    event = Event.query.filter(Event.event_id == id).first()

    return event

def update_event(id, data):
    event = Event.query.filter(Event.event_id == id).first()

    if event:
        event.event_title = data['event_title']
        event.date = data['date']
        event.time = data['time']
        event.desc = data['desc']
        event.location = data['location']

        db.session.commit()

    return event

def delete_event(id):
    event = Event.query.filter(Event.event_id == id).first()

    if not event:
        return False
    
    db.session.delete(event)
    db.session.commit()

    return True

