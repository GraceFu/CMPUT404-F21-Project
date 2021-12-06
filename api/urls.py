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


from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import auth, homepage, authors, followers, posts, profiles, comments, likes, inbox
from api.utils import methods


""" All api endpoints begain with api/ """

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
    path("api/authors/", authors.AuthorsViewSet.as_view(
        {methods.GET: 'list_all'}), name="authors_list"),
    path("api/author/<str:authorID>", authors.ProfileViewSet.as_view(
        {methods.GET: 'retrieve', methods.POST: 'update'}), name="author_profile"),
    path("authors", authors.all_authors_view, name="authors"),
    path("api/get_num_of_authors", authors.AuthorsViewSet.as_view(
        {methods.GET: 'get_num_of_authors'}), name="get_num_of_authors"),

    # Profile
    path("profile/<str:authorID>", profiles.profile_view, name="profile"),

    # Followers
    # Get Followees
    path("api/author/<str:authorID>/followees", followers.FollowersViewSet.as_view(
        {methods.GET: 'get_author_followees'}), name="author_followees"),
    # Get Followers
    path("api/author/<str:authorID>/followers", followers.FollowersViewSet.as_view(
        {methods.GET: 'get_author_followers'}), name="author_followers"),
    # Get Friends
    path("api/author/<str:authorID>/friends", followers.FollowersViewSet.as_view(
        {methods.GET: 'get_author_friends'}), name="author_friends"),
    path("api/author/<str:authorID>/followers/<str:foreignAuthorID>", followers.FollowersViewSet.as_view(
        {methods.GET: 'check_if_follower', methods.PUT: 'follow', methods.DELETE: 'unfollow'}), name="handle_follower"),

    # FriendRequest

    # Post
    # Currently author posts
    path("my-posts", posts.my_posts_view, name="my-posts"),
    path("author/<str:authorID>/posts/<str:postID>", posts.single_post_view, name="single-post"),
    # Management of Post 'GET' and 'POST' then direct to 'GET', 'POST', 'PUT' and 'DELETE'
    path("api/author/<str:authorID>/posts",
         posts.post_handler, name="post_handler"),
    path("api/author/<str:authorID>/posts/", posts.PostViewSet.as_view(
        {methods.GET: 'get_author_posts', methods.POST: 'create_post_with_new_id'}), name="handle_new_post"),
    path("api/author/<str:authorID>/posts/<str:postID>", posts.PostViewSet.as_view(
        {methods.GET: 'get_public_post', methods.POST: 'update_post', methods.DELETE: 'delete_post', methods.PUT: "create_post_with_existing_id"}), name="handle_existing_post"),

    # Comments
    path("api/author/<str:authorID>/posts/<str:postID>/comments", comments.CommentViewSet.as_view(
        {methods.GET: 'get_post_comment', methods.POST: 'create_comment_with_new_id'}), name="handle_new_comment"),

    # Likes
    path("api/author/<str:authorID>/posts/<str:postID>/likes", likes.LikeViewSet.as_view(
        {methods.GET: 'get_post_likes'}), name="get_post_likes"),
    path("api/author/<str:authorID>/posts/<str:postID>/comments/<str:commentID>/likes", likes.LikeViewSet.as_view(
        {methods.GET: 'get_comment_likes'}), name="get_comment_likes"),
    path("api/author/<str:authorID>/inbox/",
         likes.LikeViewSet.as_view({methods.POST: 'like_object'}), name="like_object"),

    # Liked
    path("api/author/<str:authorID>/liked", likes.LikeViewSet.as_view(
        {methods.GET: 'get_author_liked'}), name="get_author_liked"),

    # Inbox
    path("api/author/<str:authorID>/inbox", inbox.InboxViewSet.as_view(
        {methods.GET: 'get_inbox_items', methods.POST: 'add_item_to_inbox', methods.DELETE: 'clear_inbox'}), name="handle_inbox"),
    path("my-inbox", inbox.my_inbox_view, name="my-inbox"),
    path("api/author/<str:authorID>/inbox/get_num_of_inbox_items", inbox.InboxViewSet.as_view(
        {methods.GET: 'get_num_of_inbox_items'}), name="get_num_of_inbox_items"),

]
