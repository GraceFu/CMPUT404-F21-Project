from api.models import *
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


USER_LOGIN_URL = reverse('author_login')
USER_REGISTER_URL = reverse('author_register')
USER_LOGOUT_URL = reverse('author_logout')


class TestAuthorView(APITestCase):
    


    def setUp(self):


        test_user = User.objects.create_user(
            username= 'testuser',
            password= 'testpassword',
        )

        test_user2 = User.objects.create_user(
            username='testuser2',
            password='testpassword2',
        )

        self.client = APIClient()

        self.author_test = Author.objects.create(
            user=test_user,
            displayName='Test Author',
            host="http://localhost:8000/",
            github="https://www.github.com/TestAuthor"
        )

        self.author_test2 = Author.objects.create(
            user=test_user2,
            displayName='Test Author2',
            host="http://localhost:8000/",
            github="https://www.github.com/TestAuthor2"
        )

        self.author_test.save()
        self.author_test2.save()

    def test_login_author(self):
        """Testing for a successful login of an author"""

        login_response = self.client.post(
            USER_LOGIN_URL,
            {
                'username': 'testuser',
                'password': 'testpassword'
            },
            format='json'
        )

        # checking if the response is successful
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)    



    def test_retrieve_auth_author(self):
        """Testing for login of an authorized author
        """
        # forcing authentication of an author
        self.client.force_authenticate(user=self.author_test.user)

        author_response = self.client.get(
            reverse('author_object', kwargs={'id': self.author_test.id}))

        # checking for authorized user
        self.assertEqual(author_response.status_code, status.HTTP_200_OK)


    def test_register_author(self):
        """Testing for a successful registration of an author"""

        register_response = self.client.post(
            USER_REGISTER_URL,
            {
                "user": "testuser3",
                "password": "testpassword3",
                "password2" : "testpassword3",
                "displayName": "Test User3",
                "github": "https://github.com/testuser",
            },
            format='json'
        )

        # checking if the response is successful
        self.assertEqual(register_response.status_code, status.HTTP_201_CREATED)

    def test_register_author_duplicate(self):
        """Testing for a duplicate registration of an author"""

        register_response = self.client.post(
            USER_REGISTER_URL,
            {
                'user': 'testuser',
                'password': 'testpassword',
                "password2": "testpassword",
                "displayName": "Test User",
                "github": "https://github.com/testuser",
            },
            format='json'
        )

        # checking if the response is successful
        self.assertEqual(register_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout_author(self):
        """Testing for a successful logout of an author"""

        # forcing authentication of an author
        self.client.force_authenticate(user=self.author_test.user)

        logout_response = self.client.post(
            USER_LOGOUT_URL,
            {
                'username': 'testuser',
                'password': 'testpassword'
            },
            format='json'

        )

        # checking if the response is successful
        self.assertEqual(logout_response.status_code, status.HTTP_200_OK)

    
    
    
    def test_delete_author(self):
        """Testing for a successful deletion of an author"""
        # forcing authentication of an author
        self.client.force_authenticate(user=self.author_test.user)

        author_response = self.client.delete(
            reverse('author_detail', args=[self.author_test.id]))

        # checking for authorized user
        self.assertEqual(author_response.status_code, status.HTTP_204_NO_CONTENT)




    def test_incorrect_login_author(self):
        
        """Testing for incorrect login"""

        login_response = self.client.post(
            USER_LOGIN_URL,
            {
                'username': 'testuser',
                'password': 'wrongpassword'
            },
            format='json'
        )

        # checking if the response is successful
        self.assertEqual(login_response.status_code, status.HTTP_403_FORBIDDEN)



   

    def test_unauthorized_login_author(self):
        """Testing for login of an unauthorized author"""

        author_response = self.client.get(
            reverse('author_object', kwargs={'id': self.author_test.id}))

        # checking for authorized user
        self.assertEqual(author_response.status_code,
                         status.HTTP_401_UNAUTHORIZED)




    def test_update_author(self):
        """Testing for a successful update of an author"""


        # forcing authentication of an author
        self.client.force_authenticate(user=self.author_test.user)

        post_request = {
            "displayName": "Test User New",
            "github": "https://github.com/testusernew",
        }

        update_response = self.client.post(
            reverse('author_detail', args=[self.author_test.id]),
            post_request,
            format='json'
        )

        # checking if the response is successful

        self.assertEqual(update_response.status_code, status.HTTP_200_OK)




        #checking if the update is successful
        self.assertEqual(update_response.data['displayName'], "Test User New")
        self.assertEqual(update_response.data['github'], "https://github.com/testusernew")


    #get a list of authors
    def test_list_authors(self):

        # forcing authentication of an author
        self.client.force_authenticate(user=self.author_test.user)
        self.client.force_authenticate(user=self.author_test2.user)

        authors_response = self.client.get(
            reverse('author_list'))

        # checking for authorized user
        self.assertEqual(authors_response.status_code, status.HTTP_200_OK)

        #checking if the list is not empty
        self.assertTrue(authors_response.data)
        
        #checking if the list contains the correct number of authors
        self.assertEqual(len(authors_response.data), 2)

        self.assertEqual(authors_response.data[0]['displayName'], "Test Author")
        self.assertEqual(authors_response.data[1]['displayName'], "Test Author2")
 