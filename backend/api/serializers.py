from .models import Author, Post, Follow, Friend, Comment, Like, Inbox
from rest_framework import serializers


# serializer translates python object to json representation
# https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["type", "id", "url", "host",
                  "displayName", "github", "profileImage"]

    # Create and return a new Author instance, given the validated data.
    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    # allowing changes to displayName and github link
    def update(self, instance, validated_data):
        instance.displayName = validated_data.get(
            'display_name', instance.displayName)
        instance.github = validated_data.get('github', instance.github)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["type", "title", "id", "source", "origin", "description", "contentType", "content",
                  "author", "categories", "count", "comments", "published", "visibility", "unlisted"]

# TODO add more serializers
