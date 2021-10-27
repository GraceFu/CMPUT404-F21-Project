from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Author, Post
from api.serializers import PostSerializer
from api.utils import generate_id
from django.contrib.auth.decorators import login_required


# Create your views here.
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/

GET = 'GET'
POST = 'POST'
DELETE = 'DELETE'
PUT = 'PUT'

"""
URL: ://service/author/{AUTHOR_ID}/posts/{POST_ID}
GET: get the public post
POST: update the post (must be authenticated)
DELETE: remove the post
PUT: create a post with that post_id
"""


@api_view([GET, POST, DELETE, PUT])
def handle_existing_post(request, author_id, post_id):
    get_author_by_id(author_id)
    get_post_by_id(post_id)

    if request.method == GET:
        return get_post(request, author_id)
    elif request.method == POST:
        return update_post(request, author_id)
    elif request.method == DELETE:
        return delete_post(request, author_id)
    elif request.method == PUT:
        return create_post(request, author_id)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


"""
Creation URL ://service/author/{AUTHOR_ID}/posts/
GET: get recent posts of author (paginated)
POST: create a new post but generate a post_id
"""


@api_view([GET, POST])
def handle_creating_post(request, author_id):
    get_author_by_id(author_id)
    post_id = generate_id()

    if request.method == GET:
        return get_post(request, author_id, post_id)
    elif request.method == POST:
        return create_post(request, author_id, post_id)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# https://www.django-rest-framework.org/tutorial/3-class-based-views/#rewriting-our-api-using-class-based-views


def get_post(request, author_id, post_id):
    # TODO service
    pass


@login_required
def create_post(request, author_id, post_id):
    # TODO service
    post_serializer = PostSerializer(data=request.data)
    post_instance = post_serializer.save()


def delete_post(request, author_id, post_id):
    # TODO service
    pass


def update_post(request, author_id, post_id):
    # TODO service
    pass


def get_author_by_id(author_id):
    # check author authentication
    try:
        Author.objects.get(author_id=author_id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


def get_post_by_id(post_id):
    # check existence of a post
    try:
        Post.objects.get(post_id=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
