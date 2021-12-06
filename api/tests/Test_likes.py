from django.http import response
from api import *
from api.models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

class TestLikeAPI(APITestCase):
    
    """
        This method will run before any test. Creating test users
    """
    
    def setUp(self):
        self.test_user1 = User.objects.create_user(
            username='testuser1',
            password='testpassword1'
        )

        self.test_user2 = User.objects.create_user(
            username='anotheruser',
            password='anotherpassword'
        )

        self.client = APIClient()

        self.author_test1 = Author.objects.create(
            user=self.test_user1,
            displayName='Test Author 1',
            host="http://localhost:8000/",
            github="https://www.github.com/testuser1",
        )

        self.author_test2 = Author.objects.create(
            user=self.test_user2,
            displayName='Test Author 2',
            host="http://localhost:8000/",
            github="https://www.github.com/anotheruser",
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

        # test user 2 create PRIVATE post

        self.test_post2friends_author = Post.objects.create(
            author=self.author_test1,
            title="Test Post 2",
            description="Test Post 2 Description",
            content="Test Post 2 Content",  
            contentType="text/plain",
            visibility="FREINDS",
            unlisted=False,
            categories=[
                "Test",
                "post",
                "author",
                "friends"
            ],
        )


        self.test_post2friends_author.save()

        # test user 1 create comment on post 1

        self.test_comment = Post.objects.create(
            author=self.author_test1,
            title="comment1",
            description="comment1 description",
            content="comment1 content",
            contentType="text/plain",
            visibility="PUBLIC",
            unlisted=False,
            categories=[
                "Test",
                "post",
                "author"
            ],
        )

        self.test_comment.save()

        # comment on a post made by author 1
        self.test_comment1 = Comment.objects.create(
            author=self.author_test2,
            post=self.test_comment,
            comment="comment by a user",
            contentType="text/plain",
            post_author=self.author_test1
        )
        self.test_comment1.save()



        #create likes
        self.test_like1 = Like.objects.create(

            author=self.author_test1,
            post=self.test_post1_author,
            comment=self.test_comment1,
            like=True,
        )

        self.test_like1.save()

        self.test_like2 = Like.objects.create(

            author=self.author_test2,
            post=self.test_post1_author,
            comment=self.test_comment1,
            like=True,
        )

        self.test_like2.save()

        self.test_like3 = Like.objects.create(

            author=self.author_test1,
            post=self.test_post2friends_author,
            comment=self.test_comment1,
            like=True,
        )

        self.test_like3.save()

        self.test_like4 = Like.objects.create(

            author=self.author_test2,
            post=self.test_post2friends_author,
            comment=self.test_comment1,
            like=True,
        )

        self.test_like4.save()


    #test for liking a post made by a friend
    def test_like_on_post_friends(self):

        # forcing authentication of an authors
        self.client.force_authenticate(user=self.author_test1.user)
        self.client.force_authenticate(user=self.author_test2.user)

        response = self.client.get(
            reverse(
                'get_post_likes',
                kwargs={
                    'author_id': self.author_test1.id,
                    'post_id': self.test_post2friends_author.id
                }
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]['summary'], 'Someone Likes your post')


    #test for liking a comment made by an author
    def test_like_on_comment_author(self):

        # forcing authentication of authors
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.get(
            reverse(
                'get_comment_likes',
                kwargs={
                    'author_id': self.author_test1.id,
                    'post_id': self.test_post1_author.id,
                    'comment_id': self.test_comment1.id
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    #test for liking a comment made by a friend
    def test_like_on_comment_friends(self):
            
            # forcing authentication of authors
            self.client.force_authenticate(user=self.author_test1.user)
    
            response = self.client.get(
                reverse(
                    'get_comment_likes',
                    kwargs={
                        'author_id': self.author_test2.id,
                        'post_id': self.test_post1_author.id,
                        'comment_id': self.test_comment1.id
                    }
                )
            )
    
            self.assertEqual(response.status_code, status.HTTP_200_OK)



  

    #list of items liked by author
    def test_list_of_likes_author(self):

        # forcing authentication of authors
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.get(
            reverse(
                'get_author_liked',
                kwargs={
                    'author_id': self.author_test1.id
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
