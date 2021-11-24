from .models import Author, Post, Follow, Friend, Comment, Like, Inbox, Node
from rest_framework import serializers


# serializer translates python object to json representation

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["type", "authorID", "url", "host",
                  "displayName", "github"]

    # Create and return a new Author instance, given the validated data.
    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    # allowing changes to displayName and github link
    def update(self, instance, validated_data):
        instance.displayName = validated_data.get(
            'displayName', instance.displayName)
        instance.github = validated_data.get('github', instance.github)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["type", "title", "postID", "source", "origin", "description", "contentType", "content",
                  "author", "categories", "count", "published", "visibility", "unlisted", "likes"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["type", "commentID", "post", "author", "content",
                  "contentType", "published"]
