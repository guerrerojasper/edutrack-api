from flask_restx import fields
from app import api

event_model = api.model(
    'Event',
    {
        'event_id': fields.Integer(readOnly=True, description='The event ID.'),
        'event_title': fields.String(required=True, description='The event title.'),
        'date': fields.String(required=True, description='The event date.'),
        'time': fields.String(required=True, description='The event time.'),
        'desc': fields.String(required=True, description='The event description.'),
        'location': fields.String(required=True, description='The event location.')
    }
)