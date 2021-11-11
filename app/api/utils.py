from django.shortcuts import redirect

import uuid


def generate_id():
    return uuid.uuid4().hex


class methods:
    GET = 'get'
    POST = 'post'
    DELETE = 'delete'
    PUT = 'put'


# Check the view of user
def invalid_user_view(request):
    try:
        if request.user.is_authenticated and request.user.is_active and request.user.author:
            return False
    except:
        return True

    return True
