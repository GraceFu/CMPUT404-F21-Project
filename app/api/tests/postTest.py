from rest_framework.test import APITestCase, APIClient
from django.urls import include, path, reverse
from ..views import posts
from ..utils import methods, generate_id

# https://www.django-rest-framework.org/api-guide/testing/


class TestPost(APITestCase):
    urlpatterns = [
        path("author/<str:authorID>/posts/", posts.PostViewSet.as_view(
        {methods.GET: 'get_author_post', methods.POST: 'create_post_with_new_id'}), name="handle_new_post"),
        path("author/<str:authorID>/posts/<str:postID>", posts.PostViewSet.as_view(
        {methods.GET: 'get_public_post', methods.POST: 'update_post', methods.DELETE: 'delete_post', methods.PUT: "create_post_with_existing_id"}), name="handle_existing_post")
    ]

    def test_get_author_post_fail():
        authorID = generate_id()
        client = APIClient()
        response = client.get('author/<str:authorID>/posts/')
        assert response.status_code == 401