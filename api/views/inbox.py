from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from api.utils import invalid_user_view

@login_required(login_url='login')
def my_posts_view(request):
    # Check the user is invalid in view
    if invalid_user_view(request):
        return redirect("login")

    content = {}
    content['my_inbox_page'] = True

    return render(request, "inbox.html", content)
