from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.fields import related
from django.conf import settings
from backend.Social_network.settings import HOSTNAME
from utils import generate_id

# Create your models here.
##signup and friends not implemented yet

######### Author #########
class Author(models.Model):
	id = models.CharField(primary_key=True, default=generate_id, max_length=100, unique=True, editable=False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, editable=False)
	token = models.CharField(default="1234", max_length=100)
	displayName = models.CharField(max_length=100)
	github = models.URLField(default=('https://github.com/'))
	host = models.CharField(default=HOSTNAME, max_length=200)
	url = models.URLField()


######### Post #########
class Post(models.Model):
	id = models.CharField(primary_key=True, default=generate_id, unique=True, max_length=100)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	source = models.URLField(default=HOSTNAME)
	origin = models.URLField(default=HOSTNAME)
	description = models.CharField(max_length=100)
	contentType = models.CharField(max_length=50)
	content = models.CharField(max_length=500, null=True, blank=True)
	image_content = models.TextField(null=True, blank=True)
	categories = models.JSONField()
	published = models.DateTimeField(auto_now_add=True)
	visibility = models.CharField(max_length=20)
	unlisted = models.BooleanField(default=False)
	host = models.CharField(max_length=50)


######### Comment #########
class Comment(models.Model):
	id = models.CharField(primary_key=True, default=generate_id, editable=False, unique=True, max_length=100)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
	comment = models.CharField(max_length=500, null=True)
	image_content = models.TextField(null=True, blank=True)
	published = models.DateTimeField(auto_now_add=True)
	contentType = models.CharField(max_length=50)
	host = models.CharField(max_length=50)
	post_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='post_author')


######### Like #########
class Like(models.Model):
	id = models.CharField(primary_key=True, default=generate_id, editable=False, unique=True, max_length=100)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
	summary = models.CharField(max_length=100, default="Someone Likes your post")

######### Node #########
class Node(models.Model):
	host = models.CharField(primary_key=True, default=HOSTNAME, max_length=200)
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	remote_username = models.CharField(max_length=150)
	remote_password = models.CharField(max_length=150)

######### Follow #########
class Follow(models.Model):
    request_id = models.UUIDField(primary_key=True, default=generate_id, editable=False, unique=True)
    actor = models.ForeignKey(Author, on_delete=models.CASCADE)  # friend request from user
    object = models.ForeignKey(Author, on_delete=models.CASCADE)  # friend request to user
    request_time = models.DateTimeField(auto_now_add=True)
    summary = models.CharField(max_length=100, default="new friend request")
    request_acceptance = models.BooleanField(default=False)
    friend_status = models.BooleanField(default=False)

######### Inbox #########
class Inbox(models.Model):
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#choices
    class Type(models.TextChoices):
        POST = "post"
        FOLLOW = "follow"
        LIKE = "like"
    inbox_id = models.UUIDField(primary_key=True, default=generate_id, editable=False, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.TextField(choices=Type.choices)
    published = models.DateTimeField(auto_now_add=True)
