from app import api

from app.routes import user_ns, login_ns, student_ns, subject_ns, event_ns

def register_routes():
    api.add_namespace(user_ns)
    api.add_namespace(login_ns)
    api.add_namespace(student_ns)
    api.add_namespace(subject_ns)
    api.add_namespace(event_ns)