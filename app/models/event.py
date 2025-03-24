from app import db

class Event(db.Model):
    __tablename__ = 'event'

    event_id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'EVENT - Event Title: {self.event_title}, Desc: {self.desc}'
    
    def to_dict(self):
        return {
            'event_id': self.event_id,
            'event_title': self.event_title,
            'date': self.date,
            'time': self.time,
            'desc': self.desc,
            'location': self.location
        }