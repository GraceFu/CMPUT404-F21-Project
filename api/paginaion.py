from rest_framework import pagination
from rest_framework.response import Response


class CustomPagiantor(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        response = {}
        try:
            response["type"] = self.type
        except:
            pass
        response["items"] = data

        return Response(response)


class AuthorsPaginator(CustomPagiantor):
    type = "authors"
