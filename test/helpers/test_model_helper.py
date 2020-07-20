import invoice_challenge.helpers.model_helper as ModelHelper

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
