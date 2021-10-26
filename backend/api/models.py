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


######### Author #########
class Author(models.Model):


class Follow(models.Model):
    request_id = models.UUIDField(primary_key=True, default=generate_id, editable=False, unique=True)
    actor = models.ForeignKey(Author, on_delete=models.CASCADE)  # friend request from user
    object = models.ForeignKey(Author, on_delete=models.CASCADE)  # friend request to user
    request_time = models.DateTimeField(auto_now_add=True)
    summary = models.CharField(max_length=100, default="new friend request")
    request_acceptance = models.BooleanField(default=False)
    friend_status = models.BooleanField(default=False)


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
