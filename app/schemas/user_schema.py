from flask_restx import fields
from app import api

user_model = api.model(
    'User', 
    {
        'user_id': fields.Integer(readOnly=True, description='The user ID'),
        'first_name': fields.String(required=True, description='The first name'),
        'last_name': fields.String(required=True, description='The last name'),
        'job_title': fields.String(required=True, description='The job title'),
        'email': fields.String(required=True, description='The user email'),
        'password': fields.String(required=True, description='The user password')

    }
)

user_response_model = api.model(
    'UserResponse', 
    {
        'user_id': fields.Integer(description='The user ID'),
        'first_name': fields.String(description='The first name'),
        'last_name': fields.String(description='The last name'),
        'job_title': fields.String(description='The job title'),
        'email': fields.String(description='The user email'),
        'password': fields.String(description='The user password')
    }
)
