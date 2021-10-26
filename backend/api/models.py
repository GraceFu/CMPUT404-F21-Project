from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.fields import related
from django.conf import settings
from backend.Social_network.settings import HOSTNAME
from utils import generate_id
import uuid
from django import forms

# Create your models here.
##signup and friends not implemented yet

visibility_choices = [
    ('public', 'Public'),
    ('followers', 'Follower'),
]

######### Author #########
class Author(models.Model):
        id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=100, unique=True, editable=False)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
        tokens = models.CharField(max_length=100,default="1234")
        displayName = models.CharField(max_length=100)
        host = models.CharField(default=HOSTNAME, max_length=500)
        url = models.URLField(null=True, blank=True)
        github = models.URLField(null=True, blank=True)


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



######### Post #########
class Post(models.Model):
        post_id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=100, unique=True, editable=False)
        author_id = models.ForeignKey(Author, on_delete=models.CASCADE,)
        title = models.CharField(max_length=100)
        origin_post = models.URLField()
        source = models.URLField()
        description = models.CharField(max_length=200)
        content = models.CharField(max_length=500, null=True, blank=True)
        contentType = models.CharField(max_length=50, default="text/html", blank=False, null=False)
        image_content = models.TextField(null=True, blank=True)
        categories_id = models.JSONField()
        published_date = models.DateTimeField(default=timezone.now)
        visibility = models.CharField(max_length=50, choices=visibility_choices, default='public')
        unlisted = models.BooleanField(default=False)
        likes = models.IntegerField(default=0)
        comments = models.IntegerField(default=0)
        host = models.CharField(max_length=50)
        url = models.URLField(null=True, blank=True, default=None)




######### Comment #########
class Comment(models.Model):
        comment_id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=100, unique=True, editable=False)
        post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
        author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
        content = models.CharField(max_length=500, null=True)
        image_content = models.TextField(null=True, blank=True)
        published_date = models.DateTimeField(default=timezone.now)
        contentType = models.CharField(max_length=50, default="text/html", blank=False, null=False)
        host = models.CharField(max_length=50)
        post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
        url = models.URLField(null=True, blank=True, default=None)



######### Like #########
class Like(models.Model):
        like_id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=100, unique=True, editable=False)
        author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
        post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
        comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
        notification = models.CharField(max_length=100, default="Someone liked your post!")
        published_date = models.DateTimeField(default=timezone.now)
        url = models.URLField(null=True, blank=True, default=None)




######### Node #########
class Node(models.Model):
        host = models.CharField(primary_key=True, default=HOSTNAME, max_length=100)
        user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
        username = models.CharField(max_length=200, null=False)
        password = models.CharField(max_length=200, null=False)
        email = models.EmailField(max_length=200, null=False)
        displayName = models.CharField(max_length=200, null=True)
        host_url = models.URLField(max_lenght = 200,null=True, blank=True)
        date_added = models.DateTimeField(auto_now_add=True)



class sign_up_form(forms.Form):
    username = forms.CharField(max_length=200, null=False)
    password = forms.CharField(max_length=200, null=False)
    email = forms.EmailField(max_length=200, null=False)
    displayName = forms.CharField(max_length=200, null=True)
    host_url = forms.URLField(max_lenght = 200,null=True, blank=True)

