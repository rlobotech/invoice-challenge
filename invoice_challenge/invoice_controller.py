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
    def get(self, id):
        invoice_model = InvoiceModel()
        data_resp = invoice_model.read_item(id)
        return data_resp[0], 200

    def delete(self, id):
        invoice_model = InvoiceModel()
        data_resp = invoice_model.read_item(id)
        return '', 204

class InvoiceCollection(Resource):
    def get(self):
        invoice_model = InvoiceModel()
        data_resp = invoice_model.read_items()
        resp = format_response(data_resp)
        return resp, 200

class InvoiceCollectionFilterable(Resource):
    def get(self, query):
        invoice_model = InvoiceModel()
        data_resp = invoice_model.read_items()
        resp = format_response(data_resp)
        return resp, 200