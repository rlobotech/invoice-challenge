from invoice_challenge.basic_model import BasicModel
import invoice_challenge.helpers.model_helper as ModelHelper

def format_invoice_query(params):
    query = ""
    if(params["document"]):
        query += f" AND document = {params['document']}"
    if(params["description"]):
        query += f" AND description = {params['description']}"
    if(params["amount"]):
        query += f" AND amount = '{params['amount']}'"
    return ModelHelper.format_generic_query(params, query)

class InvoiceModel(BasicModel):
    def __init__(self):
        self._table_name = "invoice"

    @property
    def table_name(self):
        return self._table_name

    def create_item(self, params):
        super().create_item(self.table_name, params)

    def read_items(self, params):
        query_addition = format_invoice_query(params)
        return super().read_items(self.table_name, query_addition)
    
    def read_item(self, id):
        return super().read_item(self.table_name, id)

    def update_item(self, id, params):
        super().update_item(self.table_name, id, params)

    def delete_item(self, id):
        super().delete_item(self.table_name, id)
