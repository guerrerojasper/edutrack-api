from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import api, db, logger
from app.schemas import user_model, response_model
from app.utils import require_api_key, hashed_password, create_response
from app.models import User

from .model import get_all_users, get_user

user_ns = Namespace(
    'users',
    description='User-related operations.'
)

@user_ns.route('/')
class UserHandler(Resource):
    @user_ns.doc('list_users')
    @user_ns.marshal_with(response_model)
    @jwt_required()
    @require_api_key
    def get(self):
        logger.info('Get all users')
        users = get_all_users()

        return create_response('success', f'Requestor: {get_jwt_identity()}', [user.to_dict() for user in users], 200)
    
    @user_ns.doc('create_user')
    @user_ns.expect(user_model, validate=True)
    @user_ns.marshal_with(response_model)
    @require_api_key
    def post(self):
        logger.info('Create user')
        data = api.payload
        logger.info(f'User body param: {data}')
        
        exiting_user = get_user(email=data['email'])
        if exiting_user:
            return create_response('error', 'User already exist!', '', 201)

        user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            job_title=data['job_title'],
            email=data['email'],
            password=hashed_password(data['password'])
        )

        db.session.add(user)
        db.session.commit()

        return create_response('success', '', user.to_dict(), 201)