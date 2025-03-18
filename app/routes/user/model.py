from app.models import User

from app import db

def get_all_users():
    users = User.query.all()

    return users

def get_user(**kwargs):
    user_email = kwargs['email']
    user = User.query.filter(User.email == user_email).first()
    
    return user