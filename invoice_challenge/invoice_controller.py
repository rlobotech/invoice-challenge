from flask import json, request, session
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from werkzeug.exceptions import HTTPException
from invoice_challenge.invoice_model import InvoiceModel
import invoice_challenge.helpers.controller_helper as CH
import sys

# RequestParser serve as an allowlist params (old whitelist params).
def invoice_request_parser():
    parser = RequestParser(bundle_errors=True)
    parser.add_argument("document",       type=str,   help="Please enter a valid String as a document")
    parser.add_argument("description",    type=str,   help="Please enter a valid String as a description")
    parser.add_argument("amount",         type=float, help="Please enter valid Decimal as an amount")
    parser.add_argument("referenceMonth", type=str,   help="Please enter a valid Datetime as a referenceMonth")
    parser.add_argument("referenceYear",  type=int,   help="Please enter valid Integer as a referenceYear")
    return parser

# def exception_handler(func):
#     print('1', file=sys.stderr)
#     def wrapper(self, *args, **kwargs):
#         try:
#             return func(self, *args, **kwargs)
#         except CH.TokenError as e:
#             message = CH.token_error_message(e)
#             status = CH.token_error_status()
#             return message, status
#         except HTTPException as e:
#             response = CH.https_exception_response_format(e)
#             return response
#         except Exception:
#             message = CH.internal_server_error_message()
#             status = CH.internal_server_error_status()
#             return message, status
#     return wrapper


class Invoice(Resource):
    def get(self, id):
        try:
            invoice_model = InvoiceModel()
            data_resp = invoice_model.read_item(id)
            return data_resp, 200
        except CH.TokenError as e:
            message = CH.token_error_message(e)
            status = CH.token_error_status()
            return message, status
        except HTTPException as e:
            response = CH.https_exception_response_format(e)
            return response
        except Exception:
            message = CH.internal_server_error_message()
            status = CH.internal_server_error_status()
            return message, status

    def put(self, id):
        try:
            params = invoice_request_parser().parse_args()
            invoice_model = InvoiceModel()
            invoice_model.update_item(id, params)
            return {}, 204
        except CH.TokenError as e:
            message = CH.token_error_message(e)
            status = CH.token_error_status()
            return message, status
        except HTTPException as e:
            response = CH.https_exception_response_format(e)
            return response
        except Exception as e:
            message = CH.internal_server_error_message()
            status = CH.internal_server_error_status()
            return message, status

    def delete(self, id):
        try:
            invoice_model = InvoiceModel()
            invoice_model.delete_item(id)
            return {}, 204
        except CH.TokenError as e:
            message = CH.token_error_message(e)
            status = CH.token_error_status()
            return message, status
        except HTTPException as e:
            response = CH.https_exception_response_format(e)
            return response
        except Exception:
            message = CH.internal_server_error_message()
            status = CH.internal_server_error_status()
            return message, status

class InvoiceCollection(Resource):
    def post(self):
        try:
            CH.check_authentication_token()

            params = invoice_request_parser().parse_args()
            invoice_model = InvoiceModel()
            invoice_model.create_item(params)
            return {}, 201
        except CH.TokenError as e:
            message = CH.token_error_message(e)
            status = CH.token_error_status()
            return message, status
        except HTTPException as e:
            response = CH.https_exception_response_format(e)
            return response
        except Exception as e:
            message = CH.internal_server_error_message()
            status = CH.internal_server_error_status()
            return message, status

    @CH.exception_handler
    def get(self):
        print('2', file=sys.stderr)
        CH.check_authentication_token()

        parser = invoice_request_parser()
        parser.add_argument("pageSize",       type=int, location="args")
        parser.add_argument("page",           type=int, location="args")
        parser.add_argument("order_by_desc",  type=str, location="args")
        parser.add_argument("order_by_asc",   type=str, location="args")
        params = parser.parse_args()

        invoice_model = InvoiceModel()
        data_resp = invoice_model.read_items(params)

        formmated_resp = CH.format_get_collection_response(data_resp, params)
        return formmated_resp, 200
