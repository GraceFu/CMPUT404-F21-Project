from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Author
from api.serializers import AuthorSerializer
from api.utils import methods, author_not_found
from api.paginaion import CustomPagiantor
from api.utils import invalid_user_view

from django.shortcuts import redirect, render


""" put request data into instance 
example of an working data:

{
    "displayName": "the name",
    "github": "https://uofa-cmput404.github.io/"
}

"""
def all_authors_view(request):
    # Check the user is invalid in view
    if invalid_user_view(request):
        return redirect("login")

    content = {}
    content['all_authors'] = True

    return render(request, "all_authors.html", content)


class AuthorsViewSet(viewsets.GenericViewSet):

    permission_classes = [permissions.IsAuthenticated]

    """
    URL: api/authors/
    GET: retrieve all profiles on the server paginated
    """
    @action(methods=[methods.GET], detail=True)
    def list_all(self, request):

        queryset = Author.objects.all()
        pagination = CustomPagiantor()
        qs = pagination.paginate_queryset(queryset, request)
        serializer = AuthorSerializer(qs, many=True)
        res = {
            "type": "authors",
            "items": serializer.data
        }
        return Response(res, status=status.HTTP_200_OK)
    
    # Return the total number of authors
    @action(methods=[methods.GET], detail=True)
    def get_num_of_authors(self, request):
        total = Author.objects.all().count()
        res = {"total_item": total}
        return Response(res, status=status.HTTP_200_OK)


class ProfileViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated]

    """
    URL: api/author/{authorID}/
    GET: retrieve their profile
    POST: update profile
    """
    @action(methods=[methods.GET], detail=True)
    def retrieve(self, request, authorID):
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)

        author = Author.objects.get(authorID=authorID)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    @action(methods=[methods.POST], detail=True)
    def update(self, request, authorID):
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            instance = Author.objects.get(authorID=authorID)
            self.populate_author_data(serializer.data, instance)
            return Response(AuthorSerializer(instance).data, status=status.HTTP_200_OK)
        else:
            # return 400 response if the data was invalid/missing require field
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def populate_author_data(self, data, instance):
        instance.displayName = data["displayName"]
        instance.github = data["github"]
        instance.save()
