from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required

from app import api, logger
from app.schemas import response_model, event_log_model
from app.utils import create_response, require_api_key

from .model import get_event_logs, create_event_log, get_event_log, update_event_log, delete_event_log

event_log_ns = Namespace(
    'event_log',
    description='EventLog-related operations.'
)

@event_log_ns.route('/')
class EventLogHandler(Resource):
    @event_log_ns.doc('list_event_logs')
    @event_log_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def get(self):
        logger.info('Get all event logs')
        event_logs = get_event_logs()
        
        return create_response('success', '', [event_log.to_dict() for event_log in event_logs], 200)
    
    @event_log_ns.doc('create_event_log')
    @event_log_ns.expect(event_log_model, validate=True)
    @event_log_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def post(self):
        logger.info('Create event log')
        data = api.payload
        logger.info(f'Event log body param: {data}')
        event_log = create_event_log(
            action=data['action'],
            user_name=data['user_name'],
            date_time=data['date_time'] # YYYY-MM-DD hh:mm:ss
        )

        return create_response('success', '', [event_log.to_dict()], 201)

@event_log_ns.route('/<int:id>')
@event_log_ns.param('id', 'The event log ID identifier.')
class EventLogResourceHandler(Resource):
    @event_log_ns.doc('get_event_log')
    @event_log_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def get(self, id):
        logger.info('Get event log')
        logger.info(f'Event log path param: {id}')
        event_log = get_event_log(id)

        if not event_log:
            return create_response('error', 'Event log not found!', [{'event_log_id': id}], 404)
        
        return create_response('success', '', [event_log.to_dict()], 200)
    
    @event_log_ns.doc('update_event_log')
    @event_log_ns.expect(event_log_model, validate=True)
    @event_log_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def patch(self, id):
        logger.info('Update event log')
        data = api.payload
        logger.info(f'Event log body param: {data}')
        event_log = update_event_log(id, data)

        if not event_log:
            return create_response('error', 'Event log not found!', [{'event_log_id': id}], 404)
        
        return create_response('success', f'Event log with ID number: {id} is updated!', [event_log.to_dict()], 201)
    
    @event_log_ns.doc('delete_event_log')
    @event_log_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def delete(self, id):
        logger.info('Delete event log')
        logger.info('Event log path param: {id}')
        is_deleted = delete_event_log(id)
        if not is_deleted:
            return create_response('error', 'Event log not found!', [{'event_log_id': id}], 404)
        
        return create_response('success', f'Event log with ID number: {id} is deleted!', [], 204)
