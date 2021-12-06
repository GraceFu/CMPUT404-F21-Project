from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication

from api.models import Author, Follower, Friend
from api.serializers import FollowSerializer
from api.utils import methods, author_not_found

from django.db.models import Q
from django.core import serializers

from datetime import datetime
import json

"""
auto-set fields: type, followee, follower, 
example of an working:
    {
    "followee": "AUTHOR_ID",
    "follower": "FOREIGN_AUTHOR_ID"
    }
"""


class FollowersViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    """
    URL: api/author/{AUTHOR_ID}/followees
    GET: get a list of authors who are their followees
    """
    @action(methods=[methods.GET], detail=True)
    def get_author_followees(self, request, authorID):
        """ get a list of followees of author """
        """ author is the follower, foreignAuthor is the followee """
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)
        followees = Follower.objects.filter(follower=authorID)
        serializer = FollowSerializer(followees, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    URL: api/author/{AUTHOR_ID}/followers
    GET: get a list of authors who are their followers
    """
    @action(methods=[methods.GET], detail=True)
    def get_author_followers(self, request, authorID):
        """ get a list of followers of author """
        """ author is the followee, foreignAuthor is the follower """
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)
        followers = Follower.objects.filter(followee=authorID)
        serializer = FollowSerializer(followers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    URL: api/author/{AUTHOR_ID}/friends
    GET: get a list of authors who are their friends
    """
    @action(methods=[methods.GET], detail=True)
    def get_author_friends(self, request, authorID):
        """ get a list of friends of author """
        """ author is the followee, foreignAuthor is the follower """
        """ also, author is the follower, foreignAuthor is the followee """
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)
        followers = Follower.objects.filter(followee=authorID)

        # Addition the displayName of the followers
        index = 0
        for item in followers:
            if author_not_found(item.follower.authorID):
                return Response(status=status.HTTP_404_NOT_FOUND)

            try:
                follow_back = Follower.objects.get(
                    Q(followee=item.follower.authorID) & Q(follower=authorID))
            except:
                followers = followers.exclude(follower=item.follower.authorID)

            index += 1

        serializer = FollowSerializer(followers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    URL: api/author/{AUTHOR_ID}/followers/{FOREIGN_AUTHOR_ID}
    DELETE: remove a follower
    PUT: Add a follower (must be authenticated)
    GET check if follower
    """
    @action(methods=[methods.GET], detail=True)
    def check_if_follower(self, request, authorID, foreignAuthorID):
        """ check foreignAuthor is a follower of author """
        """ author is the followee, foreignAuthor is the follower """
        if author_not_found(authorID):
            return Response(
                {
                    "detail": authorID + " is not found "
                },
                status=status.HTTP_404_NOT_FOUND)
        if author_not_found(foreignAuthorID):
            return Response(
                {
                    "detail": foreignAuthorID + " is not found "
                },
                status=status.HTTP_404_NOT_FOUND)

        try:
            followed = Follower.objects.filter(
                Q(followee=authorID) & Q(follower=foreignAuthorID))
            serializer = FollowSerializer(followed, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_200_OK)

    @action(methods=[methods.PUT], detail=True)
    def follow(self, request, authorID, foreignAuthorID):
        """ add a follower(foreignAuthor) to an author """
        """ author is the followee, foreignAuthor is the follower """
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)
        if author_not_found(foreignAuthorID):
            return Response(status=status.HTTP_404_NOT_FOUND)

        followee_author = Author.objects.get(authorID=authorID)
        follower_author = Author.objects.get(authorID=foreignAuthorID)

        try:
            instance = Follower()
            instance.followee = followee_author
            instance.follower = follower_author
            instance.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            friendRequest = Friend.objects.get((Q(actor=authorID) & Q(
                object=foreignAuthorID)) | (Q(actor=foreignAuthorID) & Q(object=authorID)))
            friendRequest.acceptance = True
            friendRequest.save()
        except:
            try:
                instance = Friend()
                instance.actor = followee_author
                instance.object = follower_author
                instance.summary = followee_author.displayName + \
                    " wants to follow " + follower_author.displayName
                instance.time = datetime.now().isoformat()
                instance.save()
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)

    @action(methods=[methods.DELETE], detail=True)
    def unfollow(self, request, authorID, foreignAuthorID):
        """ follower(foreignAuthor) unfollows author """
        """ author is the followee, foreignAuthor is the follower """
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)
        if author_not_found(foreignAuthorID):
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            Follower.objects.get(Q(followee=authorID) & Q(
                follower=foreignAuthorID)).delete()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            friendRequest = Friend.objects.get((Q(actor=authorID) & Q(
                object=foreignAuthorID)) | (Q(actor=foreignAuthorID) & Q(object=authorID)))
            if friendRequest.acceptance:
                friendRequest.acceptance = False
                friendRequest.save()
            else:
                friendRequest.delete()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)
