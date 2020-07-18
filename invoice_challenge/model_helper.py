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
