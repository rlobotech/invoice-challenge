from invoice_challenge.basic_model import BasicModel

def format_query(params):
    asw = ""
    if(params["document"]):
        asw += f" AND document = {params['document']}"

    if(params["description"]):
        asw += f" AND description = {params['description']}"

    if(params["amount"]):
        asw += f" AND amount = '{params['amount']}'"

    if(params['order_by_desc'] or params['order_by_asc']):
        asw += " ORDER BY"
        if(params['order_by_desc']):
            split = params['order_by_desc'].split(",")
            for s in split:
                asw += f" {s} DESC,"
        if(params['order_by_asc']):
            split = params['order_by_asc'].split(",")
            for s in split:
                asw += f" {s} ASC,"
        asw = asw[:-1]

    limit = params['pageSize'] if params['pageSize'] else 100
    page = params['page'] if params['page'] else 0

    asw += f" LIMIT {limit} OFFSET {page * limit}"
    return asw

class InvoiceModel(BasicModel):
    def __init__(self):
        self._table_name = 'invoice'

    @property
    def table_name(self):
        return self._table_name

    def create_item(self, params):
        super().create_item(self.table_name, params)

    def read_items(self, params):
        extra_query = format_query(params)
        return super().read_items(self.table_name, extra_query)
    
    def read_item(self, id):
        return super().read_item(self.table_name, id)

    def update_item(self, id, params):
        super().update_item(self.table_name, id, params)

    def delete_item(self, id):
        super().delete_item(self.table_name, id)
