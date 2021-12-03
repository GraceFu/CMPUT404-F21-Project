from .models import Author, Post, Follower, Friend, Comment, Like, Inbox, Node
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
        fields = ["type", "title", "postID", "url", "author", "source", "origin", "description", "contentType", "content",
                  "categories", "count", "published", "visibility", "unlisted", "likes"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["type", "commentID", "content",
                  "author", "post", "contentType"]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["type", "author", "summary", "object"]


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ["type", "followee", "follower"]


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ["type", "actor", "object", "summary", "time"]
