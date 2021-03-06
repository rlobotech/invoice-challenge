from flask import request, session
from os import environ
import invoice_challenge.helpers.exception_helper as EH
import datetime
import jwt

def format_get_collection_response(data_resp, params):
    total = len(data_resp) if data_resp else 0
    page_size = params.get("pageSize") if params.get("pageSize") else 100
    page = params.get("page") if params.get("page") else 0

    formatted_response = {
        "data": data_resp,
        "total": total,
        "page_size": page_size,
        "page": page
    }
    return formatted_response

def check_authentication_token():
    auth_token = session['token'] if session else request.headers['token']
    decode_auth_token(auth_token)

def encode_auth_token(user_id):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=600),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
    }
    auth_token = jwt.encode(
        payload,
        environ.get("SECREAT_KEY"),
        algorithm='HS256'
    )
    return auth_token

def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, environ.get("SECREAT_KEY"))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise EH.TokenError('Signature expired. Please log in again.')
    except jwt.InvalidTokenError:
        raise EH.TokenError('Invalid token. Please log in again.')
