from flask import request, session
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from werkzeug.exceptions import HTTPException
# from invoice_challenge import bcrypt
import invoice_challenge.helpers.controller_helper as CH
import sys

class Login(Resource):
    def get(self):
        try:
            auth_token = CH.encode_auth_token(1)
            responseObject = {
                'code': 200,
                'message': 'Successfully logged in.',
                'auth_token': auth_token.decode()
            }

            session.clear()
            session['token'] = auth_token.decode()

            return responseObject, 200
        except HTTPException as e:
            response = CH.https_exception_response_format(e)
            return response
        except Exception as e:
            message = CH.internal_server_error_message()
            status = CH.internal_server_error_status()
            return message, status

    def post(self):
        try:
            auth_token = CH.encode_auth_token(1)
            responseObject = {
                'code': 200,
                'message': 'Successfully logged in.',
                'auth_token': auth_token.decode()
            }

            session.clear()
            session['token'] = auth_token.decode()

            return responseObject, 200
        except HTTPException as e:
            response = CH.https_exception_response_format(e)
            return response
        except Exception as e:
            message = CH.internal_server_error_message()
            status = CH.internal_server_error_status()
            return message, status
