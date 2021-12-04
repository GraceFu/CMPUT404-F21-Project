from django.db.models import query
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication

from api.models import Author, Like, Post, Follower, Inbox
from api.serializers import InboxSerializer
from api.utils import methods, generate_id, author_not_found, post_not_found
from api.paginaion import CustomPagiantor

from datetime import datetime

""" put request data into instance 
auto-set fields: 

example of an working data:

{

}

"""
class InboxViewSet(viewsets.GenericViewSet):

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    serializer_class = InboxSerializer
    queryset = {}

    @action(methods=[methods.GET], detail=True)
    def get_inbox_items(self, request, authorID):
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)

        # # get all comments that is owned by the post
        # items = Inbox.objects.all().order_by('-published')
        # pagination = CustomPagiantor()
        # qs = pagination.paginate_queryset(items, request)
        # serializer = InboxSerializer(qs, many=True)
        # res = {
        #     "type": "inbox",
        #     # "page": request.GET.get("page"),
        #     # "size": request.GET.get("size"),
        #     "items": [serializer.data]
        # }
        # return Response(res, status=status.HTTP_200_OK)

        queryset = Inbox.objects.filter(author=authorID).order_by('-published')
        
        serializer = InboxSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    @action(methods=[methods.POST], detail=True)
    def add_item_to_inbox(self, request):

        print("---------\n",request)
        type = request["type"]

        authorID = request["author"]
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InboxSerializer(data=request)
        if serializer.is_valid():
            instance = Inbox(inboxID=generate_id())
            instance.author = Author.objects.get(authorID=authorID)
            instance.published = datetime.now().isoformat()
            if type == "post":
                instance.posts = request
            elif type == "follow":
                instance.requests = request
            elif type == "like":
                instance.likes = request
            instance.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
