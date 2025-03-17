from functools import wraps
from flask import request, abort
from app.config import SECRET_KEY

def require_api_key(func):
    """
        Decorator to validate API keys.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if not api_key or api_key != SECRET_KEY:
            abort(401, description='Invalid or Missing API Keys')
        
        return func(*args, **kwargs)
    
    return wrapper