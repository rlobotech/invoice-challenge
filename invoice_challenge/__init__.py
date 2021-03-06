from flask import Flask
from flask_restful import Resource, Api
from invoice_challenge.invoice_controller import Invoice, InvoiceCollection
from invoice_challenge.user_controller import User
from invoice_challenge.login_controller import Login
from os import environ

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
app.secret_key = environ.get("SECREAT_KEY")

api.add_resource(InvoiceCollection, "/invoices")
api.add_resource(Invoice, "/invoices/<id>")
api.add_resource(User, "/users")
api.add_resource(Login, "/login")
