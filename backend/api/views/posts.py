from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.api.models import Author

# Create your views here.
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/

GET = 'GET'
POST = 'POST'
DELETE = 'DELETE'
PUT = 'PUT'

@api_view([GET, POST, DELETE, PUT])
def post(request, author_id):
    try:
        author = Author.objects.get(author_id=author_id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    if request.method == GET:
        get_post(request, author_id)
    elif request.method == POST:
        create_post(request, author_id)
    elif request.method == DELETE:
        delete_post(request, author_id)
    elif request.method == PUT:
        update_post(request, author_id)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    return render(request=request, template_name="post.html")



def get_post(request, author_id):
    #TODO
    pass

def create_post(request, author_id):
    #TODO
    pass

def delete_post(request, author_id):
    #TODO
    pass

def update_post(request, author_id):
    #TODO
    pass
