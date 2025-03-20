from flask_restx import Namespace, Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from datetime import timedelta

from app.schemas import login_schema, response_model
from .model import get_user
from app import api
from app.utils import require_api_key, create_response, descrypt_password

login_ns = Namespace(
    'login',
    description='Login-related operations.'
)

@login_ns.route('/')
class LoginHandler(Resource):
    @login_ns.doc('authenticate_user')
    @login_ns.expect(login_schema, validate=True)
    @login_ns.marshal_with(response_model)
    @require_api_key
    def post(self):
        data = api.payload
        email = data['email']
        password = data['password']

        user = get_user(email)
        if not user:
            return create_response('error', 'Invalid email!', None, 401)
        
        user_email = user.email
        user_password = user.password

        if not descrypt_password(password, user_password):
            return create_response('error', 'Invalid password!', None, 401)
        
        # create access token
        access_token = create_access_token(identity=user_email, expires_delta=timedelta(minutes=15))
        refresh_token = create_refresh_token(identity=user_email, expires_delta=timedelta(days=7))

        return create_response('success', '', {'access_token': access_token, 'refresh_token': refresh_token}, 200)

@login_ns.route('/refresh')
class LoginResourceHandler(Resource):
    @login_ns.doc('refresh_token')
    @login_ns.marshal_with(response_model)
    @jwt_required(refresh=True)
    @require_api_key
    def post(self):
        current_user_email = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user_email, expires_delta=timedelta(minutes=15))

        return create_response('success', '', {'access_token': new_access_token}, 200)