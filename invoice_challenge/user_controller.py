from flask import session
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
# from invoice_challenge import bcrypt
from invoice_challenge.user_model import UserModel
import invoice_challenge.helpers.controller_helper as CH
import invoice_challenge.helpers.exception_helper as EH

def user_request_parser():
    parser = RequestParser(bundle_errors=True)
    parser.add_argument("email",       type=str,   help="Please enter a valid String as a document")
    parser.add_argument("password",    type=str,   help="Please enter a valid String as a description")
    return parser

class User(Resource):
    @EH.exception_handler
    def post(self):
        params = user_request_parser().parse_args()
        user_model = UserModel()
        user_model.create_item(params)
        return {}, 201

    @EH.exception_handler
    def get(self):
        CH.check_authentication_token()

        parser = user_request_parser()
        parser.add_argument("pageSize",       type=int, location="args")
        parser.add_argument("page",           type=int, location="args")
        parser.add_argument("order_by_desc",  type=str, location="args")
        parser.add_argument("order_by_asc",   type=str, location="args")
        params = parser.parse_args()

        user_model = UserModel()
        data_resp = user_model.read_items(params)

        formmated_resp = CH.format_get_collection_response(data_resp, params)
        return formmated_resp, 200
