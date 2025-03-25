from app import db
from app.models import EventLog

def get_event_logs():
    event_logs = EventLog.query.all()

    return event_logs

def create_event_log(**kwargs):
    event_log = EventLog(
        action=kwargs['action'],
        user_name=kwargs['user_name'],
        date_time=kwargs['date_time']
    )

    db.session.add(event_log)
    db.session.commit()

    return event_log

def get_event_log(id):
    event_log = EventLog.query.filter(EventLog.event_log_id == id).first()

    return event_log

def update_event_log(id, data):
    event_log = EventLog.query.filter(EventLog.event_log_id == id).first()

    if event_log:
        event_log.action = data['action']
        event_log.user_name = data['user_name']
        event_log.date_time = data['date_time']

        db.session.commit()

    return event_log

def delete_event_log(id):
    event_log = EventLog.query.filter(EventLog.event_log_id == id).first()

    if not event_log:
        return False
    
    db.session.delete(event_log)
    db.session.commit()

    return True
