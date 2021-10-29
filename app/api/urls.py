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
from api.views import auth, homepage, authors, followers, posts
from api.utils import methods

router = DefaultRouter()
router.register(r'posts', posts.post_view_set, basename='posts')
urlpatterns = router.urls

urlpatterns = [
    # Authorization
    path("login", auth.login_request, name="login"),
    path("signup", auth.signup_request, name="signup"),

    # Homepage after login
    path("homepage", homepage.homepage, name="homepage"),

    # Authors
    # TODO -> {methods.GET: 'retrieve_all_authors'}, -> GET error,since we dont have a object to trigger GET. frontend should have a trigger that send request payload and method to the url
    # TODO -> {methods.GET: 'retrieve'}, -> GET error,since we dont have a object to trigger GET. frontend should have a trigger that send request payload and method to the url
    path("author/<str:author_id>", authors.author_view_set.as_view({methods.POST: 'update'}), name="author_profile"),
    
    # Followers

    # FriendRequest

    # Post
    # TODO -> {methods.GET: 'get_author_posts'}, -> 404 cuz we dont have a author_id
    path("author/<str:author_id>/posts/", posts.post_view_set.as_view({methods.GET: 'get_author_post', methods.POST: 'create_post_with_new_id'}), name="handle_new_post"),
    # TODO -> fix update_post to have author_id and able able update TODO {methods.PUT: 'get_public_posts'}
    path("author/<str:author_id>/posts/<str:post_id>", posts.post_view_set.as_view({methods.GET: 'get_public_post', methods.POST: 'update_post', methods.DELETE: 'delete_post'}), name="handle_existing_post")
    # TODO post
    #  stream

    # Comments

    # Likes

    # Liked

    # Inbox

]
