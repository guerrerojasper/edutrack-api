from flask_restx import fields
from app import api

event_log_model = api.model(
    'EventLog',
    {
        'event_log_id': fields.Integer(readOnly=True, description='The event log ID.'),
        'action': fields.String(required=True, description='The event log action.'),
        'user_name': fields.String(required=True, description='The event log user_name.'),
        'date_time': fields.String(required=True, description='The event log date_time.')
    }
)
