from app import db

class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    school = db.Column(db.String, nullable=False)
    grade = db.Column(db.String, nullable=False)
    section = db.Column(db.String, nullable=False)
    adviser = db.Column(db.String)
    rank = db.Column(db.Integer)
    school_year = db.Column(db.String, nullable=False)
    total_year = db.Column(db.Integer)

    def __repr__(self):
        return f'STUDENT - Name: {self.name}, School: {self.school}'
    
    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'school': self.school,
            'grade': self.grade,
            'section': self.section,
            'adviser': self.adviser,
            'rank': self.rank,
            'school_year': self.school_year,
            'total_year': self.total_year
        }