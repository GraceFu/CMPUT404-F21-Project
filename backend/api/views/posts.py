from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Author, Post, visibilityType
from api.serializers import PostSerializer
from api.utils import generate_id, methods
from Social_network.settings import HOSTNAME
from django.contrib.auth.decorators import login_required
from datetime import datetime

# References
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
# https://www.django-rest-framework.org/api-guide/viewsets/
# https://www.django-rest-framework.org/tutorial/3-class-based-views/#rewriting-our-api-using-class-based-views


class post_view_set(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated]
    """
    Creation URL ://service/author/{AUTHOR_ID}/posts/
    GET: get recent posts of author (paginated)
    POST: create a new post but generate a post_id
    """
    @action(methods=[methods.GET], detail=True)
    def get_author_posts(self, request, author_id):
        """ list author posts """
        if self.check_author_by_id(author_id) is False:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        queryset = Post.objects.filter(
            author_id=author_id).order_by('-published_date')
        serializer = PostSerializer(queryset, many=True)
        if serializer.is_valid:
            return Response(serializer.data)
        else:
            # return 400 response if the data was invalid.
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=[methods.POST], detail=True)
    def create_post_without_post_id(self, request, author_id):
        """ create a post """
        if self.check_author_by_id(author_id) is False:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        post_id = generate_id()
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            instance = Post(post_id=post_id)
            self.populate_post_data(serializer.data, instance)
            return Response(PostSerializer(instance).data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    """
    URL: ://service/author/{AUTHOR_ID}/posts/{POST_ID}
    GET: get the public post
    POST: update the post (must be authenticated)
    DELETE: remove the post
    PUT: create a post with that post_id
    """
    @action(methods=[methods.GET], detail=True)
    def get_public_posts(self):
        """ list public postS """
        # sort public post from the most recent to the oldest
        queryset = Post.objects.filter(
            visibility=visibilityType.PUBLIC).order_by('-published_date')
        serializer = self.get_serializer(queryset, many=True)

        if serializer.is_valid:
            return Response(serializer.data)
        else:
            # return 400 response if the data was invalid.
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def create_post_with_post_id(self, request):
        # TODO
        pass

    def delete_post(self, request, post_id):
        # TODO service
        pass

    def update_post(self, request, post_id):
        # TODO service
        pass

    def check_author_by_id(self, author_id):
        """ check existence of an author """
        try:
            if Author.objects.get(author_id=author_id):
                return True
        except Author.DoesNotExist:
            return False

    def check_post_by_id(self, post_id):
        """ check existence of a post """
        try:
            if Post.objects.get(post_id=post_id):
                return True
        except Post.DoesNotExist:
            return False

    def populate_post_data(self, post_id, author_id, data, instance):
        """ put request data into instance """
        instance.title = data["title"]
        instance.post_id = post_id
        instance.source = data["source"]  # TODO make it to url
        instance.origin_post = data["origin"]  # TODO make it to url
        instance.description = data["description"]
        instance.content_type = data["contentType"]
        instance.content = data["content"]
        instance.author = author_id
        instance.categories = data["categories"]
        # total number of comments for this post
        instance.count = len(data["comments"])
        instance.published_date = datetime.now().isoformat()
        instance.visibility = data["visibility"]
        instance.unlisted = data["unlisted"]
        instance.save()
