from flask import Flask
from flask_restful import Resource, Api
from invoice_challenge.invoice_controller import Invoice, InvoiceCollection

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

# It seems that flask_restful was not build to work with filters.
# In order to work with filters I will add a resource specific for filters.
api.add_resource(InvoiceCollection, '/invoices')
api.add_resource(Invoice, '/invoices/<id>')
