from basic_model import BasicModel

class InvoiceModel(BasicModel):
    def __init__(self):
        self._table_name = 'invoice'

    @property
    def item_type(self):
        return self._table_name

    def read_items(self):
        return super().read_items(self.item_type)
    
    # def read_item(self, uuid):

    # def create_item(self, hash):

    # def create_items(self, hash):

    # def update_item(self, uuid, hash):

    # def delete_item(self, uuid):

if __name__ == '__main__':
    invoice_model = InvoiceModel()
    print(invoice_model.read_items())
