from flask import json
from werkzeug.exceptions import HTTPException

class TokenError(Exception):
    pass

def internal_server_error_message():
    response = {
        "code": internal_server_error_status(),
        "name": "Internal Server Error",
        "description": "Something went wrong"
    }
    return response

def internal_server_error_status():
    return 500

def token_error_message(e):
    response = {
        "code": token_error_status(),
        "message": str(e)
    }
    return response

def token_error_status():
    return 401

def https_exception_response_format(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

def exception_handler(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except TokenError as e:
            message = token_error_message(e)
            status = token_error_status()
            return message, status
        except HTTPException as e:
            response = https_exception_response_format(e)
            return response
        except Exception:
            message = internal_server_error_message()
            status = internal_server_error_status()
            return message, status
    return wrapper
