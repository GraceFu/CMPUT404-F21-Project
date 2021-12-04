from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication

from api.models import Author, Post, Comment
from api.serializers import CommentSerializer
from api.utils import methods, generate_id, author_not_found, post_not_found
from api.paginaion import CustomPagiantor


from datetime import datetime

""" put request data into instance 
auto-set fields: type, commentID, post, author

example of an working data:

{
    "content": "comment content",
    "contentType": "text/plain"
}

"""


class CommentViewSet(viewsets.GenericViewSet):

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    serializer_class = CommentSerializer

    @action(methods=[methods.GET], detail=True)
    def get_post_comment(self, request, authorID, postID):
        if author_not_found(authorID) or post_not_found(postID):
            return Response(status=status.HTTP_404_NOT_FOUND)

        # get all comments that is owned by the post
        post = Post.objects.filter(postID=postID)
        queryset = Comment.objects.filter(post__in=post).order_by('-published')
        pagination = CustomPagiantor()
        qs = pagination.paginate_queryset(queryset, request)
        serializer = CommentSerializer(qs, many=True)
        res = {
            "type": "comments",
            "page": request.GET.get("page"),
            "size": request.GET.get("size"),
            # TODO
            # "post":
            # "id":
            "comments": serializer.data
        }
        return Response(res, status=status.HTTP_200_OK)

    @action(methods=[methods.POST], detail=True)
    def create_comment_with_new_id(self, request, authorID, postID):
        if author_not_found(authorID) or post_not_found(postID):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            instance = Comment(commentID=generate_id())
            instance.author = Author.objects.get(authorID=authorID)
            instance.post = Post.objects.get(postID=postID)
            self.populate_comment_data(serializer.data, instance)
            return Response(CommentSerializer(instance).data, status=status.HTTP_200_OK)
        else:
            # return 400 response if the data was invalid/missing require field
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def populate_comment_data(self, data, instance):
        instance.content = data["content"]
        instance.contentType = data["contentType"]
        instance.published = datetime.now().isoformat()
        instance.save()
