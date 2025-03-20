from app.models import Student
from app import db

def get_students():
    students = Student.query.all()

    return students

def create_student(**kwargs):
    student = Student(
        name=kwargs['name'],
        school=kwargs['school'],
        grade=kwargs['grade'],
        section=kwargs['section'],
        adviser=kwargs['adviser'],
        rank=kwargs['rank'],
        school_year=kwargs['school_year'],
        total_year=kwargs['total_year']
    )

    db.session.add(student)
    db.session.commit()

    return student
