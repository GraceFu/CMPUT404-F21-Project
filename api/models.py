from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from Social_network.settings import HOSTNAME


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
    host = models.CharField(default="/", max_length=500)
    url = models.URLField(null=True, blank=True, editable=False)
    github = models.URLField(null=True, blank=True)
    # profile_picture = models.URLField(null=True, blank=True)
    # TODO set profile picture properly


######### Follower #########
class Follower(models.Model):
    type = models.CharField(default="followers", max_length=100)
    """ author is the followee, foreignAuthor is the follower """
    followee = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="followee", blank=True)
    follower = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="follower", blank=True)

    class Meta:
        unique_together = ('followee', 'follower')


######### Friend #########
class Friend(models.Model):
    type = models.CharField(default="friend", max_length=100)
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
    comments = models.URLField(
        null=True, blank=True, editable=False, max_length=500)


######### Comment #########
class Comment(models.Model):
    type = models.CharField(default="comment", max_length=100)
    commentID = models.UUIDField(
        primary_key=True, editable=False, unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, blank=True, null=True)
    content = models.CharField(max_length=500, null=True)
    contentType = models.CharField(
        max_length=100, default=content_type.PLAIN, blank=False, null=False)
    # image = models.URLField()  # TODO Should be an url ?
    published = models.DateTimeField(default=timezone.now)
    #url = models.URLField(null=True, blank=True, editable=False)


######### Like #########
class Like(models.Model):
    # context = models.URLField(null=True, blank=True, editable=False)
    type = models.CharField(default="like", max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    summary = models.CharField(max_length=100, null=True)
    # object is the post object/link or the comment object/link that is liked
    object = models.CharField(max_length=500, null=True)


######### InboxObject #########
class InboxObject(models.Model):
    type = models.CharField(default="inbox", max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    object = models.JSONField(null=True, blank=True)


######### Node #########
class Node(models.Model):
    url = models.URLField(primary_key=True, max_length=100)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    hostUsername = models.CharField(max_length=200, null=False)
    hostPassword = models.CharField(max_length=200, null=False)
