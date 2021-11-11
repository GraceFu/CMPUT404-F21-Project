from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from api.models import *
from api.utils import *

# Source: https://docs.djangoproject.com/zh-hans/3.2/topics/auth/default/#the-login-required-decorator
@login_required(login_url='login')
def homepage_request(request):
    # Check the user is invalid in view
    if invalid_user_view(request): 
        return redirect("login")

    content = {}

    author = Author.objects.filter(authorID=request.user.author.authorID).first()
    self_post = Post.objects.filter(author__exact=author).order_by('-published')

    print(self_post)

    content['author'] = author
    content['self_post'] = self_post

    return render(request, "homepage.html", content)
