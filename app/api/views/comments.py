from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication

from api.models import Author, Post, visibility_type, Comment
from api.serializers import CommentSerializer
from api.utils import methods, generate_id, invalid_user_view
from api.forms import NewCommentForm

from Social_network.settings import HOSTNAME

from datetime import datetime

# References
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
# https://www.django-rest-framework.org/api-guide/viewsets/
# https://www.django-rest-framework.org/tutorial/3-class-based-views/#rewriting-our-api-using-class-based-views


class CommentAPISet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    @action(methods=[methods.GET], detail=True)
    def get_post_comment(self, request, authorID, postID):
        # return 401 response if the author does not exists
        if not self.check_author_by_id(authorID) or not self.check_post_by_id(authorID):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        # get all comments that is owned by the post
        post = Post.objects.get(postID=postID)
        author = Comment.objects.filter(post__in=post).order_by('-published')
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=[methods.POST], detail=True)
    def create_comment_with_new_id(self, request, authorID, postID):
        # return 401 response if the author does not exists
        if not self.check_author_by_id(authorID) or not self.check_post_by_id(authorID):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        # Check the comment is vaild or not
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            instance = Comment(commentID=generate_id())
            instance.author = Author.objects.get(authorID=authorID)
            instance.post = Post.objects.get(postID=postID)
            self.populate_post_data(serializer.data, instance)
            return Response(CommentSerializer(instance).data, status=status.HTTP_200_OK)
        else:
            # return 400 response if the data was invalid/missing require field
            return Response(status=status.HTTP_400_BAD_REQUEST)


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

    def populate_comment_data(self, data, instance):
        """ put request data into instance 
        auto-set fields: commentID, type, visibility, unlisted, count

        example of an working data:

        {
        "content": content,
        "contentType": "text/plain",
        "published": time.object
        }

        """

        instance.content = data["content"]
        instance.contentType = data["contentType"]
        instance.published = datetime.now().isoformat()
        instance.save()