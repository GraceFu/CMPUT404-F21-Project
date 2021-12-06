from django.http import response
from api import *
from api.models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
USER_LOGIN_URL = reverse('author_login')


class TestPost(APITestCase):
    
    """
        This method will run before any test. Creating test users
    """

    def setUp(self):
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
            displayName="Test Author 3",
            host="http://localhost:8000/",
            github="https://www.github.com/testAuthor3"
        )

        self.author_test1.save()
        self.author_test2.save()
        self.author_test3.save()


        self.follow_1 = Follower.objects.create(
            follower=self.author_test1,
            followee=self.author_test3,
        )
        self.follow_2 = Follower.objects.create(
            follower=self.author_test3,
            followee=self.author_test1,
        )

        self.follow_1.save()
        self.follow_2.save()
        
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
                "author",
                "post1"
            ],
        )


        self.test_post1_author.save()


        # test user 1 create post 2

        self.test_post2_author = Post.objects.create(
            author=self.author_test1,
            title="Test Post 2",
            description="Test Post 2 Description",
            content="Test Post 2 Content",  
            contentType="text/plain",
            visibility="PUBLIC",
            unlisted=False,
            categories=[
                "Test",
                "post",
                "author",
                "post2"
            ],
        )


        self.test_post2_author.save()

        # test user 2 create post

        self.test_post3_author = Post.objects.create(

            author=self.author_test2,
            title="Test Post 3",
            description="Test Post 3 Description",
            content="Test Post 3 Content",  
            contentType="text/plain",
            visibility="PUBLIC",
            unlisted=False,
            categories=[
                "Test",
                "post",
                "author",
                "post3"
            ],
        )


        self.test_post3_author.save()

        # test user 3 create post   
        self.test_post4_author = Post.objects.create(

            author=self.author_test3,
            title="Test Post 4",
            description="Test Post 4 Description",
            content="Test Post 4 Content",  
            contentType="text/plain",
            visibility="PUBLIC",
            unlisted=False,
            categories=[
                "Test",
                "post",
                "author",
                "post4"
            ],
        )


        self.test_post4_author.save()




        # test post to update
        self.test_post_to_update = Post.objects.create(
            
            author=self.author_test1,
            title="Test Post to Update",
            description="Test Post to Update Description",
            content="Test Post to Update Content",  
            contentType="text/plain",
            visibility="PUBLIC",
            unlisted=False,
            categories=[
                "Test",
                "post",
                "author",
                "post_to_update"
            ],
        )


        self.test_post_to_update.save()

        #test post to delete
        self.test_post_to_delete = Post.objects.create(

            author=self.author_test1,
            title="Test Post to Delete",
            description="Test Post to Delete Description",
            content="Test Post to Delete Content",  
            contentType="text/plain",
            visibility="PUBLIC",
            unlisted=False,
            categories=[
                "Test",
                "post",
                "author",
                "post_to_delete"
            ],
        )


        self.test_post_to_delete.save()


    
    def test_check_post_detail(self):

        """Testing for returning a post detail
        """
        # forcing authentication of an author
        self.client.force_authenticate(user=self.author_test1.user)

        detail_response = self.client.get(
            reverse('get_public_post', kwargs={'author_id': self.author_test1.id, 'post_id': self.test_post1_author.id}))

        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)


    def test_check_post_list(self):

        """Testing for returning a list of posts
        """
        # forcing authentication of an author
        self.client.force_authenticate(user=self.author_test1.user)

        list_response = self.client.get(reverse('my-posts', kwargs={'author_id': self.author_test1.id}))

        self.assertEqual(list_response.status_code, status.HTTP_200_OK)



    def test_create_post(self):
        """Testing post creation
        """
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.post(
            reverse('create_post_with_new_id', kwargs={'author_id': self.author_test1.id}),
            {
                "type": "post",
                "title": "Test Post",
                "description": "Test Post Description",
                "contentType": "text/plain",
                "content": "Test Post Content",
                "categories": [
                    "Test",
                    "post",
                    "author"

                ],
                "visibility": "PUBLIC",
                "unlisted": False,
                "author": {
                    "type": "author",
                    "id": "http://localhost:8000/author/{}".format(self.author_test1.id),
                    "host": "http://localhost:8000/",
                    "displayName": "Test Author 1",
                    "github": "https://www.github.com/testAuthor1"
                },
                "likes": "0",
                "count": "0",
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('type', response.data)
        self.assertIn('title', response.data)
        self.assertIn('id', response.data)
        self.assertIn('source', response.data)
        self.assertIn('origin', response.data)
        self.assertIn('contentType', response.data)
        self.assertIn('content', response.data)
        self.assertIn('description', response.data)
        self.assertIn('published', response.data)
        self.assertIn('comments', response.data)
        self.assertIn('visibility', response.data)
        self.assertIn('author', response.data)
        self.assertIn('categories', response.data)
        self.assertIn('count', response.data)
        self.assertIn('unlisted', response.data)


    #test for creating post with wrong author
    def test_create_post_wrong_author(self):

        """Testing post creation with wrong author
        """
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.post(
            reverse('create_post_with_new_id', kwargs={'author_id': self.author_test2.id}),
            {
                "type": "post",
                "title": "Test Post",
                "description": "Test Post Description",
                "contentType": "text/plain",
                "content": "Test Post Content",
                "categories": [
                    "Test",
                    "post",
                    "author"

                ],
                "visibility": "PUBLIC",
                "unlisted": False,
                "author": {
                    "type": "author",
                    "id": "http://localhost:8000/author/{}".format(self.author_test1.id),
                    "host": "http://localhost:8000/",
                    "displayName": "Test Author 1",
                    "github": "https://www.github.com/testAuthor1"
                },
                "likes": "0",
                "count": "0",
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



    #test for getting an author's posts
    def test_get_author_posts(self):

        """Testing for getting an author's posts
        """
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.get(reverse('get_author_posts', kwargs={'author_id': self.author_test1.id}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)



    #test for updating a post
    def test_update_post(self):

        """Testing for updating a post
        """
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.put(
            reverse('update_post', kwargs={'author_id': self.author_test1.id, 'post_id': self.test_post_to_update.id}),
            {
                "type": "post",
                "title": "Test Post to Update",
                "description": "Test Post to Update Description",
                "contentType": "text/plain",
                "content": "Test Post to Update Content",
                "categories": [
                    "Test",
                    "post",
                    "author",
                    "post_to_update"
                ],
                "visibility": "PUBLIC",
                "unlisted": False,
                "author": {
                    "type": "author",
                    "id": "http://localhost:8000/author/{}".format(self.author_test1.id),
                    "host": "http://localhost:8000/",
                    "displayName": "Test Author 1",
                    "github": "https://www.github.com/testAuthor1"
                },
                "likes": "0",
                "count": "0",
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], 'Test Post to Update')
        self.assertEqual(response.data["description"],'Test Post to Update Description')
        self.assertEqual(response.data["author"]['displayName'], 'Test Author 1')




    #test for deleting a post
    def test_delete_post(self):

        """Testing for deleting a post
        """
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.delete(
            reverse('delete_post', kwargs={'author_id': self.author_test1.id, 'post_id': self.test_post_to_delete.id}),
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
    #Testing for incorrectly updating a post
    def test_update_incorrect_post_public(self):
        

        """Testing for incorrectly updating a post
        """
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.post(
            reverse('update_post', kwargs={'author_id': self.author_test1.id, 'post_id': self.test_post_to_update.id}),
            {
                "description": "Test Post to Update Description",
                "contentType": "text/plain",
                "content": "Test Post to Update Content",
                "categories": [
                    "Test",
                    "post",
                    "author"
                ],
                "visibility": "PUBLIC",
                "unlisted": False,
                "author": {
                    "type": "author",
                    "id": "http://localhost:8000/author/{}".format(self.author_test1.id),
                    "host": "http://localhost:8000/",
                    "displayName": "Test Author 1",
                    "github": "https://www.github.com/testAuthor1"
                }
            },  format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


     #Testing for incorrectly updating a post that has friend visibility (private)
    def test_update_incorrect_post_public(self):
        

        """Testing for incorrectly updating a post
        """
        self.client.force_authenticate(user=self.author_test1.user)

        response = self.client.post(
            reverse('update_post', kwargs={'author_id': self.author_test1.id, 'post_id': self.test_post_to_update.id}),
            {
                "description": "Test Post to Update Description",
                "contentType": "text/plain",
                "content": "Test Post to Update Content",
                "categories": [
                    "Test",
                    "post",
                    "author"
                ],
                "visibility": "FRIENDS",
                "unlisted": False,
                "author": {
                    "type": "author",
                    "id": "http://localhost:8000/author/{}".format(self.author_test1.id),
                    "host": "http://localhost:8000/",
                    "displayName": "Test Author 1",
                    "github": "https://www.github.com/testAuthor1"
                }
            },  format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    

    #test for creating post with author and post id
    def test_create_post_with_author_id(self):

        post_id = self.test_post_to_putupdate.id
        author_id = self.author_test2.id
        self.client.force_authenticate(user=self.author_test2.user)

        response = self.client.put(
            reverse('create_post_with_existing_id', kwargs={'author_id':author_id, 'post_id': post_id}),
            { 
                "title": "Test Post for an author",
                "id": "http://localhost:8000/author/{}/posts/{}".format(
                    author_id , post_id
                ),
                "description": "Test Post for an author description",
                "source": "http://localhost:8000/",
                "origin": "http://localhost:8000/",
                "content": "Test Post for an author content",
                "contentType": "text/plain",
                "categories": [
                    "Test",
                    "post",
                    "author",
                    "post_to_create"
                ],
                "visibility": "PUBLIC",
                "unlisted": False,
                "author": {
                    "type": "author",
                    "id": "http://localhost:8000/author/{}".format(self.author_test2.id),
                    "host": "http://localhost:8000/",
                    "displayName": "Test Author 2",
                    "github": "https://www.github.com/testAuthor2"
                },
                "likes": "0",
                "count": "0",
            },
            format='json',
        )


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    #test for creating private post with author and post id

    def test_create_private_post_with_author_id(self):
            
            author_id = self.author_test2.id
            self.client.force_authenticate(user=self.author_test2.user)
    
            response = self.client.put(
                reverse('create_post_with_existing_id', kwargs={'author_id':author_id}),
                { 
                    "title": "Test Post for an author",
                    "id": "http://localhost:8000/author/{}/posts/{}".format(
                        author_id
                    ),
                    "description": "Test Post for an author description",
                    "source": "http://localhost:8000/",
                    "origin": "http://localhost:8000/",
                    "content": "Test Post for an author content",
                    "contentType": "text/plain",
                    "categories": [
                        "Test",
                        "post",
                        "author",
                        "post_to_create",
                        "private"
                    ],
                    "visibility": "PRIVATE",
                    "unlisted": False,
                    "author": {
                        "type": "author",
                        "id": "http://localhost:8000/author/{}".format(self.author_test2.id),
                        "host": "http://localhost:8000/",
                        "displayName": "Test Author 2",
                        "github": "https://www.github.com/testAuthor2"
                    },
                    "likes": "0",
                    "count": "0",
                },
                format='json',
            )
    
    
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)


            self.client.force_authenticate(user=self.author_test3.user)

            response_2 = self.client.get(
                reverse(
                    'get_inbox_items',
                    kwargs={
                        'author_id': self.author_test3.id,
                    }
                )
            )

            self.assertEqual(response_2.data['items'][0]['type'], "post")
            self.assertEqual(response_2.data['items'][0]['title'], "Test Post for an author")