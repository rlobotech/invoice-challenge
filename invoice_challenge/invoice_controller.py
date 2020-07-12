from flask_restful import Resource
from invoice_challenge.invoice_model import InvoiceModel

def format_response(data, total=0, page_size=100, page=0):
    formatted_response = {
        'data': data,
        'total': total,
        'page_size': page_size,
        'page': page
    }
    return formatted_response

class Invoice(Resource):
    def get(self, query):
        return {'message': 'success', 'data': 'invoice'}, 200

class InvoiceAll(Resource):
    def get(self):
        invoice_model = InvoiceModel()
        data_resp = invoice_model.read_items()
        resp = format_response(data_resp)
        return resp, 200
