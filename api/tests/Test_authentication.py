from django.contrib.auth.models import User
from django.test import TestCase



class AuthenticationTests(TestCase):
    def setUp(self):
        response = self.client.get("")
        self.request = response.wsgi_request

    #Tests if a user can log in
    def test_login(self):
        registration_data = {
            "user": "testuser",
            "password": "testpassword",
            "password2": "testpassword",
            "displayName": "Test User",
            "github": "https://github.com/testuser",
            
        }

        registration_response = self.client.post(
            f"/api/v1/dj-rest-auth/registration/",   ##### is this correct?##########
            registration_data,
            format="json",
        )
        self.assertEquals(registration_response.status_code, 201)
        self.assertEquals(len(User.objects.all()), 1)
        self.assertEqual(User.objects.get(username="testuser").is_active, False)



    # Tests if new user can login and approved by admin

    def test_approved_user(self):
        registration_data = {
            "user": "testuser2",
            "password": "testpassword",
            "password2": "testpassword",
            "displayName": "Test User2",
            "github": "https://github.com/testuser2",
        }
        registration_response = self.client.post(
            f"/api/v1/dj-rest-auth/registration/",
            registration_data,
            format="json",
        )
        new_user = User.objects.get(username="testuser2")
        self.assertEquals(registration_response.status_code, 201)
        self.assertEqual(new_user.is_active, False)
        self.assertEquals(len(User.objects.all()), 1)

        login_data = {
            "user": "testuser2",
            "password": "testpassword"
        }

        login_response = self.client.post(
            f"/api/v1/dj-rest-auth/login/",
            login_data,
            format="json",
        )

        self.assertEquals(login_response.status_code, 400)
        new_user.is_active = True
        new_user.save()
        login_response = self.client.post(
            f"/api/v1/dj-rest-auth/login/",
            login_data,
            format="json",
        )
        self.assertEquals(login_response.status_code, 200)



    # Tests if a user can log out

    def test_logout(self):
        registration_data = {
            "user": "testuser3",
            "password": "testpassword",
            "password2": "testpassword",
            "displayName": "Test User3",
            "github": "https://github.com/testuser3",
        }
        registration_response = self.client.post(
            f"/api/v1/dj-rest-auth/registration/",
            registration_data,
            format="json",
        )
        new_user = User.objects.get(username="testuser3")
        self.assertEquals(registration_response.status_code, 201)
        self.assertEqual(new_user.is_active, False)
        self.assertEquals(len(User.objects.all()), 1)

        login_data = {
            "user": "testuser3",
            "password": "testpassword"
        }

        login_response = self.client.post(
            f"/api/v1/dj-rest-auth/login/",
            login_data,
            format="json",
        )

        self.assertEquals(login_response.status_code, 200)

        logout_response = self.client.post(
            f"/api/v1/dj-rest-auth/logout/",
            format="json",
        )

        self.assertEquals(logout_response.status_code, 200)





   


