from rest_framework import status, exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from api.models import Author, Post
from api.serializers import PostSerializer, AuthorSerializer
from api.utils import generate_id
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import NewPostForm


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
    author = get_author_by_id(author_id)
    post = get_post_by_id(post_id)

    # check whether the author matches the post
    if post.author.author_id != author.author_id:
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == GET:
        return get_post(request, post)
    elif request.method == PUT:
        return create_post(request, author, post_id)
    elif request.method == DELETE:
        return delete_post(request, author_id)
    elif request.method == POST:
        return update_post(request, author_id)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


"""
Creation URL ://service/author/{AUTHOR_ID}/posts/
GET: get recent posts of author (paginated)
POST: create a new post but generate a post_id
"""


@api_view([GET, POST])
def handle_creating_post(request, author_id):
    author = get_author_by_id(author_id)
    post_id = generate_id()

    if request.method == GET:
        return get_posts(request, author_id)
    elif request.method == POST:
        return create_post(request, author_id, post_id)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# https://www.django-rest-framework.org/tutorial/3-class-based-views/#rewriting-our-api-using-class-based-views


def get_post(request, post):
    """ View a public post """
    # TODO: try it out
    if post.visibility != Post.VisibilityType.PUBLIC:
        return Response(status=status.HTTP_403_FORBIDDEN)

    serializer = PostSerializer(post)
    # return 400 response if the data was invalid.
    if serializer.is_valid(raise_exception=True):
        return render(request, 'post.html', serializer)


def create_post(request, author, post_id):
    """ create a post """
    # TODO service
    #post_serializer = PostSerializer(data=request.data)
    #post_instance = post_serializer.save()


def delete_post(request, author_id, post_id):
    # TODO service
    pass


def update_post(request, author_id, post_id):
    # TODO service
    pass


def get_posts(request, author_id):
    # TODO service
    pass


def get_author_by_id(author_id):
    """ check existence of an author """
    try:
        return Author.objects.get(author_id=author_id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def get_post_by_id(post_id):
    """ check existence of a post """
    try:
        return Post.objects.get(post_id=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
