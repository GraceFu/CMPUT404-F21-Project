from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from api.models import *

# Source: https://docs.djangoproject.com/zh-hans/3.2/topics/auth/default/#the-login-required-decorator
@login_required(login_url='login')
def homepage_request(request):
    '''if request.user.is_anonymous and not request.user.is_active:
        return redirect(reverse('login'))'''

    author = Author.objects.filter(user=request.user).first()

    return render(request, "homepage.html", { 'Author': author })
