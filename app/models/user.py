from app import db

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    job_title = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f'USER - Name: {self.first_name}, Email: {self.email}, Job Title {self.job_title}'
    
    def to_dict(self):
        return {'user_id': self.user_id, 'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email, 'job_title': self.job_title}