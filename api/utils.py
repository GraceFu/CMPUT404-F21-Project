import uuid

from api.models import Author, Post, Node


def generate_id():
    return uuid.uuid4().hex


class methods:
    GET = 'get'
    POST = 'post'
    DELETE = 'delete'
    PUT = 'put'


def invalid_user_view(request):
    """ check the view of user """
    try:
        if request.user.is_authenticated and request.user.is_active and request.user.author:
            return False
    except:
        return True

    return True

def author_not_found(authorID):
    """ check existence of an author """
    try:
        if Author.objects.get(authorID=authorID):
            return False
    except Author.DoesNotExist:
        return True

def post_not_found(postID):
    """ check existence of a post """
    try:
        if Post.objects.get(postID=postID):
            return False
    except:
        return True

def node_not_found(hostURL):
    """ check existence of an author """
    try:
        if Node.objects.get(hostURL=hostURL):
            return False
    except Node.DoesNotExist:
        return True