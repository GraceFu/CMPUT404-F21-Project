from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Author, Post
from api.serializers import AuthorSerializer
from api.utils import methods
from django.shortcuts import get_object_or_404


# Create your models here.
# https://www.django-rest-framework.org/api-guide/viewsets/

class AuthorsViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated]

    """
    URL: ://service/authors/
    GET: retrieve all profiles on the server paginated
    page: how many pages
    size: how big is a page
    """

    @action(methods=[methods.GET], detail=True)
    def list_all(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated]

    """
    URL: ://service/author/{authorID}/
    GET: retrieve their profile
    POST: update profile
    """

    @action(methods=[methods.GET], detail=True)
    def retrieve(self, request, authorID):
        if not self.check_author_by_id(authorID):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        author = Author.objects.get(authorID=authorID)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    @action(methods=[methods.POST], detail=True)
    def update(self, request, authorID):
        if not self.check_author_by_id(authorID):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            instance = Author.objects.get(authorID=authorID)
            self.populate_author_data(serializer.data, instance)
            return Response(AuthorSerializer(instance).data, status=status.HTTP_200_OK)
        else:
            # return 400 response if the data was invalid/missing require field
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def populate_author_data(self, data, instance):
        """ put request data into instance 

        example of an working data:

        {
        "displayName": "the name",
        "github": "https://uofa-cmput404.github.io/"
        }

        """

        #instance.type = data["type"]
        instance.displayName = data["displayName"]
        # instance.host = data["host"]
        instance.github = data["github"]

    def check_author_by_id(self, authorID):
        """ check existence of an author """
        try:
            if Author.objects.get(authorID=authorID):
                return True
        except Author.DoesNotExist:
            return False
