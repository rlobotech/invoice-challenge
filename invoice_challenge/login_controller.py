from flask import session
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from invoice_challenge.user_model import UserModel
import invoice_challenge.helpers.controller_helper as CH
import invoice_challenge.helpers.exception_helper as EH

def user_request_parser():
    parser = RequestParser(bundle_errors=True)
    parser.add_argument("email",    type=str, required=True, help="Please enter a valid String as a document")
    parser.add_argument("password", type=str, required=True, help="Please enter a valid String as a description")
    return parser

class Login(Resource):
    @EH.exception_handler
    def post(self):
        user_model = UserModel()
        params = user_request_parser().parse_args()
        data_resp = user_model.read_item(params)

        auth_token = CH.encode_auth_token(data_resp[0]["id"])
        responseObject = {
            'code': 200,
            'message': 'Successfully logged in.',
            'auth_token': auth_token.decode()
        }

        session.clear()
        session['token'] = auth_token.decode()

        return responseObject, 200

    '''
    This Get function should not exist in production.
    This is only for testing on browser by starting a session
        using the admin user already created on database.
    '''
    @EH.exception_handler
    def get(self):
        user_model = UserModel()
        params = {
            "email": "admin@admin",
            "password": "admin"
        }
        data_resp = user_model.read_item(params)

        auth_token = CH.encode_auth_token(data_resp[0]["id"])
        responseObject = {
            'code': 200,
            'message': 'Successfully logged in.',
            'auth_token': auth_token.decode()
        }

        session.clear()
        session['token'] = auth_token.decode()

        return responseObject, 200
