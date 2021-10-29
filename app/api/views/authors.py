from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Author
from api.serializers import AuthorSerializer
from api.utils import methods
from django.shortcuts import get_object_or_404


# Create your models here.
# https://www.django-rest-framework.org/api-guide/viewsets/

class AuthorViewSet(viewsets.ViewSet):

    """
    URL: ://service/authors/
    GET: retrieve all profiles on the server paginated
    page: how many pages
    size: how big is a page
    """

    @action(methods=[methods.POST], detail=True)
    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def delete(self, request, pk=None):
        pass
