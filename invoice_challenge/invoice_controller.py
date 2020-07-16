from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from invoice_challenge.invoice_model import InvoiceModel
import datetime, decimal

# Request parser serve as an allowed params aswell.
parser = RequestParser(bundle_errors=True)
parser.add_argument("document",       type=str,   help="Please enter a valid String as a document")
parser.add_argument("description",    type=str,   help="Please enter a valid String as a description")
parser.add_argument("amount",         type=float, help="Please enter valid Decimal as an amount")
parser.add_argument("referenceMonth", type=str,   help="Please enter a valid Datetime as a referenceMonth")
parser.add_argument("referenceYear",  type=int,   help="Please enter valid Integer as a referenceYear")

def format_response(data, total=0, page_size=100, page=0):
    formatted_response = {
        'data': data,
        'total': total,
        'page_size': page_size,
        'page': page
    }
    return formatted_response

class Invoice(Resource):
    def get(self, id):
        invoice_model = InvoiceModel()
        data_resp = invoice_model.read_item(id)
        return data_resp[0], 200

    def put(self, id):
        invoice_model = InvoiceModel()
        params = parser.parse_args()
        invoice_model.update_item(id, params)
        return '', 204

    def delete(self, id):
        invoice_model = InvoiceModel()
        invoice_model.delete_item(id)
        return '', 204

class InvoiceCollection(Resource):
    def post(self):
      invoice_model = InvoiceModel()
      params = parser.parse_args()
      invoice_model.create_item(params)
      return '', 201

    def get(self):
        parser.add_argument('pageSize',       type=int,   location='args')
        parser.add_argument('page',           type=int,   location='args')
        parser.add_argument('order_by_desc',  type=str,   location='args')
        parser.add_argument('order_by_asc',   type=str,   location='args')

        invoice_model = InvoiceModel()
        params = parser.parse_args()
        data_resp = invoice_model.read_items(params)

        total = len(data_resp)
        page_size = params['pageSize'] if params['pageSize'] else 100
        page = params['page'] if params['page'] else 0
        resp = format_response(data_resp, total, page_size, page)

        return resp, 200
