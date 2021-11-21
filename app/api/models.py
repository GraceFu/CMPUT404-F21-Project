from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.fields import related
from Social_network.settings import HOSTNAME
from django.utils.translation import activate
from django import forms

# Create your models here.
# https://docs.djangoproject.com/en/3.2/topics/db/models/
# https://docs.djangoproject.com/en/3.2/ref/models/fields/#choices


# Defined constant/enum fields
class visibility_type(models.TextChoices):
    PUBLIC = "PUBLIC"
    FRIENDS = "FRIENDS"


class content_type(models.TextChoices):
    MARKDOWN = "text/markdown"
    PLAIN = "text/plain"
    APPLICATION = "application/base64"
    PNG = "image/png;base64"
    JPEG = "image/jpeg;base64"


######### Author #########
class Author(models.Model):
    type = models.CharField(default="author", max_length=100)
    authorID = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    displayName = models.CharField(max_length=100, default="Someone")
    host = models.CharField(default=HOSTNAME, max_length=500)
    url = models.URLField(null=True, blank=True, editable=False)
    github = models.URLField(null=True, blank=True)
    # profile_picture = models.URLField(null=True, blank=True)
    # TODO set profile picture properly


######### Follow #########
class Follow(models.Model):
    type = models.CharField(default="followers", max_length=100)
    requestID = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    # follow request from user
    followee = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="followee")
    # follow request to user, person to be follow
    follower = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="follower")
    time = models.DateTimeField(auto_now_add=True)
    acceptance = models.BooleanField(default=False)


######### Friend #########
class Friend(models.Model):
    type = models.CharField(default="friend", max_length=100)
    requestID = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    # friend request from user
    actor = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="actor")
    # friend request to user
    object = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="object")
    summary = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    acceptance = models.BooleanField(default=False)


# Post ######### potentially missing comment field and list of comment field
class Post(models.Model):
    type = models.CharField(default="post", max_length=100)
    postID = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=100)
    source = models.URLField(null=True, blank=True)
    origin = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    contentType = models.CharField(
        max_length=100, default=content_type.PLAIN, null=True, blank=True)
    content = models.CharField(max_length=500, null=True, blank=True)
    image = models.URLField(
        null=True, blank=True)  # TODO Should be an url ?
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, blank=True)
    categories = models.JSONField(null=True, blank=True)  # list of strings
    count = models.IntegerField(default=0)
    published = models.DateTimeField(default=timezone.now)
    visibility = models.CharField(
        max_length=50, choices=visibility_type.choices, default=visibility_type.PUBLIC)
    unlisted = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    url = models.URLField(null=True, blank=True, editable=False)
    # TODO list of comment object ? -> list of comment id maybe


######### Comment #########
class Comment(models.Model):
    type = models.CharField(default="comment", max_length=100)
    commentID = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField(max_length=500, null=True)
    contentType = models.CharField(
        max_length=100, default=content_type.PLAIN, blank=False, null=False)
    #image = models.URLField()  # TODO Should be an url ?
    published = models.DateTimeField(default=timezone.now)
    #url = models.URLField(null=True, blank=True, editable=False)


# Like ######### Doubt we need @context in the model (see proj description)
class Like(models.Model):
    context = models.URLField(null=True, blank=True, editable=False)
    type = models.CharField(default="like", max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.CharField(max_length=100)
    # object is the post object/link or the comment object/link that is liked
    object = models.URLField(null=True, blank=True, editable=False)


# Inbox ######### potentially missing list of inbox object
class Inbox(models.Model):
    type = models.CharField(default="inbox", max_length=100)
    inboxID = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    items = models.JSONField(default=list)


######### Node #########
class Node(models.Model):
    url = models.URLField(default=HOSTNAME, max_length=100)
    host = models.UUIDField(
        primary_key=True, editable=False, unique=True, blank=True)  # doubt we even need this,this class only looks for interfaceable servers/hosts
    user = models.OneToOneField(  # so no need to generate unique id
        User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    hostUsername = models.CharField(max_length=200, null=False)
    hostPassword = models.CharField(max_length=200, null=False)
    email = models.EmailField(
        max_length=200, null=True, blank=True, default=None)
    displayName = models.CharField(max_length=200, null=True, blank=True)
