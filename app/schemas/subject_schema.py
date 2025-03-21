from flask_restx import fields
from app import api

subject_model =  api.model(
    'Subject',
    {
        'subject_id': fields.Integer(readOnly=True, description='The subject ID.'),
        'student_id': fields.Integer(required=True, description='The student ID.'),
        'subject': fields.String(required=True, description='The subject name.'),
        'unit': fields.String(required=True, description='The subject unit.'),
        'status': fields.String(required=True, description='The subject status.'),
        'final': fields.Integer(required=True, description='The subject final grade.'),
        'first_grading': fields.Integer(required=True, description='The subject grade for first grading.'),
        'second_grading': fields.Integer(required=True, description='The subject grade for second grading.'),
        'third_grading': fields.Integer(required=True, description='The subject grade for third grading.'),
        'fourth_grading': fields.Integer(required=True, description='The subject grade for fourth grading.')
    }
)