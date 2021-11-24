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
from api.views import auth, homepage, authors, followers, posts, profiles, comments, likes
from api.utils import methods

router = DefaultRouter()
router.register(r'posts', posts.PostViewSet, basename='posts')
urlpatterns = router.urls

urlpatterns = [
    # Default
    path("", auth.default_page_request, name="default"),

    # Authorization
    path("login", auth.login_request, name="login"),
    path("signup", auth.signup_request, name="signup"),
    path("logout", auth.logout_request, name="logout"),

    # Homepage
    path("homepage", homepage.homepage_request, name="homepage"),

    # Authors
    path("api/authors",
         authors.AuthorsViewSet.as_view({methods.GET: 'list_all'}), name="authors_list"),
    path("api/author/<str:authorID>",
         authors.ProfileViewSet.as_view({methods.GET: 'retrieve', methods.POST: 'update'}), name="author_profile"),

    # Profile
    path("profile/<str:authorID>", profiles.profile_view, name="profile"),

    # Followers

    # FriendRequest

    # Post
    # Currently author posts
    path("my-posts", posts.my_posts_view, name="my-posts"),
    # Management of Post 'GET' and 'POST' then direct to 'GET', 'POST', 'PUT' and 'DELETE'
    path("api/author/<str:authorID>/posts",
         posts.post_handler, name="post_handler"),
    # TODO -> {methods.GET: 'get_author_posts'}, -> 404 cuz we dont have a authorID
    path("api/author/<str:authorID>/posts/", posts.PostViewSet.as_view(
        {methods.GET: 'get_author_posts', methods.POST: 'create_post_with_new_id'}), name="handle_new_post"),
    # TODO -> fix update_post to have authorID and able able update TODO {methods.PUT: 'get_public_posts'}
    path("api/author/<str:authorID>/posts/<str:postID>", posts.PostViewSet.as_view(
        {methods.GET: 'get_public_post', methods.POST: 'update_post', methods.DELETE: 'delete_post', methods.PUT: "create_post_with_existing_id"}), name="handle_existing_post"),
    # TODO post
    #  stream

    # Comments
    path("api/author/<str:authorID>/posts/<str:postID>/comments", comments.CommentAPISet.as_view(
        {methods.GET: 'get_post_comment', methods.POST: 'create_comment_with_new_id'}), name="handle_new_comment"),


    # Likes
    path("api/author/<str:authorID>/posts/<str:postID>/likes",
         likes.LikeViewSet.as_view({methods.GET: 'get_post_likes'}), name="get_post_likes"),
    path("api/author/<str:authorID>/posts/<str:postID>/comments/<str:commentID>/likes",
         likes.LikeViewSet.as_view({methods.GET: 'get_comment_likes'}), name="get_comment_likes"),

    # Liked
    path("api/author/<str:authorID>/liked", likes.LikeViewSet.as_view(
        {methods.GET: 'get_author_liked'}), name="get_author_liked"),
    # Inbox


]
