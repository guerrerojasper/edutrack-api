from app import db

class Subject(db.Model):
    __tablename__ = 'subject'

    subject_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String, nullable=False)
    unit = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    final = db.Column(db.Integer, nullable=False)
    first_grading = db.Column(db.Integer, nullable=False)
    second_grading = db.Column(db.Integer, nullable=False)
    third_grading = db.Column(db.Integer, nullable=False)
    fourth_grading = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'SUBJECT - Subject: {self.subject}, student_id: {self.student_id}'
    
    def to_dict(self):
        return {
            'subject_id': self.subject_id,
            'student_id': self.student_id,
            'subject': self.subject,
            'unit': self.unit,
            'status': self.status,
            'final': self.final,
            'first_grading': self.first_grading,
            'second_grading': self.second_grading,
            'third_grading': self.third_grading,
            'fourth_grading': self.fourth_grading
        }
