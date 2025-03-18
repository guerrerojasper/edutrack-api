
def create_response(status, message, data=None, status_code=200):
    return {
        'status': status,
        'message': message,
        'data': data
    }, status_code