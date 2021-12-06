from django.http import response
from api import *
from api.models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

USER_LOGIN_URL = reverse('author_login')


class TestFollow(APITestCase):
    
    def setUp(self):

        self.test_user1 = User.objects.create_user(
            username='testuser1',
            password='testpassword1'
        )

        self.test_user2 = User.objects.create_user(
            username='testuser2',
            password='  testpassword2'
        )

        self.test_user3 = User.objects.create_user(
            username='testuser3',
            password='  testpassword3'
        )

        self.test_user4 = User.objects.create_user(
            username='testuser4',
            password=' testpassword4'
        )

        self.test_user5 = User.objects.create_user(
            username='testuser5',
            password='testpassword5'
        )

        self.test_user6 = User.objects.create_user(
            username='testuser6',
            password='testpassword6'
        )


        self.client = APIClient()

        self.author_test1 = Author.objects.create(
            user=self.test_user1,
            displayName='Test User 1',
            host="http://localhost:8000/",
            github="https://www.github.com/testuser1"
        )

        self.author_test2 = Author.objects.create(
            user=self.test_user2,
            displayName='Test User 2',
            host="http://localhost:8000/",
            github="https://www.github.com/testuser2"
        )

        self.author_test5 = Author.objects.create(
            user=self.test_user5,
            displayName='Test User 5',
            host="http://localhost:8000/",
            github="https://www.github.com/testuser5"
        )

        self.author_test6 = Author.objects.create(
            user=self.test_user6,
            displayName='Test User 6',
            host="http://localhost:8000/",
            github="https://www.github.com/testuser6"
        )


        self.author_test1.save()
        self.author_test2.save()
        self.author_test5.save()
        self.author_test6.save()

        self.author_test3 = Author.objects.create(
            user=self.test_user3,
            displayName='Test User 3',
            host="http://localhost:8000/",
            github="https://www.github.com/testuser3"
        )

        self.author_test4 = Author.objects.create(
            user=self.test_user4,
            displayName='Test User 4',
            host="http://localhost:8000/",
            github="https://www.github.com/testuser4"
        )

        self.author_test3.save()
        self.author_test4.save()




        self.author1_follow_author2 = Follower.objects.create(
            follower=self.author_test1,
            followee=self.author_test2,
            friends=False
        )
        self.author1_follow_author2.save()

        self.author3_follow_author2 = Follower.objects.create(
            follower=self.author_test3,
            followee=self.author_test2,
            friends=False
        )
        self.author3_follow_author2.save()

        self.author3_friend_author4 = Follower.objects.create(
            follower=self.author_test3,
            followee=self.author_test4,
            friends=True
        )
        self.author3_friend_author4.save()

        self.author4_friend_author3 = Follower.objects.create(
            follower=self.author_test4,
            followee=self.author_test3,
            friends=True
        )
        self.author4_friend_author3.save()




    def test_follow_friend(self):
        """
        Testing friend as a follower and vice versa
        """

        # forcing authentication of an authors
        self.client.force_authenticate(user=self.author_test1.user)
        self.client.force_authenticate(user=self.author_test2.user)


        response = self.client.post(
            reverse(
                'update_followers',
                kwargs={
                    'author_id': self.author_test1.id,
                    'foreign_id': self.author_test2.id
                }
            ),
            follow_request = {  
                'type': 'followee',
                'object': { 
                    "type": "author",
                    "id": "http://localhost:8000/author/{}".format(self.author_test1.id),
                    "host": "http://localhost:8000/",
                    "displayName": "Test User 1",
                    "github": "https://www.github.com/testuser1"
                },
                'actor': {
                    "type": "author",
                    "id": "http://localhost:8000/author/{}".format(self.author_test2.id),
                    "host": "http://localhost:8000/",
                    "displayName": "Test User 2",
                    "github": "https://www.github.com/testuser2"

                
                }
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            Follower.objects.get(
                follower=self.author_test1,
                followee=self.author_test2
            ).friends,
            True
        )

        self.assertEqual(
            Follower.objects.get(
                follower=self.author_test2,
                followee=self.author_test1
            ).friends,
            True
        )



    def test_get_follower(self):

        """
        Test for getting a follower object if the foreign author follows
        an author regardless of them being friends
        """

        # forcing authentication of an authors
        self.client.force_authenticate(user=self.author_test1.user)
        self.client.force_authenticate(user=self.author_test2.user)

        response = self.client.get(
            reverse(
                'update_followers',
                kwargs={
                    'author_id': self.author_test2.id,
                    'foreign_id': self.author_test1.id
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'Follow')
        self.assertEqual(response.data['actor']['id'].split(
            "/")[-1], self.author_test1.id)
        self.assertEqual(response.data['object']['id'].split(
            "/")[-1], self.author_test2.id)




    def test_follow_list(self):
        """
        Getting a list of all the authors that the foreign author follows
        """
        # forcing authentication of an authors
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.get(
            reverse(
                'followers_list',
                kwargs={
                    'author_id': self.author_test2.id
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['items'][0]['id'].split(
            "/")[-1], self.author_test1.id)
        self.assertEqual(response.data['items'][1]['id'].split(
            "/")[-1], self.author_test3.id)

    
    





    def test_friend(self):

        self.client.force_authenticate(user=self.author_test5.user)

        response = self.client.get(
            reverse(
                'friends_api',
                kwargs={
                    'author_id': self.author_test5.id
                }
            )
        )
        self.assertEqual(response.data['items'], [])

        follow_request = {
            'type': "followee",
            'object': {
                "type": "author",
                "id": "http://localhost:8000/author/{}".format(self.author_test6.id),
                "host": "http://localhost:8000/",
                "displayName": "test user 6",
                "github": "https://www.github.com/testuser6"
            },
            'actor': {
                "type": "author",
                "id": "http://localhost:8000/author/{}".format(self.author_test5.id),
                "host": "http://localhost:8000/",
                "displayName": "test user 5",
                "github": "https://www.github.com/testuser5"
            }
        }

        response = self.client.put(
            reverse(
                'update_followers',
                kwargs={
                    'author_id': self.author_test6.id,
                    'foreign_id': self.author_test5.id
                }
            ),
            follow_request,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            reverse(
                'friends_api',
                kwargs={
                    'author_id': self.author_test5.id
                }
            )
        )
        self.assertEqual(response.data['items'], [])

        follow_request2 = {
            'type': "followee",
            'object': {
                "type": "author",
                "id": "http://localhost:8000/author/{}".format(self.author_test5.id),
                "host": "http://localhost:8000/",
                "displayName": "test user 5",
                "github": "https://www.github.com/testuser5"
            },
            'actor': {
                "type": "author",
                "id": "http://localhost:8000/author/{}".format(self.author_test6.id),
                "host": "http://localhost:8000/",
                "displayName": "test user 6",
                "github": "https://www.github.com/testuser6"
            }
        }

        response = self.client.put(
            reverse(
                'update_followers',
                kwargs={
                    'author_id': self.author_test5.id,
                    'foreign_id': self.author_test6.id
                }
            ),
            follow_request2,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            reverse(
                'friends_api',
                kwargs={
                    'author_id': self.author_test5.id
                }
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'friends')
        self.assertEqual(response.data['items'][0]['displayName'], 'test user 6')