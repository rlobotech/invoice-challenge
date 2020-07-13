from invoice_challenge.basic_model import BasicModel

class InvoiceModel(BasicModel):
    def __init__(self):
        self._table_name = 'invoice'

    @property
    def table_name(self):
        return self._table_name

    def read_items(self):
        return super().read_items(self.table_name)
    
    def read_item(self, id):
        return super().read_item(self.table_name, id)

    # def create_item(self, hash):

    # def create_items(self, hash):

    # def update_item(self, uuid, hash):

    def delete_item(self, id):
        super().delete_item(self.table_name, id)

if __name__ == '__main__':
    invoice_model = InvoiceModel()
    print(invoice_model.read_items())
