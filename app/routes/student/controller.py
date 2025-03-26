from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required

from app import api, logger
from app.schemas import response_model, student_model
from app.utils import require_api_key, create_response

from .model import get_students, get_student, create_student, update_student, delete_student

student_ns = Namespace(
    'student',
    description='Student-related operations.'
)

@student_ns.route('/')
class StudentHandler(Resource):
    @student_ns.doc('list_students')
    @student_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def get(self):
        logger.info('Get all students')
        students = get_students()

        return create_response('success', '', [student.to_dict() for student in students], 200)
    

    @student_ns.doc('create_student')
    @student_ns.expect(student_model, validate=True)
    @student_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def post(self):
        logger.info('Create student')
        data = api.payload
        logger.info(f'Student body param: {data}')

        try:
            student = create_student(
                name=data['name'],
                school=data['school'],
                grade=data['grade'],
                section=data['section'],
                adviser=data['adviser'],
                rank=data['rank'],
                school_year=data['school_year'],
                total_year=data['total_year']
            )
        except Exception as e:
            logger.error(f'Create student error: {e}')

        return create_response('success', '', [student.to_dict()], 201)


@student_ns.route('/<int:id>')
@student_ns.param('id', 'The student identifier.')
class StudentResourceHandler(Resource):
    @student_ns.doc('get_student')
    @student_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def get(self, id):
        logger.info('Get student')
        logger.info(f'Student path param: {id}')
        student = get_student(id)
        if not student:
            return create_response('error', 'Student not found!', [{'student_id': id}], 404)

        return create_response('success', '', [student.to_dict()], 200)
    
    @student_ns.doc('update_student')
    @student_ns.expect(student_model, validate=True)
    @student_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def patch(self, id):
        logger.info('Update student')
        data = api.payload
        logger.info(f'Student body param: {data}')
        student = update_student(id, data)
        if not student:
            return create_response('error', 'Student not found!', [{'student_id': id}], 404)
        
        return create_response('success', f'Student with ID number: {id} is updated!', [student.to_dict()], 201)
    
    @student_ns.doc('delete_student')
    @student_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def delete(self, id):
        logger.info('Delete student')
        logger.info(f'Student path param: {id}')
        is_deleted = delete_student(id)

        if not is_deleted:
            return create_response('error', 'Student not found!', [{'student_id': id}], 404)
        
        return create_response('success', f'Student with ID number: {id} is deleted! ', '', 204)
