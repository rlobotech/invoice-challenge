from invoice_challenge.basic_model import BasicModel
import invoice_challenge.helpers.model_helper as ModelHelper
import hashlib

def format_user_params(params):
    if(params["password"]):
        password = hashlib.sha1(params["password"].encode('utf-8'))
        params["password"] = password.hexdigest()

def format_user_query(params):
    query = ""
    if(params["email"]):
        query += f" AND email = {params['email']}"
    return ModelHelper.format_generic_query(params, query)

def format_user_find_query(params):
    query = f" AND email = '{params['email']}'"
    query += f" AND password = '{params['password']}'"
    return query

class UserModel(BasicModel):
    def __init__(self):
        self._table_name = "user"

    @property
    def table_name(self):
        return self._table_name

    def create_item(self, params):
        format_user_params(params)
        super().create_item(self.table_name, params)

    def read_items(self, params):
        query_addition = format_user_query(params)
        return super().read_items(self.table_name, query_addition)

    def read_item(self, params):
        format_user_params(params)
        query_addition = format_user_find_query(params)
        return super().read_items(self.table_name, query_addition)
