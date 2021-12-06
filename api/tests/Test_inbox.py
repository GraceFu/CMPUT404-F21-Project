from django.http import response
from api import *
from api.models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

USER_LOGIN_URL = reverse('author_login')


class TestInbox(APITestCase):
    
    def setUp(self):
        """
        This method will run before any test.Creating authors
        """

        self.test_user1 = User.objects.create_user(
            username='testuser1', 
            password='testpassword1'
        )

        self.test_user2 = User.objects.create_user(
            username='testuser2',
            password='testpassword2'
        )

        self.test_user3 = User.objects.create_user(
            username='testuser3',
            password='testpassword3'
        )

        self.client = APIClient()

        self.author_test1 = Author.objects.create(
            user=self.test_user1,
            displayName='Test Author 1',
            host="http://localhost:8000/",
            github="https://www.github.com/testAuthor1"
        )

        self.author_test2 = Author.objects.create(
            user=self.test_user2,
            displayName='Test Author 2',
            host="http://localhost:8000/",
            github="https://www.github.com/testAuthor2"
        )

        self.author_test3 = Author.objects.create(
            user=self.test_user3,
            displayName='Test Author 3',
            host="http://localhost:8000/",
            github="https://www.github.com/testAuthor3"
        )

        self.author_test1.save()
        self.author_test2.save()
        self.author_test3.save()



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

        #Creating likes
        self.test_like1_post1 = Like.objects.create(
            author=self.author_test2,
            post=self.test_post1_author1,
        )
        self.test_like1_post1.save()


        self.author3_follow_author1 = Follower.objects.create(
            follower=self.author_test3,
            followee=self.author_test1,
            friends=False
        )
        self.author3_follow_author1.save()



        self.author1_inbox1 = Inbox.objects.create(
            author=self.author_test1,
            like=self.test_like1_post1,
        )
        self.author1_inbox1.save()



        self.author1_inbox2 = Inbox.objects.create(
            author=self.author_test1,
            follow=self.author3_follow_author1
        )
        self.author1_inbox2.save()






    def test_add_follow_request_to_inbox(self):
        """
            Test for follow requests in Inbox
        """

        #authentication of an author 1 & 2
        self.client.force_authenticate(user=self.author_test1.user)
        self.client.force_authenticate(user=self.author_test2.user)

        response = self.client.post(
            reverse(
                'inbox_object',
                kwargs={
                    'author_id': self.author_test1.id
                }
            ),
            follow_request = {
                'type': "followee",
                'object': {
                    "type": "author",
                    "id": "http://localhost:8000/author/{}".format(self.author_test1.id),
                    "host": "http://localhost:8000/",
                    "displayName": "Test Author 1",
                    "github": "https://www.github.com/testAuthor1",
                },
                'actor': {
                    "type": "author",
                    "id": "http://localhost:8000/author/{}".format(self.author_test2.id),
                    "host": "http://localhost:8000/",
                    "displayName": "Test Author 2",
                    "github": "https://www.github.com/testAuthor2",
                }
            },
            format='json'
        )




        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Inbox.objects.count(), 2)



        
    def test_add_like_request_to_inbox(self):
        
        """
            Test for like requests in Inbox
        """
        # forcing authentication of an authors
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.post(
            reverse(
                'inbox_object',
                kwargs={
                    'author_id': self.author_test1.id,
                }
            ),
            like_request = {
                "type": "like",
                "author": {
                    "type": "author",
                    "id": f"https://localhost:8000/author/{self.author_test3.id}",
                    "host": "https://localhost:8000/",
                    "displayName": "Test Author 3",
                    "url": f"https://localhost:8000/author/{self.author_test3.id}",
                    "github": "https://www.github.com/testAuthor3",
                },
                "object": f"https://localhost:8000/author/{self.author_test1.id}/posts/"+self.test_post1_author1.id
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    
    def test__get_posts_inbox(self):
        """
        Test for getting inbox
        """
        # forcing authentication of an authors
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.get(
            reverse(
                'inbox_object',
                kwargs={
                    'author_id': self.author_test1.id,
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['items'][0]['type'], "Follow")
        self.assertEqual(response.data['items'][1]['type'], "like")

    
    
    
    def test_clear_inbox(self):
        """
        Testing for clearing inbox
        """
        # forcing authentication of an authors
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.delete(
            reverse(
                'inbox_object',
                kwargs={
                    'author_id': self.author_test1.id,
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


