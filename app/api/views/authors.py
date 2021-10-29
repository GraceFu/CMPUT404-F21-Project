from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Author
from api.serializers import AuthorSerializer
from api.utils import methods

# Create your models here.


class author_view_set(viewsets.ViewSet):
    @action(methods=[methods.POST], detail=True)
    def update(self, request, authorID):
        pass
