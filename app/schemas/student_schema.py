from flask_restx import fields
from app import api

student_model = api.model(
    'Student',
    {
        'student_id': fields.String(readOnly=True, description='The Student ID'),
        'name': fields.String(required=True, description='The Student Name'),
        'school': fields.String(required=True, description='The Student School'),
        'grade': fields.String(required=True, description='The Student Grade'),
        'section': fields.String(required=True, description='The Student Section'),
        'adviser': fields.String(required=True, description='The Student Adviser'),
        'rank': fields.String(required=True, description='The Student Rank'),
        'school_year': fields.String(required=True, description='The Student School Year'),
        'total_year': fields.String(required=True, description='The Student Total Years')
    }
)