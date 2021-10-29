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
# https://www.django-rest-framework.org/api-guide/viewsets/#example

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from api.views import auth, homepage, posts
from api.utils import methods

router = DefaultRouter()
router.register(r'posts', posts.post_view_set, basename='posts')
urlpatterns = router.urls

urlpatterns = [
    # Authors

    # Followers

    # FriendRequest

    # Post            methods.GET: 'get_author_posts',  --> GET /posts/> uuid invalid error?
    path("posts/", posts.post_view_set.as_view({methods.POST: 'create_post_without_post_id'}), name="handle_new_post"),
    path("posts/<str:post_id>", posts.post_view_set.as_view({methods.GET: 'get_public_posts', methods.POST: 'create_post_with_post_id'}), name="handle_existing_post"),
    
    # Comments

    # Likes

    # Liked

    # Inbox

    path("homepage", homepage.homepage, name="homepage"),
    path("signup", auth.signup_request, name="signup"),
    path("login", auth.login_request, name="login")
]
