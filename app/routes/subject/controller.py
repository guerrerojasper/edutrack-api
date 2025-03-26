from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required

from app import api, logger
from app.schemas import response_model, subject_model
from app.utils import create_response, require_api_key

from .model import get_subjects, create_subject, get_subject, update_subject, delete_subject, get_subjects_per_student

subject_ns = Namespace(
    'subject',
    description='Subject-related operations.'
)

@subject_ns.route('/')
class SubjectHandler(Resource):
    @subject_ns.doc('list_subjects')
    @subject_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def get(self):
        logger.info('Get all subjects')
        subjects = get_subjects()

        return create_response('success', '', [subject.to_dict() for subject in subjects], 200)
    
    @subject_ns.doc('create_subject')
    @subject_ns.expect(subject_model)
    @subject_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def post(self):
        logger.info('Create subject')
        data = api.payload
        logger.info(f'Subject body param: {data}')

        try:
            subject = create_subject(
                student_id=data['student_id'],
                subject=data['subject'],
                unit=data['unit'],
                status=data['status'],
                final=data['final'],
                first_grading=data['first_grading'],
                second_grading=data['second_grading'],
                third_grading=data['third_grading'],
                fourth_grading=data['fourth_grading']
            )
        except Exception as e:
            logger.error(f'Create subject error: {e}')

        return create_response('success', '', [subject.to_dict()], 201)
    
@subject_ns.route('/<int:id>')
@subject_ns.param('id', 'Subject ID identifier.')
class SubjectResourceHandler(Resource):
    @subject_ns.doc('get_subject')
    @subject_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def get(self, id):
        logger.info('Get subject')
        logger.info(f'Subject path param: {id}')
        subject = get_subject(id)  
        if not subject:
            return create_response('success', 'Subject not found!', [{'subject_id': id}], 404)

        return create_response('success', '', [subject.to_dict()], 200)
    
    @subject_ns.doc('update_subject')
    @subject_ns.expect(subject_model, validate=True)
    @subject_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def patch(self, id):
        logger.info('Update subject')
        data = api.payload
        logger.info(f'Subject body param: {data}')
        subject = update_subject(id, data)

        if not subject:
            return create_response('success', 'Subject not found!', [{'subject_id': id}], 404)

        return create_response('success', f'Subject with ID number: {id} is updated!', [subject.to_dict()], 201)
    
    @subject_ns.doc('delete_subject')
    @subject_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def delete(self, id):
        logger.info('Delete subject')
        logger.info(f'Subject path param: {id}')
        is_deleted = delete_subject(id)

        if not is_deleted:
            return create_response('success', 'Subject not found!', [{'subject_id': id}], 404)

        return create_response('success', f'Subject with ID number: {id} is deleted!', '', 204)

@subject_ns.route('/student/<int:id>')
@subject_ns.param('id', 'Student ID identifier.')
class SubjectResourceHandler2(Resource):
    @subject_ns.doc('get_subjects_per_student')
    @subject_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def get(self, id):
        logger.info('Get subject per student id')
        logger.info(f'Subject per student path param: {id}')
        subjects = get_subjects_per_student(id)

        return create_response('success', '', [subject.to_dict() for subject in subjects], 200)