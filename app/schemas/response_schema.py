from flask_restx import fields
from app import api

response_model = api.model(
    'Response',
    {
        'status': fields.String(description='Status of the operations.'),
        'message': fields.String(description='Additional Information.'),
        'data': fields.Raw(description='Optional data payload.')
    }
)