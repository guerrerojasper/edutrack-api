from app.models import Student
from app import db

def get_students():
    students = Student.query.all()

    return students

def get_student(id):
    student = Student.query.filter(Student.student_id == id).first()

    return student

def update_student(id, student_details):
    student = Student.query.filter(Student.student_id == id).first()

    if student:
        student.name = student_details['name']
        student.school = student_details['school']
        student.grade = student_details['grade']
        student.section = student_details['section']
        student.adviser = student_details['adviser']
        # student.rank = student_details['rank']
        student.school_year = student_details['school_year']
        student.total_year = student_details['total_year']

        db.session.commit()
    
    return student

def delete_student(id):
    student = Student.query.filter(Student.student_id == id).first()

    if not student:
        return False
    
    db.session.delete(student)
    db.session.commit()

    return True

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
