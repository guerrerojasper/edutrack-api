from app import db

class EventLog(db.Model):
    __tablename__ = 'event_log'

    event_log_id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String, nullable=False)
    user_name = db.Column(db.String, nullable=False)
    date_time = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'EVENT_LOG - user_name: {self.user_name}, Action: {self.action}'
    
    def to_dict(self):
        return {
            'event_log_id': self.event_log_id,
            'action': self.action,
            'user_name': self.user_name,
            'date_time': self.date_time
        }
