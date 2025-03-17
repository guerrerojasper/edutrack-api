from flask_restx import Namespace, Resource
from app.models.user import User
from app.schemas.user_schema import user_model, user_response_model
from app import api, db

from app.utils import require_api_key, hashed_password

user_ns = Namespace(
    'users',
    description='User-related operations.'
)

@user_ns.route('/')
class UserHandler(Resource):
    @user_ns.doc('list_users')
    @user_ns.marshal_with(user_response_model)
    @require_api_key
    def get(self):
        users = User.query.all()

        return users, 200
    
    @user_ns.doc('create_user')
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_response_model)
    @require_api_key
    def post(self):
        data = api.payload
        user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            job_title=data['job_title'],
            email=data['email'],
            password=hashed_password(data['password'])
        )

        db.session.add(user)
        db.session.commit()

        return user, 201