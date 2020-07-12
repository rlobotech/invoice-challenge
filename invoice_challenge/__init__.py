from flask import Flask
from flask_restful import Resource, Api
from invoice_challenge.invoice_controller import Invoice, InvoiceAll

app = Flask(__name__)
api = Api(app)

api.add_resource(InvoiceAll, '/invoice')
api.add_resource(Invoice, '/invoice/<query>')
