from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication

from api.models import Author, Follower
from api.serializers import FollowSerializer
from api.utils import methods, author_not_found

from django.db.models import Q


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

        # Addition the displayName of the followees
        index = 0
        for item in serializer.data:
            serializer.data[index]["followeeDisplayName"] = Author.objects.get(authorID=item["followee"]).displayName
            index += 1
        
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

        # Addition the displayName of the followers
        index = 0
        for item in serializer.data:
            serializer.data[index]["followerDisplayName"] = Author.objects.get(authorID=item["follower"]).displayName
            index += 1
        
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
                follow_back = Follower.objects.get(Q(followee=item.follower.authorID) & Q(follower=authorID))
            except:
                followers = followers.exclude(follower=item.follower.authorID)

            index += 1

        serializer = FollowSerializer(followers, many=True)
        # Addition the displayName of the followers
        index = 0
        for item in serializer.data:
            serializer.data[index]["followerDisplayName"] = Author.objects.get(authorID=item["follower"]).displayName
            index += 1
        
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
            followed = Follower.objects.get(Q(followee=authorID) & Q(follower=foreignAuthorID))
            serializer = FollowSerializer(followed, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(
                {
                    "detail": foreignAuthorID + " is not a follower of " + authorID
                }, 
                status=status.HTTP_200_OK)

    @action(methods=[methods.PUT], detail=True)
    def follow(self, request, authorID, foreignAuthorID):
        """ add a follower(foreignAuthor) to an author """
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

        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            instance = Follower()
            instance.followee = Author.objects.get(authorID=authorID)
            instance.follower = Author.objects.get(authorID=foreignAuthorID)
            instance.save()
            return Response(
                {
                    "detail": foreignAuthorID + " is now following " + authorID
                }, 
                status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    "detail": foreignAuthorID + " is already a follower of " + authorID
                }, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=[methods.DELETE], detail=True)
    def unfollow(self, request, authorID, foreignAuthorID):
        """ follower(foreignAuthor) unfollows author """
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
            Follower.objects.get(Q(followee=authorID) & Q(follower=foreignAuthorID)).delete()
            return Response(
                {
                    "detail": foreignAuthorID + " no longer follows " + authorID
                }, 
                status=status.HTTP_200_OK)
        except:
            return Response(
                {
                    "detail": foreignAuthorID + " is not a follower of " + authorID
                }, 
                status=status.HTTP_200_OK)
