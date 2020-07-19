from flask import json, request, session
from werkzeug.exceptions import HTTPException
import datetime
import jwt
import sys

class TokenError(Exception):
    pass

def format_get_collection_response(data_resp, params):
    total = len(data_resp) if data_resp else 0
    page_size = params["pageSize"] if params["pageSize"] else 100
    page = params["page"] if params["page"] else 0

    formatted_response = {
        "data": data_resp,
        "total": total,
        "page_size": page_size,
        "page": page
    }
    return formatted_response

# Generic controller response messages and its status by exceptions
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

def check_authentication_token():
    auth_token = session['token'] if session else request.headers['token']
    decode_auth_token(auth_token)

def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            "very_secreat",
            algorithm='HS256'
        )
    except Exception as e:
        raise e

def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, "very_secreat")
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise TokenError('Signature expired. Please log in again.')
    except jwt.InvalidTokenError:
        raise TokenError('Invalid token. Please log in again.')

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
