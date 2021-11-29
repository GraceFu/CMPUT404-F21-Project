from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from ..models import Author
from ..forms import NewUserForm
from ..utils import generate_id


def signup_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            author = Author(user=user, authorID=generate_id())
            author.github = form.cleaned_data["github"]
            author.displayName = form.cleaned_data["displayName"]
            author.url = "https://" + request.get_host() + "/api/author/" + author.authorID
            author.host = request.get_host()
            author.save()
            messages.warning(
                request, "Thank you! Please wait for admin to appove your registration.")
        else:
            messages.error(
                request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="signup.html", context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # TODO: Different message sent to wrong auth and not-yet-approved users
            if user is not None and user.is_active:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
        else:
            messages.error(
                request, "Invalid username or password. Or your account has not been approved yet.")

    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form": form})


def logout_request(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    return redirect("login")


def default_page_request(request):
    if request.method == "GET":
        try:
            if request.user.is_authenticated and request.user.is_active and request.user.author:
                return redirect("homepage")
        except:
            return redirect("login")

    return redirect("login")
