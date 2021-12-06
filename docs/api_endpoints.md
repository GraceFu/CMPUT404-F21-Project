# API Endpoints Documentation

[Author](#author) <br>
[Post](#post) <br>
[Comment](#comment) <br>
[Liked & likes](#liked-&-likes) <br>
[Follower & Friend](#follower-friend) <br>
[Inbox](#inbox) <br>

## Author

### URL: ://api/authors/

- **GET**: Retrieve all authors on the server

  - Example request: `GET /api/authors/`

  - Example response:
    - 200 OK

    ```json
    {
        "type": "authors",
        "items": [
            {
                "type": "author",
                "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
                "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
                "host": "https://cmput404-proj-social-app.herokuapp.com/",
                "displayName": "team19",
                "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
            },
            {
                "type": "author",
                "authorID": "e4801aff-10b2-43f0-a1dc-ca27dc94c7a9",
                "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/e4801aff-10b2-43f0-a1dc-ca27dc94c7a9/",
                "host": "https://cmput404-proj-social-app.herokuapp.com/",
                "displayName": "tester19",
                "github": "https://github.com/tester19.com"
            }
        ]
    }
    ```
    - 401 Unauthorized (if not logged in)


### URL: ://api/author/{AUTHOR_ID}

- **GET**: Retrieve this author's profile

  - Example request: `GET /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e`

  - Example response: 
    - 200 OK

    ```json
    {
        "type": "author",
        "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
        "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
        "host": "https://cmput404-proj-social-app.herokuapp.com/",
        "displayName": "team19",
        "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
    }
    ```
    - 401 Unauthorized (if not logged in)

- **POST**: Update this author's profile

  - Example request: `POST /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e`
    ```json
    {
        "type": "author",
        "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
        "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
        "host": "https://cmput404-proj-social-app.herokuapp.com/",
        "displayName": "team19_newName",
        "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
    }
    ```

  - Example response: 
    - 200 OK
    
    ```json
    {
        "type": "author",
        "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
        "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
        "host": "https://cmput404-proj-social-app.herokuapp.com/",
        "displayName": "team19_newName",
        "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
    }
    ```
    - 400 Bad Request (if request payload is not valid/missing nassesary field)
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)


## Post

### URL: ://api/author/{AUTHOR_ID}/posts/

- **GET**: Retrieve recent posts of this author *(default pagination size=5)*

  - Example request *without pagenation*: `GET /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/`

  - Example response: 
    - 200 OK

    ```json
    {
        "items": [
            {
                "type": "post",
                "title": "Second Post",
                "postID": "bf2c76dc-bcde-400a-9564-4fb062bf0ce6",
                "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/bf2c76dc-bcde-400a-9564-4fb062bf0ce6",
                "author": {
                    "type": "author",
                    "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
                    "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
                    "host": "https://cmput404-proj-social-app.herokuapp.com/",
                    "displayName": "team19",
                    "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
                },
                "source": null,
                "origin": null,
                "description": "Team 19 second post",
                "contentType": "text/plain",
                "content": "This is a post",
                "categories": null,
                "count": 0,
                "published": "2021-12-05T01:27:59.971897Z",
                "visibility": "PUBLIC",
                "unlisted": false,
                "likes": 0,
                "comments": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/bf2c76dc-bcde-400a-9564-4fb062bf0ce6/comments"
            },
            {
                "type": "post",
                "title": "First Post",
                "postID": "67a293a3-67a8-4191-82da-91c85c72371b",
                "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a3-67a8-4191-82da-91c85c72371b",
                "author": {
                    "type": "author",
                    "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
                    "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
                    "host": "https://cmput404-proj-social-app.herokuapp.com/",
                    "displayName": "team19",
                    "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
                },
                "source": null,
                "origin": null,
                "description": "Team 19 first post",
                "contentType": "text/plain",
                "content": "Hello World!",
                "categories": null,
                "count": 0,
                "published": "2021-12-05T01:25:28.309081Z",
                "visibility": "PUBLIC",
                "unlisted": false,
                "likes": 0,
                "comments": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a3-67a8-4191-82da-91c85c72371b/comments"
            }
        ]
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post does not exist)

- **POST**: Create a post with generated POST_ID

  - Example request: `POST /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/`
    ```json
    {
        "title": "New Post Title",
        "description": "my description",
        "contentType": "text/plain",
        "content": "my content",
        "categories": [
            "web",
            "tutorial"
        ],
        "visibility": "PUBLIC",
        "unlisted": false
    }
    ```

  - Example response: 
    - 200 OK

    ```json
    {
        "type": "post",
        "title": "New Post Title",
        "postID": "70d0a59b-4fee-4e84-b091-1b1161455ebb",
        "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb",
        "author": {
            "type": "author",
            "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "team19",
            "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
        },
        "source": null,
        "origin": null,
        "description": "my description",
        "contentType": "text/plain",
        "content": "my content",
        "categories": [
            "web",
            "tutorial"
        ],
        "count": 0,
        "published": "2021-12-05T01:31:48.037419",
        "visibility": "PUBLIC",
        "unlisted": false,
        "likes": 0,
        "comments": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb/comments"
    }
    ```
    - 400 Bad Request (if request payload is not valid/missing nassesary field)
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)


### URL: ://api/author/{AUTHOR_ID}/posts/{POST_ID}

- **GET**: Retrieve specific public post

  - Example request: `GET /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb`

  - Example response: 
    - 200 OK
    
    ```json
    {
        "type": "post",
        "title": "New Post Title",
        "postID": "70d0a59b-4fee-4e84-b091-1b1161455ebb",
        "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb",
        "author": {
            "type": "author",
            "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e96e645d8bff370a2d052d31e/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "team19",
            "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
        },
        "source": null,
        "origin": null,
        "description": "my description",
        "contentType": "text/plain",
        "content": "my content",
        "categories": [
            "web",
            "tutorial"
        ],
        "count": 0,
        "published": "2021-12-06T05:34:37.386696Z",
        "visibility": "PUBLIC",
        "unlisted": false,
        "likes": 0,
        "comments": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb/comments"
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post does not exist)

- **POST**: Update this post

  - Example request: `POST /api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb`
    ```json
    {
        "title": "Update Post Title",
        "description": "my description 2.0",
        "content": "my content 2.0",
        "categories": [
            "tech"
        ]
    }
    ```

  - Example response: 
    - 200 OK
    ```json
    {
        "type": "post",
        "title": "Update Post Title",
        "postID": "70d0a59b-4fee-4e84-b091-1b1161455ebb",
        "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb",
        "author": {
            "type": "author",
            "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "team19",
            "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
        },
        "source": null,
        "origin": null,
        "description": "my description 2.0",
        "contentType": "text/plain",
        "content": "my content 2.0",
        "categories": [
            "tech"
        ],
        "count": 0,
        "published": "2021-12-05T01:31:48.037419Z",
        "visibility": "PUBLIC",
        "unlisted": false,
        "likes": 0,
        "comments": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb/comments"
    }
    ```
    - 400 Bad Request (if request payload is not valid/missing nassesary field)
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post does not exist)

- **DELETE**: Delete this post

  - Example request: `DELETE /api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb`

  - Example response: 
    - 200 OK
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post not exists)

- **PUT**: Create a post with POST_ID

  - Example request: `PUT /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/ccf0b45d-47c5-4247-b7e4-a834b140f98a`
    ```json
    {
        "type": "post",
        "title": "PUT Post Title",
        "postID": "ccf0b45d-47c5-4247-b7e4-a834b140f98a",
        "description": "PUT post description",
        "contentType": "text/plain",
        "content": "my content 2.0",
        "visibility": "PUBLIC",
        "unlisted": false
    }
    ```

  - Example response: 
    - 200 OK

    ```json
    {
        "type": "post",
        "title": "PUT Post Title",
        "postID": "ccf0b45d-47c5-4247-b7e4-a834b140f98a",
        "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/ccf0b45d-47c5-4247-b7e4-a834b140f98a",
        "author": {
            "type": "author",
            "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "team19",
            "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
        },
        "source": null,
        "origin": null,
        "description": "PUT post description",
        "contentType": "text/plain",
        "content": "my content 2.0",
        "categories": null,
        "count": 0,
        "published": "2021-12-05T01:55:26.398274",
        "visibility": "PUBLIC",
        "unlisted": false,
        "likes": 0,
        "comments": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/ccf0b45d-47c5-4247-b7e4-a834b140f98a/comments"
    }
    ```
    - 400 Bad Request (if request payload is not valid, OR if this POST_ID already exists)
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)


## Comment

### URL: ://api/author/{AUTHOR_ID}/posts/{POST_ID}/comments

- **GET**: Retrieve recent comments of this post *(default pagination size=5)*


  - Example request: `GET /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a3-67a8-4191-82da-91c85c72371b/comments`

  - Example response: 
    - 200 OK

    ```json
    {
        "type": "comments",
        "page": 1,
        "size": 5,
        "post": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb",
        "id": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb/comments",
        "comments": [
            {
                "type": "comment",
                "commentID": "e92b4bb5-b937-405c-b8a1-840aad7d036a",
                "content": "new comment from tester19",
                "author": {
                    "type": "author",
                    "authorID": "f9d8ccb2-b867-4eae-976a-e4e739e7ae38",
                    "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/",
                    "host": "https://cmput404-proj-social-app.herokuapp.com/",
                    "displayName": "tester19",
                    "github": "https://github.com/tester19.com"
                },
                "contentType": "text/plain",
                "published": "2021-12-06T06:06:11.786712Z"
            }
        ]
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post does not exist)

- **POST**: Create a comment to the post

  - Example request: `POST /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a3-67a8-4191-82da-91c85c72371b/comments`
    ```json
    {
      "content": "another comment",
      "contentType": "text/plain"
    }
    ```

  - Example response: 
    - 200 OK

    ```json
    {
        "type": "comment",
        "commentID": "d26390db-ad50-485c-ac0f-87efe9333dde",
        "content": "Team 19 test comment",
        "author": {
            "type": "author",
            "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e96e645d8bff370a2d052d31e/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "team19",
            "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
        },
        "contentType": "text/plain",
        "published": "2021-12-06T05:44:19.953226Z"
    }
    ```
    - 400 Bad Request (if request payload is not valid/missing nassesary field)
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post does not exist)


## Liked & Likes

### URL: ://api/author/{AUTHOR_ID}/liked

- **GET**: Retrieve all public things this author liked

  - Example request: `GET /api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/liked`

  - Example response:
    - 200 OK

    ```json
    {
        "items": [
            {
                "type": "like",
                "author": {
                    "type": "author",
                    "authorID": "f9d8ccb2-b867-4eae-976a-e4e739e7ae38",
                    "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/",
                    "host": "https://cmput404-proj-social-app.herokuapp.com/",
                    "displayName": "tester19",
                    "github": "https://github.com/tester19.com"
                },
                "summary": "tester19 Likes your post",
                "object": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a3-67a8-4191-82da-91c85c72371b"
            },
            {
                "type": "like",
                "author": {
                    "type": "author",
                    "authorID": "f9d8ccb2-b867-4eae-976a-e4e739e7ae38",
                    "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/",
                    "host": "https://cmput404-proj-social-app.herokuapp.com/",
                    "displayName": "tester19",
                    "github": "https://github.com/tester19.com"
                },
                "summary": "tester19 Likes your comment",
                "object": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a3-67a8-4191-82da-91c85c72371b/comments/bba10938-3778-4f68-a995-05b2be075d5b"
            }
        ]
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)

### URL: ://author/{AUTHOR_ID}/posts/{POST_ID}/likes

- **GET**: Get all likes of a post

  - Example request: `GET /api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/posts/cfead2ce-41b6-4021-af12-7f562d7fbe24/likes`

  - Example response:
    - 200 OK

    ```json
    {
        "items": [
            {
                "type": "like",
                "author": {
                    "type": "author",
                    "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
                    "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e96e645d8bff370a2d052d31e/",
                    "host": "https://cmput404-proj-social-app.herokuapp.com/",
                    "displayName": "team19",
                    "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
                },
                "summary": "team19 Likes your post",
                "object": "https://cmput404-proj-social-app.herokuapp.com/api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/posts/cfead2ce-41b6-4021-af12-7f562d7fbe24"
            }
        ]
    }
    ```

### URL: ://author/{AUTHOR_ID}/post/{POST_ID}/comments/{COMMENT_ID}/likes

- **GET**: Get all likes of a comment

  - Example request: `GET /api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/posts/cfead2ce-41b6-4021-af12-7f562d7fbe24/comments/2a82af06-28f3-4b1f-ac78-fcd37252e816/likes`

  - Example response:
    - 200 OK

    ```json  
    {
        "items": [
            {
                "type": "like",
                "author": {
                    "type": "author",
                    "authorID": "f9d8ccb2-b867-4eae-976a-e4e739e7ae38",
                    "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/",
                    "host": "https://cmput404-proj-social-app.herokuapp.com/",
                    "displayName": "tester19",
                    "github": "https://github.com/tester19.com"
                },
                "summary": "tester19 Likes your comment",
                "object": "https://cmput404-proj-social-app.herokuapp.com/api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/posts/cfead2ce-41b6-4021-af12-7f562d7fbe24/comments/2a82af06-28f3-4b1f-ac78-fcd37252e816"
            }
        ]
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)


## Follower & Friend

### URL: ://author/{AUTHOR_ID}/followers

- **GET**: Get author's followers

  - Example request: `GET /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/followees`

  - Example response:
    - 200 OK

    ```json
    {
        "type": "followers",
        "followee": {
            "type": "author",
            "authorID": "f9d8ccb2-b867-4eae-976a-e4e739e7ae38",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "tester19",
            "github": "https://github.com/tester19.com"
        },
        "follower": {
            "type": "author",
            "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e96e645d8bff370a2d052d31e/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "team19",
            "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
        }
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)

### URL: ://author/{AUTHOR_ID}/followees

- **GET**: Get author's followees

  - Example request: `/api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/followers`

  - Example response:
    - 200 OK

    ```json
    {
        "type": "followers",
        "followee": {
            "type": "author",
            "authorID": "f9d8ccb2-b867-4eae-976a-e4e739e7ae38",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "tester19",
            "github": "https://github.com/tester19.com"
        },
        "follower": {
            "type": "author",
            "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e96e645d8bff370a2d052d31e/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "team19",
            "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
        }
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)

### URL: ://author/{AUTHOR_ID}/friends

- **GET**: Get author's friends (follow for follow)

  - Example request: `GET /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/friends`

  - Example response:
    - 200 OK

    ```json
    {
        "type": "followers",
        "followee": {
            "type": "author",
            "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e96e645d8bff370a2d052d31e/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "team19",
            "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
        },
        "follower": {
            "type": "author",
            "authorID": "f9d8ccb2-b867-4eae-976a-e4e739e7ae38",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "tester19",
            "github": "https://github.com/tester19.com"
        }
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)

### URL: ://author/{AUTHOR_ID}/followers/{FOREIGN_AUTHOR_ID}

- **GET**: Check if the foreignAuthor is a follower of the author

  - Example request: `GET /api/author/1cd4b70d-b38b-4f45-bb75-4d2940d24532/followers/`

  - Example response:
    - 200 OK - relationship exist

    ```json
    {
        "type": "followers",
        "followee": {
            "type": "author",
            "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e96e645d8bff370a2d052d31e/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "team19",
            "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
        },
        "follower": {
            "type": "author",
            "authorID": "f9d8ccb2-b867-4eae-976a-e4e739e7ae38",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/f9d8ccb2-b867-4eae-976a-e4e739e7ae38/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "tester19",
            "github": "https://github.com/tester19.com"
        }
    }
    ```
    
    - 200 OK - relationship does not exist
    ```json
    []
    ```
    
    - 401 Unauthorized (if not logged in)
    
    - 404 Not Found (if such author does not exist)
    ```json
    {
        "detail": "f9d8ccb2-b867-4eae-976a-e4e739e7ae38 is not found "
    }
    ```
- **PUT**: Add a follower to author, foreignAuthor send a friend request to the author

  - Example request: `PUT /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/followers/04f36b6d-79ae-4e6d-83de-ccfb12e2647b`

  - Example response:
    - 200 OK

    ```json
    {
        "type": "followers",
        "followee": {
            "type": "author",
            "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e96e645d8bff370a2d052d31e/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "team19",
            "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
        },
        "follower": {
            "type": "author",
            "authorID": "04f36b6d-79ae-4e6d-83de-ccfb12e2647b",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/04f36b6d-79ae-4e6d-83de-ccfb12e2647b/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "gracetest",
            "github": "https://github.com/dashboard"
        }
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 400 BAD REQUEST (if foreignAuthor does not exist)

- **DELETE**: ForeignAuthor unfollowers the author, delete friend relationship between two authors

  - Example request: `DELETE /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/followers/04f36b6d-79ae-4e6d-83de-ccfb12e2647b`

  - Example response:
    - 200 OK
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post not exists)


## Inbox

### URL: ://author/{AUTHOR_ID}/inbox

- **GET**: Get all objects in author's inbox *(default pagination size=5)*

  - Example request: `GET /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/inbox`

  - Example response:
    - 200 OK

    ```json
    {
        "type": "inbox",
        "author": "https://cmput404-proj-social-app/api/author/3af2be83-2191-45e8-9ca2-2a8ae83b042c/",
        "items": []
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)

- **POST**: Add an object to author's inbox

  - Example request: `POST /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/inbox`
    
    ```json
    {
    "type": "post",
    "postID": "67a293a3-67a8-4191-82da-91c85c72371b"
    }
    ```
    - type options: `post`
    - object options: `postID`
    
  - Example response:
    - 200 OK

    ```json
    {
        "type": "post",
        "author": {
            "type": "author",
            "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e96e645d8bff370a2d052d31e/",
            "host": "https://cmput404-proj-social-app.herokuapp.com/",
            "displayName": "team19",
            "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
        },
        "object": {
            "type": "post",
            "title": "First Post",
            "postID": "67a293a3-67a8-4191-82da-91c85c72371b",
            "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a367a8419182da91c85c72371b",
            "author": {
                "type": "author",
                "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
                "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e96e645d8bff370a2d052d31e/",
                "host": "https://cmput404-proj-social-app.herokuapp.com/",
                "displayName": "team19",
                "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
            },
            "source": null,
            "origin": null,
            "description": "Team 19 first post",
            "contentType": "text/plain",
            "content": "Hello World!",
            "categories": null,
            "count": 0,
            "published": "2021-12-06T05:41:01.291443Z",
            "visibility": "PUBLIC",
            "unlisted": false,
            "likes": 0,
            "comments": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a367a8419182da91c85c72371b/comments"
        }
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)
