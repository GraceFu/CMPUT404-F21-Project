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

    permission_classes = [permissions.IsAuthenticated]

    """
    URL: ://service/authors/
    GET: retrieve all profiles on the server paginated
    page: how many pages
    size: how big is a page

    URL: ://service/author/{AUTHOR_ID}/
    GET: retrieve their profile
    POST: update profile
    """

    @action(methods=[methods.GET], detail=True)
    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=[methods.GET], detail=True)
    def retrieve(self, request, author_id):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, authorID=author_id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    @action(methods=[methods.POST], detail=True)
    def update(self, request, author_id):

        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            instance = Author(authorID=author_id)
            self.populate_post_data(serializer.data, instance)
            return Response(AuthorSerializer(instance).data, status=status.HTTP_200_OK)
        else:
            # return 400 response if the data was invalid/missing require field
            return Response(status=status.HTTP_400_BAD_REQUEST)
