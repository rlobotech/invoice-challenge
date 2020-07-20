import invoice_challenge.basic_model as BasicModel
from test.database_connection import DatabaseConnection

class TestBasicModel(DatabaseConnection):
    def test_connection_to_db(self):
        basic_model = BasicModel.BasicModel()
        assert basic_model.connect_to_db()

    def test_read_items_from_a_generic_table(self):
        self.fill_database()
        basic_model = BasicModel.BasicModel()
        result = basic_model.read_items('invoice', '')
        expected = []
        assert result == expected
    
    def test_create_item(self):
        self.fill_database()
        basic_model = BasicModel.BasicModel()
        params = {
            "document": "test_document"
        }
        basic_model.create_item('invoice', params)
        result = basic_model.read_items('invoice', '')
        assert len(result) == 1
        assert result[0]['document'] == 'test_document'
        assert result[0]['description'] == None
        assert result[0]['amount'] == None
        assert result[0]['isActive'] == True    
    
    def test_update_item(self):
        self.fill_database()
        basic_model = BasicModel.BasicModel()
        params = {
            "document": "test_document"
        }
        basic_model.create_item('invoice', params)
        result = basic_model.read_items('invoice', '')
        params = {
            "document": "new_document",
            "description": 'new_description',
            "amount": 123.12
        }
        basic_model.update_item('invoice', result[0]['id'], params)
        result = basic_model.read_items('invoice', '')
        assert len(result) == 1
        assert result[0]['document'] == 'new_document'
        assert result[0]['description'] == 'new_description'
        assert result[0]['amount'] == 123.12
        assert result[0]['referenceMonth'] == None
        assert result[0]['isActive'] == True    
    
    def test_delete_item(self):
        self.fill_database()
        basic_model = BasicModel.BasicModel()
        params = {
            "document": "test_document"
        }
        basic_model.create_item('invoice', params)
        result = basic_model.read_items('invoice', '')
        basic_model.delete_item('invoice', result[0]['id'])
        result = basic_model.read_items('invoice', '')
        assert len(result) == 0
        assert result == []

    def test_update_item(self):
        self.fill_database()
        basic_model = BasicModel.BasicModel()
        params = {
            "document": "test_document"
        }
        basic_model.create_item('invoice', params)
        result = basic_model.read_items('invoice', '')
        result = basic_model.read_item('invoice', result[0]['id'])
        assert result['document'] == 'test_document'
        assert result['description'] == None
        assert result['amount'] == None
        assert result['referenceMonth'] == None
        assert result['isActive'] == True    
