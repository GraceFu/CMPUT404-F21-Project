from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.contrib.auth.decorators import login_required

from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Author, Post, Like, Comment, visibility_type
from api.serializers import LikeSerializer
from api.utils import methods

# from Social_network.settings import HOSTNAME


class LikeViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated]

    @action(methods=[methods.GET], detail=True)
    def get_author_liked(self, request, authorID):
        """ list author liked, get list of of likes originating from this author"""
        if self.check_author_by_id(authorID) is False:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        author = Author.objects.filter(authorID=authorID)
        queryset = Like.objects.filter(author__in=author)
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=[methods.GET], detail=True)
    def get_post_likes(self, request, authorID, postID):
        """ list a post's likes """
        if self.check_post_by_id(postID) is False:
            return Response(status=status.HTTP_404_NOT_FOUND)

        post_url = request.get_host() + '/author/' + authorID + '/posts/' + postID
        queryset = Like.objects.filter(object=post_url)
        serializer = LikeSerializer(queryset, many=True)
        if serializer.is_valid:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=[methods.GET], detail=True)
    def get_comment_likes(self, request, authorID, postID, commentID):
        """ list a comment's likes """
        if self.check_comment_by_id(commentID) is False:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # TODO do we need to check post id ?

        comment_url = request.get_host() + '/author/' + authorID + \
            '/posts/' + postID + '/comments/' + commentID
        queryset = Like.objects.filter(object=comment_url)
        serializer = LikeSerializer(queryset, many=True)
        if serializer.is_valid:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=[methods.POST], detail=True)
    def like_object(self, request, authorID):
        """ like a post or comment """
        if self.check_author_by_id(authorID) is False:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            instance = Like()
            instance.author = Author.objects.get(authorID=authorID)
            self.populate_like_data(serializer.data, instance)
            return Response(LikeSerializer(instance).data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=[methods.DELETE], detail=True)
    def unlike_post(self, request):
        # TODO
        pass

    def check_author_by_id(self, authorID):
        """ check existence of an author """
        try:
            if Author.objects.get(authorID=authorID):
                return True
        except Author.DoesNotExist:
            return False

    def check_post_by_id(self, postID):
        """ check existence of a post """
        try:
            if Post.objects.get(postID=postID):
                return True
        except:
            return False

    def check_comment_by_id(self, commentID):
        """ check existence of a comment """
        try:
            if Comment.objects.get(commentID=commentID):
                return True
        except:
            return False

    def populate_post_data(self, data, instance):
        instance.author = data["author"]
        instance.summary = data["summary"]
        instance.object = data["object"]
        instance.save()
