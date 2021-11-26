from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Social_network.settings import HOSTNAME


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
        Author, on_delete=models.CASCADE, related_name="followee", blank=True)
    # follow request to user, person to be follow
    follower = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="follower", blank=True)
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


######### Post #########
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
        null=True, blank=True)
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
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=500, null=True)
    contentType = models.CharField(
        max_length=100, default=content_type.PLAIN, blank=False, null=False)
    # image = models.URLField()  # TODO Should be an url ?
    published = models.DateTimeField(default=timezone.now)
    #url = models.URLField(null=True, blank=True, editable=False)


######### Comment #########
class Like(models.Model):
    # context = models.URLField(null=True, blank=True, editable=False)
    type = models.CharField(default="like", max_length=100)
    author = models.OneToOneField(
        Author, on_delete=models.CASCADE, unique=True, blank=True)
    summary = models.CharField(max_length=100)
    # object is the post object/link or the comment object/link that is liked
    object = models.URLField(null=True, blank=True, editable=False)


######### Inbox #########
class Inbox(models.Model):
    type = models.CharField(default="inbox", max_length=100)
    inboxID = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    items = models.JSONField(default=list)


######### Node #########
class Node(models.Model):
    hostURL = models.URLField(primary_key=True, unique = True)
    hostName = models.CharField(max_length=200, default="foreignConnection")
    hostUsername = models.CharField(max_length=200, null=False)
    hostPassword = models.CharField(max_length=200, null=False)
