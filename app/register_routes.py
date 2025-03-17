from app import api

from app.routes import user_ns

def register_routes():
    api.add_namespace(user_ns)