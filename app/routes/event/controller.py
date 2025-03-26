from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required

from app import api, logger
from app.schemas import event_model, response_model
from app.utils import create_response, require_api_key

from .model import get_events, create_event, get_event, update_event, delete_event

event_ns = Namespace(
    'event',
    description='Event-related operations.'
)

@event_ns.route('/')
class EventHandler(Resource):
    @event_ns.doc('list_events')
    @event_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def get(self):
        logger.info('Get all events')
        events = get_events()

        return create_response('success', '', [event.to_dict() for event in events], 200)
    
    @event_ns.doc('create_event')
    @event_ns.expect(event_model, validate=True)
    @event_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def post(self):
        data = api.payload

        logger.info('Create event')
        logger.info(f'Event body param: {data}')

        try:
            event = create_event(
                event_title=data['event_title'],
                date=data['date'], # YYYY-MM-DD
                time=data['time'], # HH:MM
                desc=data['desc'],
                location=data['location']
            )
        except Exception as e:
            logger.error(f'Create event error: {e}')

        return create_response('success', '', [event.to_dict()], 201)

@event_ns.route('/<int:id>')
@event_ns.param('id', 'The event ID identifier.')
class EventResourceHandler(Resource):
    @event_ns.doc('get_event')
    @event_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def get(self, id):
        logger.info('Get event')
        logger.info(f'Event path param ID: {id}')
        event = get_event(id)
        if not event:
           return create_response('error', 'Event not found!', [{'event_id': id}], 404)

        return create_response('success', '', [event.to_dict()], 200)
    
    @event_ns.doc('update_event')
    @event_ns.expect(event_model, validate=True)
    @event_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def patch(self, id):
        logger.info('Update event')
        data = api.payload
        logger.info(f'Event body param: {data}')
        event = update_event(id, data)

        if not event:
           return create_response('error', 'Event not found!', [{'event_id': id}], 404)

        return create_response('success', f'Event with ID number: {id} is updated!', [event.to_dict()], 201)

    @event_ns.doc('delete_event')
    @event_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def delete(self, id):
        logger.info('Delete event')
        logger.info(f'Event path param ID: {id}')
        is_deleted = delete_event(id)

        if not is_deleted:
            return create_response('error', 'Event not found!', [{'event_id': id}], 404)

        return create_response('success', f'Event with ID number: {id} is deleted!', [], 204)
