from flask import session
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
# from invoice_challenge import bcrypt
import invoice_challenge.helpers.controller_helper as CH
import invoice_challenge.helpers.exception_helper as EH

class Login(Resource):
    @EH.exception_handler
    def get(self):
        auth_token = CH.encode_auth_token(1)
        responseObject = {
            'code': 200,
            'message': 'Successfully logged in.',
            'auth_token': auth_token.decode()
        }

        session.clear()
        session['token'] = auth_token.decode()

        return responseObject, 200

    @EH.exception_handler
    def post(self):
        auth_token = CH.encode_auth_token(1)
        responseObject = {
            'code': 200,
            'message': 'Successfully logged in.',
            'auth_token': auth_token.decode()
        }

        session.clear()
        session['token'] = auth_token.decode()

        return responseObject, 200
