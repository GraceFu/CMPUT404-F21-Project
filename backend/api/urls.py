"""Social_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


This class sets the api endpoints of the app. Refers to https://github.com/abramhindle/CMPUT404-project-socialdistribution/blob/master/project.org#objects
Methods allowed: GET, POST, PUT, DELETE
"""
# Needs work

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import api
from .views import auth, homepage

urlpatterns = [
    # Authors

    # Followers

    # FriendRequest

    # Post

    # Comments

    # Likes

    # Liked

    # Inbox

    path("homepage", homepage.homepage, name="homepage"),
    path("signup", auth.signup_request, name="signup"),
    path("login", auth.login_request, name="login")
]
