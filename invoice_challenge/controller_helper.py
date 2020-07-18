# Exception that may raise from the model
class EntityNotFoundError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

def format_get_collection_response(data_resp, params):
    total = len(data_resp) if data_resp else 0
    page_size = params['pageSize'] if params['pageSize'] else 100
    page = params['page'] if params['page'] else 0

    formatted_response = {
        'data': data_resp,
        'total': total,
        'page_size': page_size,
        'page': page
    }
    return formatted_response

# Generic controller response messages and its status by exceptions
def internal_server_error_message():
    return {"message": "Something went wrong"}

def internal_server_error_status():
    return 500

def entity_not_found_error_message():
    return {"message": "Entity not found"}

def entity_not_found_error_status():
    return 404

def unauthorized_error_message():
    return {"message": "Invalid or outdated token"}

def unauthorized_error_status():
    return 401
