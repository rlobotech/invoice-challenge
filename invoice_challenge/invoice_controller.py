from flask import json
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from werkzeug.exceptions import HTTPException
from invoice_challenge.invoice_model import InvoiceModel
import invoice_challenge.controller_helper as CH

# RequestParser serve as an allowlist params (old whitelist params).
parser = RequestParser(bundle_errors=True)
parser.add_argument("document",       type=str,   help="Please enter a valid String as a document")
parser.add_argument("description",    type=str,   help="Please enter a valid String as a description")
parser.add_argument("amount",         type=float, help="Please enter valid Decimal as an amount")
parser.add_argument("referenceMonth", type=str,   help="Please enter a valid Datetime as a referenceMonth")
parser.add_argument("referenceYear",  type=int,   help="Please enter valid Integer as a referenceYear")

class Invoice(Resource):
    def get(self, id):
        try:
            invoice_model = InvoiceModel()
            data_resp = invoice_model.read_item(id)
            return data_resp, 200
        except HTTPException as e:
            response = CH.https_exception_response_format(e)
            return response
        except Exception:
            message = CH.internal_server_error_message()
            status = CH.internal_server_error_status()
            return message, status

    def put(self, id):
        try:
            invoice_model = InvoiceModel()
            params = parser.parse_args()
            invoice_model.update_item(id, params)
            return {}, 204
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
            invoice_model = InvoiceModel()
            params = parser.parse_args()
            invoice_model.create_item(params)
            return {}, 201
        except HTTPException as e:
            response = CH.https_exception_response_format(e)
            return response
        except Exception as e:
            message = CH.internal_server_error_message()
            status = CH.internal_server_error_status()
            return message, status

    def get(self):
        try:
            parser.add_argument("pageSize",       type=int, location="args")
            parser.add_argument("page",           type=int, location="args")
            parser.add_argument("order_by_desc",  type=str, location="args")
            parser.add_argument("order_by_asc",   type=str, location="args")

            invoice_model = InvoiceModel()
            params = parser.parse_args()
            data_resp = invoice_model.read_items(params)

            formmated_resp = CH.format_get_collection_response(data_resp, params)
            return formmated_resp, 200
        except HTTPException as e:
            response = CH.https_exception_response_format(e)
            return response
        except Exception:
            message = CH.internal_server_error_message()
            status = CH.internal_server_error_status()
            return message, status
