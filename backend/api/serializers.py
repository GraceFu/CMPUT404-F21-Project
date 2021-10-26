###needs work!!


from models import author, post, signupRequest, comment, like, follower, friend, inbox
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core import serializers as serialize
import json



# serializer for post model into json representation
class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = post.Post
    fields = ['title', 'description', 'content', 'contentType', 'visibility', 'categories', 'author_id', 'unlisted']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
    
class SignupSerializer(serializers.ModelSerializer):
  class Meta:
    model = signupRequest.Signup_Request
    fields = ['username','password', 'displayName','github', 'host']

# COMMENT SERIALIZER
class CommentSerializer(serializers.ModelSerializer):
   
    # This method is called on .save(), it allows for addition of extra fields in a encapsulated
    # fashion so the details are not evident on the service end
    def create(self, validated_data):
        comment_ = comment.Comment(**validated_data,
                                   post_id=self.context.get('post_id'),
                                   C_author_id=self.context.get('request').user)
        url = f"{self.context.get('request').build_absolute_uri()}/{comment_.comment_id}"
        comment_.url = url
        comment_.save()
        return comment_

    class Meta:
        model = comment.Comment
        # Serializes every field in the model
        fields = ['content', 'contentType']

# LIKE SERIALIZER
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = like.Like
        fields = ['post_id', 'comment_id', 'L_author_id', 'like_type', 'url']

    

# serializer for author model
class AuthorSerializer(serializers.ModelSerializer):
  type = serializers.CharField(default='author')
  id = serializers.URLField(source='url')
  class Meta:
    model = author.Author
    fields = ['type', 'id', 'host', 'displayName', 'url', 'github']

  # only allowing change displayName and github link
  def update(self, instance, validated_data):
    instance.displayName = validated_data.get('displayName', instance.displayName)
    instance.github = validated_data.get('github', instance.github)
    instance.save()
    return instance


# serializer for follower model
class FollowerSerializer(serializers.ModelSerializer):
  class Meta:
    model = follower.Follower
    fields = ['followee', 'follower_url']

# serializer for friend model
class FriendSerializer(serializers.ModelSerializer):
  class Meta:
    model = friend.Friend
    fields = ['author', 'friend_url']

# serializer for inbox model
class InboxSerializer(serializers.ModelSerializer):
  class Meta:
    model = inbox.Inbox
    fields = ['author_id', 'messageType', 'items']