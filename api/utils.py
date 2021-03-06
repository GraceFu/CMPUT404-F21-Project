import uuid

from api.models import Author, Post


def generate_id():
    return str(uuid.uuid4())


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
