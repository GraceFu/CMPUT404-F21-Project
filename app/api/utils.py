import uuid


def generate_id():
    return uuid.uuid4().hex


class methods:
    GET = 'get'
    POST = 'post'
    DELETE = 'delete'
    PUT = 'put'
