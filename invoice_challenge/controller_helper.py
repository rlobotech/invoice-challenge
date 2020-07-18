from flask import json

def format_get_collection_response(data_resp, params):
    total = len(data_resp) if data_resp else 0
    page_size = params["pageSize"] if params["pageSize"] else 100
    page = params["page"] if params["page"] else 0

    formatted_response = {
        "data": data_resp,
        "total": total,
        "page_size": page_size,
        "page": page
    }
    return formatted_response

# Generic controller response messages and its status by exceptions
def internal_server_error_message():
    response = {
        "code": 500,
        "name": "Internal Server Error",
        "description": "Something went wrong"
    }
    return response

def internal_server_error_status():
    return 500

def https_exception_response_format(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
