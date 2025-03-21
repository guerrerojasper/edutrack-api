from app.models import Subject
from app import db

def get_subjects():
    subjects = Subject.query.all()

    return subjects

def get_subject(id):
    subject = Subject.query.filter(Subject.subject_id == id).first()

    return subject

def update_subject(id, subject_details):
    subject = Subject.query.filter(Subject.subject_id == id).first()

    if subject:
        subject.subject = subject_details['subject']
        subject.unit = subject_details['unit']
        subject.status = subject_details['status']
        subject.final = subject_details['final']
        subject.first_grading = subject_details['first_grading']
        subject.second_grading = subject_details['second_grading']
        subject.third_grading = subject_details['third_grading']
        subject.fourth_grading = subject_details['fourth_grading']

        db.session.commit()

    return subject

def delete_subject(id):
    subject = Subject.query.filter(Subject.subject_id == id).first()

    if not subject:
        return False
    
    db.session.delete(subject)
    db.session.commit()

    return True

def create_subject(**kwargs):
    subject = Subject(
        student_id=kwargs['student_id'],
        subject=kwargs['subject'],
        unit=kwargs['unit'],
        status=kwargs['status'],
        final=kwargs['final'],
        first_grading=kwargs['first_grading'],
        second_grading=kwargs['second_grading'],
        third_grading=kwargs['third_grading'],
        fourth_grading=kwargs['fourth_grading']
    )

    db.session.add(subject)
    db.session.commit()

    return subject

def get_subjects_per_student(id):
    subjects = Subject.query.filter(Subject.student_id == id).all()

    return subjects