from django.http import response
from api import *
from api.models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

USER_LOGIN_URL = reverse('author_login')
USER_REGISTER_URL = reverse('author_register')
USER_LOGOUT_URL = reverse('author_logout')
USER_PROFILE_URL = reverse('author_profile')


class TestCommentView(APITestCase):
    
    """
        This method will run before any test. It will create users
    """

    def setUp(self):
        
        self.test_user = User.objects.create_user(
            username= 'testuser',
            password= 'testpassword',

        )
        

        self.test_user2 = User.objects.create_user(
            username='testuser2',
            password='testpassword2',

        )

        self.client = APIClient()



        self.author_test1 = Author.objects.create(
            user=self.test_user,
            displayName='Test Author',
            host="http://localhost:8000/",
            github="https://www.github.com/testuser"
        )

        self.author_test2 = Author.objects.create(
            user=self.test_user2,
            displayName='Test Author2',
            host="http://localhost:8000/",
            github="https://www.github.com/testuser2"
        )

        self.author_test1.save()
        self.author_test2.save()

        # test user 1 create post

        self.test_post1_author = Post.objects.create(
            author=self.author_test1,
            title="Test Post 1",
            description="Test Post 1 Description",
            content="Test Post 1 Content",  
            contentType="text/plain",
            visibility="PUBLIC",
            unlisted=False,
            categories=[
                "Test",
                "post",
                "author"
            ],
        )


        self.test_post1_author.save()

        #create comment on test post
        self.test_post_to_comment = Post.objects.create(
            author=self.author_test1,
            title="Test Post_comment 1",
            description="Test Post_comment 1 Description",
            content=" Test Post_comment 1 Content",
            contentType="text/plain",
            visibility="PUBLIC",
            unlisted=False,
            categories=[
                "Test",
                "post",
                "author"
            ],
        )

        self.test_post_to_comment.save()

        # post comment on post made by author 1
        self.test_comment1 = Comment.objects.create(
            author=self.author_test2,
            post=self.test_post_to_comment,
            comment="Test Comment 1",
            contentType="text/plain",
            post_author=self.author_test1
        )
        self.test_comment1.save()


        # post comment on own post
        self.test_comment2 = Comment.objects.create(
            author=self.author_test1,
            post=self.test_post_to_comment,
            comment=" Test Comment 2",
            contentType="text/plain",
            post_author=self.author_test1
        )
        self.test_comment2.save()




    #testing comments

    def test_comment_on_post(self):

        """Tests to comment on a post made by an author
        """
        # forcing authentication of an author
        self.client.force_authenticate(user=self.author_test1.user)
        self.client.force_authenticate(user=self.author_test2.user)

        comment_request = {
            "type": "comment",
            "author": {
                "type": "author",
                "url": "http://localhost:8000/author/{}".format(self.author_test2.id),
                "host": "http://localhost:8000/",
                "displayName": "testuser2",
                "github": "https://www.github.com/testuser2"
            },
            "comment": "test comment for this post",
            'contentType': "text/plain"
        }

        response = self.client.post(
            reverse(
                'comments_object',
                kwargs={
                    'author_id': self.author_test1.id,
                    'post_id': self.test_post_to_comment.id
                }
            ),
            comment_request,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_comment_on_own_post(self):

        """Tests to comment on a post made by an author
        """
        # forcing authentication of an author
        self.client.force_authenticate(user=self.author_test1.user)

        comment_request = {
            "type": "comment",
            "author": {
                "type": "author",
                "url": "http://localhost:8000/author/{}".format(self.author_test1.id),
                "host": "http://localhost:8000/",
                "displayName": "testuser",
                "github": "https://www.github.com/testuser"
            },
            "comment": "test comment for my post",
            'contentType': "text/plain"
        }

        response = self.client.post(
            reverse(
                'comments_object',
                kwargs={
                    'author_id': self.author_test1.id,
                    'post_id': self.test_post_to_comment.id
                }
            ),
            comment_request,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




    
    #Testing for unsucessfully creating a comment on an existing post by missing information in the request sent

    def test_unsuccesful_comment_on_post(self):
            
            # forcing authentication of an author
            self.client.force_authenticate(user=self.author_test1.user)
            self.client.force_authenticate(user=self.author_test2.user)
    
            comment_request = {
                "type": "comment",
                "author": {
                    "type": "author",
                    "url": "http://localhost:8000/author/{}".format(self.author_test2.id),
                    "host": "http://localhost:8000/",
                    "displayName": "testuser",
                    "github": "https://www.github.com/testuser"
                },
                "comment": "",
                'contentType': "text/plain"
            }
    
            response = self.client.post(
                reverse(
                    'comments_object',
                    kwargs={
                        'author_id': self.author_test1.id,
                        'post_id': self.test_post_to_comment.id   ##need a post id here
                    }
                ),
                comment_request,
                format='json'
            )
    
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    #test pagination of the comments

    def test_pagination_of_comments(self):

        """Tests to comment on a post made by an author
        """
        # forcing authentication of an author
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.post(
            reverse(
                'comments_object',
                kwargs={
                    'author_id': self.author_test1.id,
                    'post_id': self.test_post_to_comment.id
                }
            ),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


