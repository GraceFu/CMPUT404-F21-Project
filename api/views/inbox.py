from django.db.models import query
from rest_framework import serializers, status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication

from api.models import Author, Like, Post, Follower, InboxObject
from api.serializers import AuthorSerializer, PostSerializer, InboxObjectSerializer
from api.utils import methods, generate_id, author_not_found, post_not_found
from api.paginaion import CustomPagiantor
from api.utils import invalid_user_view


from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required


""" put request data into instance 
auto-set fields: 
example of an working data:
{
}
"""


class InboxViewSet(viewsets.GenericViewSet):

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    serializer_class = InboxObjectSerializer
    queryset = {}

    @action(methods=[methods.GET], detail=True)
    def get_inbox_items(self, request, authorID):
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)

        author = Author.objects.get(authorID=authorID)
        queryset = InboxObject.objects.filter(author__in=author)
        pagination = CustomPagiantor()
        qs = pagination.paginate_queryset(queryset, request)
        serializers = InboxObjectSerializer(qs, many=True)

        res = {
            "type": "inbox",
            "author": author[0].url,
            "items": [io["object"] for io in serializers.data]
        }
        return Response(res, status=status.HTTP_200_OK)

    @action(methods=[methods.POST], detail=True)
    def add_item_to_inbox(self, request, authorID):
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InboxObjectSerializer(data=request.data)
        if serializer.is_valid():
            if request.data["type"] == "post":
                """ required: {"type", "postID" }"""
                postID = request.data["postID"]
                post = Post.objects.get(postID=postID)
                serialized_post = PostSerializer(post)

                instance = InboxObject(type="post")
                instance.author = Author.objects.get(authorID=authorID)
                instance.object = serialized_post.data
                instance.save()

            elif request.data["type"] == "like":
                """ required: {"type", "object", "actor"} """
                actor = Author.objects.get(authorID=request.data["actor"])
                obj_type = "comment" if (
                    "comment" in request.data["object"]) else "post"

                like = {
                    "type": "like",
                    "author": AuthorSerializer(actor).data,
                    "summary": actor.displayName + " likes your " + obj_type,
                    "object": request.data["object"]
                }

                instance = InboxObject(type="like")
                instance.author = Author.objects.get(authorID=authorID)
                instance.object = like
                instance.save()

            elif request.data["type"] == "follow":
                """ required: {"type", "follower"} """
                followee = Author.objects.get(authorID=authorID)
                follower = Author.objects.get(
                    authorID=request.data["follower"])

                req = {
                    "type": "follow",
                    "summary": follower.displayName + " wants to follow " + followee.displayName,
                    "actor": AuthorSerializer(follower).data,
                    "object": AuthorSerializer(followee).data
                }

                instance = InboxObject(type="follow")
                instance.author = followee
                instance.object = req
                instance.save()

            return Response(InboxObjectSerializer(instance).data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # Return the total number of inbox items
    @action(methods=[methods.GET], detail=True)
    def get_num_of_inbox_items(self, request, authorID):
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)

        author = Author.objects.get(authorID=authorID)
        count = InboxObject.objects.filter(author=author).count()
        res = {"total_item": count}
        return Response(res, status=status.HTTP_200_OK)


def my_inbox_view(request):
    # Check the user is invalid in view
    if invalid_user_view(request):
        return redirect("login")

    content = {}
    content['my_inbox_page'] = True

    return render(request, "inbox.html", content)
