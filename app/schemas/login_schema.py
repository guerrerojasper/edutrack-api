from flask_restx import fields
from app import api

login_schema = api.model(
    'Login',
    {
        'email': fields.String(required=True, description='The user email.'),
        'password': fields.String(required=True, description='The user password.')
    }
)