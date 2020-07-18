import datetime, decimal, uuid

def format_generic_query(params, query):
    if(params['order_by_desc'] or params['order_by_asc']):
        query += " ORDER BY"

        if(params['order_by_desc']):
            split = params['order_by_desc'].split(",")
            for s in split:
                query += f" {s} DESC,"

        if(params['order_by_asc']):
            split = params['order_by_asc'].split(",")
            for s in split:
                query += f" {s} ASC,"
        query = query[:-1]

    limit = params['pageSize'] if params['pageSize'] else 100
    page = params['page'] if params['page'] else 0

    query += f" LIMIT {limit} OFFSET {page * limit}"

    return query

def format_mysql_values_to_json(value):
    if type(value) == datetime.datetime:
        return str(value)
    if type(value) == decimal.Decimal:
        return float(value)
    if type(value) == bytearray:
        return str(uuid.UUID(bytes=bytes(value)))
    return value

def format_json_to_create(params):
    json_list = list(params.items())

    column_result = "(id, "
    values_result = "(UNHEX(REPLACE(UUID(), '-', '')), "
    for key, value in json_list:
        if(value == None):
            continue
        column_result += f"{key}, "
        values_result += f"'{value}', "

    column_result = column_result[:-2] + ")"
    values_result = values_result[:-2] + ")"
    return column_result, values_result

def format_json_to_update(params):
    json_list = list(params.items())

    result = ""
    for key, value in json_list:
        if(value == None):
            continue
        result += f"{key} = '{value}', "

    result = result[:-2]
    return result
