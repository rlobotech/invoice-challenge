import invoice_challenge.helpers.model_helper as ModelHelper
import datetime, decimal, uuid

def test_should_succeed_format_generic_query():
    query = ""
    params = {
        "order_by_desc": "document",
        "order_by_asc": None,
        "pageSize": None,
        "page": None,
    }
    result = ModelHelper.format_generic_query(params, query)
    expected = " ORDER BY document DESC LIMIT 100 OFFSET 0"
    assert result == expected

def test_should_succeed_format_generic_query_without_order_by_desc():
    query = ""
    params = {
        "order_by_asc": None,
        "pageSize": None,
        "page": None,
    }
    result = ModelHelper.format_generic_query(params, query)
    expected = " LIMIT 100 OFFSET 0"
    assert result == expected

def test_should_succeed_format_generic_query_with_limit_and_page():
    query = ""
    params = {
        "order_by_asc": 'amount',
        "pageSize": 50,
        "page": 1,
    }
    result = ModelHelper.format_generic_query(params, query)
    expected = " ORDER BY amount ASC LIMIT 50 OFFSET 50"
    assert result == expected

def test_should_succeed_format_generic_query_all_params():
    query = "WHERE isActive = true"
    params = {
        "order_by_asc": 'amount',
        "order_by_desc": 'description,document',
        "pageSize": 50,
        "page": 1,
    }
    result = ModelHelper.format_generic_query(params, query)
    expected = "WHERE isActive = true ORDER BY description DESC, document DESC, amount ASC LIMIT 50 OFFSET 50"
    assert result == expected

def test_should_succeed_format_mysql_datetime_to_json():
    datetime_value = datetime.datetime.now()
    result = ModelHelper.format_mysql_values_to_json(datetime_value)
    expected = str(datetime_value)
    assert result == expected

def test_should_succeed_format_mysql_decimal_to_json():
    uuid_value = uuid.uuid1()
    result = ModelHelper.format_mysql_values_to_json(bytearray(uuid_value.bytes))
    assert result == str(uuid_value)

def test_should_succeed_format_mysql_any_other_type_to_json():
    value = 'any_other_type'
    result = ModelHelper.format_mysql_values_to_json(value)
    assert result == value

def test_should_succeed_format_json_to_create():
    params = {
        "document": "new_document",
        "amount": 123
    }
    keys, values = ModelHelper.format_json_to_create(params)
    expected_keys = "(id, document, amount)" 
    expected_values = "(UNHEX(REPLACE(UUID(), '-', '')), 'new_document', '123')"
    assert keys == expected_keys
    assert values == expected_values

def test_should_succeed_format_json_to_update():
    params = {
        "document": "new_document",
        "amount": 123,
        "description": "new_description"
    }
    result = ModelHelper.format_json_to_update(params)
    expected = "document = 'new_document', amount = '123', description = 'new_description'"
    assert result == expected

def test_should_succeed_format_read_response_to_json():
    columns_description = [["document"], ["amount"], ["description"]]
    rows_data = [
        ["new_document", 123, "new_description"],
        ["another_document", 444.12, None]
    ]
    result = ModelHelper.format_read_response_to_json(rows_data, columns_description)
    expected = [
        {
            "document": "new_document",
            "amount": 123,
            "description": "new_description"
        },
        {
            "document": "another_document",
            "amount": 444.12,
            "description": None
        }
    ]
    assert result == expected
