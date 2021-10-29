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
class visibilityType(models.TextChoices):
    PUBLIC = "PUBLIC"
    FRIENDS = "FRIENDS"


class contentType(models.TextChoices):
    MARKDOWN = "text/markdown"
    PLAIN = "text/plain"
    APPLICATION = "application/base64"
    PNG = "image/png;base64"
    JPEG = "image/jpeg;base64"


######### Author #########
class Author(models.Model):
    type = models.CharField(default="author", max_length=100)
    author_id = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, default="Someone")
    host = models.CharField(default="localhost", max_length=500)
    url = models.URLField(null=True, blank=True, editable=False)
    github = models.URLField(null=True, blank=True)
    # profile_picture = models.URLField(null=True, blank=True)
    # TODO set profile picture properly


######### Follow #########


class Follow(models.Model):
    type = models.CharField(default="followers", max_length=100)
    request_id = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    # follow request from user
    followee = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="followee")
    # follow request to user
    follower = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="follower")
    request_time = models.DateTimeField(auto_now_add=True)
    request_acceptance = models.BooleanField(default=False)

######### Friend #########


class Friend(models.Model):
    type = models.CharField(default="friend", max_length=100)
    request_id = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    # friend request from user
    actor = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="actor")
    # friend request to user
    object = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="object")
    summary = models.CharField(max_length=100)
    request_time = models.DateTimeField(auto_now_add=True)
    request_acceptance = models.BooleanField(default=False)

# Post ######### potentially missing comment field and list of comment field


class Post(models.Model):
    type = models.CharField(default="post", max_length=100)
    post_id = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=100)
    source = models.URLField(null=True, blank=True)
    origin_post = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    content_type = models.CharField(
        max_length=100, default=contentType.PLAIN, null=True, blank=True)
    content = models.CharField(max_length=500, null=True, blank=True)
    image_content = models.URLField(
        null=True, blank=True)  # TODO Should be an url ?
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, blank=True)
    categories = models.JSONField(null=True, blank=True)  # list of strings
    count = models.IntegerField(default=0)
    published_date = models.DateTimeField(default=timezone.now)
    visibility = models.CharField(
        max_length=50, choices=visibilityType.choices, default=visibilityType.PUBLIC)
    unlisted = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    url = models.URLField(null=True, blank=True, editable=False)
    # TODO list of comment object ? -> list of comment id maybe

######### Comment #########


class Comment(models.Model):
    type = models.CharField(default="comment", max_length=100)
    comment_id = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField(max_length=500, null=True)
    content_type = models.CharField(
        max_length=100, default=contentType.PLAIN, blank=False, null=False)
    image_content = models.URLField()  # TODO Should be an url ?
    published_date = models.DateTimeField(default=timezone.now)
    url = models.URLField(null=True, blank=True, editable=False)

# Like ######### Doubt we need @context in the model (see proj description)


class Like(models.Model):
    # like_id = models.UUIDField(primary_key=True, default=generate_id, editable=False, unique=True)
    type = models.CharField(default="like", max_length=100)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.CharField(max_length=100)
    # object_url refer to the post object/link or the comment object/link that is liked
    object_url = models.URLField(null=True, blank=True, editable=False)

# Inbox ######### potentially missing list of inbox object


class Inbox(models.Model):
    type = models.CharField(default="inbox", max_length=100)
    inbox_id = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    items = models.JSONField(default=list)


######### Node #########
class Node(models.Model):
    host_url = models.URLField(default='localhost', max_length=100)
    host = models.UUIDField(
        primary_key=True, editable=False, unique=True, blank=True)  # doubt we even need this,this class only looks for interfaceable servers/hosts
    user = models.OneToOneField(  # so no need to generate unique id
        User, on_delete=models.CASCADE, blank=True, null=True)
    date_interfaced = models.DateTimeField(auto_now_add=True)
    host_username = models.CharField(max_length=200, null=False)
    host_password = models.CharField(max_length=200, null=False)
    email = models.EmailField(
        max_length=200, null=True, blank=True, default=None)
    display_name = models.CharField(max_length=200, null=True, blank=True)

# ######### Sign up #########
# class sign_up_form(forms.Form):
#     username = forms.CharField(max_length=200, null=False)
#     password = forms.CharField(max_length=200, null=False)
#     email = forms.EmailField(max_length=200, null=False)
#     display_name = forms.CharField(max_length=200, null=True)
#     host_url = forms.URLField(max_lenght = 200,null=True, blank=True)
