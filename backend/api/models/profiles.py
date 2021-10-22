from django.db import models
from django.contrib.auth.models import User
from api.utils.utils import get_random_code
from django.template.defaultfilters import slugify

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True)
    bio = models.TextField(default = "It's empty...",max_length=500,blank=True)
    # avatar = models.ImageField(default = 'avatar.png',upload_to='avatars/', blank=True)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True,blank=True)
    # phone = models.CharField(max_length=20)


def __str__(self):
    return f"{self.user.username}-{self.created}"


def save(self, *args, **kwargs):
    a = False
    if self.first_name and self.last_name:
        to_slug = slugify(str(self.first_name) +" "+ str(self.last_name))
        a = Profile.objects.filter(slug=to_slug).exists()
        while a:
            to_slug = slugify(to_slug +" " + str(get_random_code()))
            a = Profile.objects.filter(slug=to_slug).exists()
    else:
        to_slug = str(self.user)
    self.slug = to_slug
    super(self).save(*args, **kwargs)
