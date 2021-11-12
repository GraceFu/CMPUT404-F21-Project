from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from api.models import Author, Post
from api.utils import invalid_user_view

# Source: https://docs.djangoproject.com/zh-hans/3.2/topics/auth/default/#the-login-required-decorator
@login_required(login_url='login')
def homepage_request(request):
    # Check the user is invalid in view
    if invalid_user_view(request): 
        return redirect("login")

    content = {}

    author = Author.objects.get(authorID=request.user.author.authorID)
    public_post = Post.objects.filter(visibility__exact="PUBLIC").order_by('-published')

    content['author'] = author
    content['public_post'] = public_post

    return render(request, "homepage.html", content)
