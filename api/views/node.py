from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Node
from api.serializers import NodeSerializer
from api.utils import methods, node_not_found


class CommentViewSet(viewsets.ViewSet):

    @action(methods=[methods.GET], detail=True)
    def get_node(self, request, hostURL):
        if node_not_found(hostURL):
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        node = Node.objects.all()
        serializer = NodeSerializer(node)
        return Response(serializer.data, status=status.HTTP_200_OK)