from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from invoice_challenge.invoice_model import InvoiceModel
import invoice_challenge.helpers.controller_helper as CH
import invoice_challenge.helpers.exception_helper as EH

# RequestParser serve as an allowlist params (old whitelist params).
def invoice_request_parser():
    parser = RequestParser(bundle_errors=True)
    parser.add_argument("document",       type=str,   help="Please enter a valid String as a document")
    parser.add_argument("description",    type=str,   help="Please enter a valid String as a description")
    parser.add_argument("amount",         type=float, help="Please enter valid Decimal as an amount")
    parser.add_argument("referenceMonth", type=str,   help="Please enter a valid Datetime as a referenceMonth")
    parser.add_argument("referenceYear",  type=int,   help="Please enter valid Integer as a referenceYear")
    return parser

class Invoice(Resource):
    @EH.exception_handler
    def get(self, id):
        CH.check_authentication_token()

        invoice_model = InvoiceModel()
        data_resp = invoice_model.read_item(id)
        return data_resp, 200

    @EH.exception_handler
    def put(self, id):
        CH.check_authentication_token()

        params = invoice_request_parser().parse_args()
        invoice_model = InvoiceModel()
        invoice_model.update_item(id, params)
        return {}, 204

    @EH.exception_handler
    def delete(self, id):
        CH.check_authentication_token()

        invoice_model = InvoiceModel()
        invoice_model.delete_item(id)
        return {}, 204

class InvoiceCollection(Resource):
    @EH.exception_handler
    def post(self):
        CH.check_authentication_token()

        params = invoice_request_parser().parse_args()
        invoice_model = InvoiceModel()
        invoice_model.create_item(params)
        return {}, 201

    @EH.exception_handler
    def get(self):
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
