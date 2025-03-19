from app.models import User
from app import db

def get_user(email):
    user = User.query.filter(User.email == email).first()

    return user