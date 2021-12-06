# API Endpoints Documentation

[Author](#author) <br>
[Post](#post) <br>
[Comment](#comment) <br>
[Liked & likes](#liked-&-likes) <br>
[Follower & Friend](#follower-friend) <br>
[Inbox](#inbox) <br>

## Author

### URL: ://api/authors/

- **GET**: Retrieve all authors on the server *(DEFAULT pagenation)*

  - Example request: `GET /api/authors/` with default pagination size=5

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

- **GET**: Retrieve recent posts of this author *(NO pagenation)*

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

- **GET**: Retrieve recent posts of this author *(WITH pagenation)*

    - Example request: `POST /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/?page=1&size=1`

    - Example response: 
      - 200 OK

      ```json
      {
          "items": [
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
                  "published": "2021-12-05T01:55:26.398274Z",
                  "visibility": "PUBLIC",
                  "unlisted": false,
                  "likes": 0,
                  "comments": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/ccf0b45d-47c5-4247-b7e4-a834b140f98a/comments"
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

- **GET**: Retrieve this public post

  - Example request: `GET /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb`

  - Example response: 
    - 200 OK
    
    ```json
    [
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
            "published": "2021-12-05T01:31:48.037419Z",
            "visibility": "PUBLIC",
            "unlisted": false,
            "likes": 0,
            "comments": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb/comments"
        }
    ]
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

- **GET**: Retrieve recent comments of this post *(DEFAULT pagenation)*

  - Example request: `GET /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a3-67a8-4191-82da-91c85c72371b/comments` with default pagenation of size=5

  - Example response: 
    - 200 OK

    ```json
    {
        "type": "comments",
        "page": 1,
        "size": 5,
        "post": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a3-67a8-4191-82da-91c85c72371b",
        "id": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a3-67a8-4191-82da-91c85c72371b/comments",
        "comments": [
            {
                "type": "comment",
                "commentID": "5fb7cef1-94af-43fe-bd6d-4ae32b59a74f",
                "content": "66666",
                "author": {
                    "type": "author",
                    "authorID": "e4801aff-10b2-43f0-a1dc-ca27dc94c7a9",
                    "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/e4801aff-10b2-43f0-a1dc-ca27dc94c7a9/",
                    "host": "https://cmput404-proj-social-app.herokuapp.com/",
                    "displayName": "tester19",
                    "github": "https://github.com/tester19.com"
                },
                "contentType": "text/plain",
                "published": "2021-12-05T02:00:17.688584Z"
            },
            {
                "type": "comment",
                "commentID": "6b94e09e-4181-4940-88a5-4d81e10d2cdb",
                "content": "Team 19 test comment",
                "author": {
                    "type": "author",
                    "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
                    "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
                    "host": "https://cmput404-proj-social-app.herokuapp.com/",
                    "displayName": "team19",
                    "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
                },
                "contentType": "text/plain",
                "published": "2021-12-05T01:57:29.416001Z"
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
    "commentID": "ebe83f74840e4a83a5c287e31db8be75",
    "content": "another comment",
    "author": {
        "type": "author",
        "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
        "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
        "host": "https://cmput404-proj-social-app.herokuapp.com/",
        "displayName": "team19",
        "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
    },
    "contentType": "text/plain",
    "published": "2021-12-05T02:14:36.202813"
}
    ```
    - 400 Bad Request (if request payload is not valid/missing nassesary field)
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post does not exist)


## Liked & Likes

### URL: ://api/author/{AUTHOR_ID}/liked

- **GET**: Retrieve all public things this author liked

  - Example request: `GET /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/liked`

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
                    "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
                    "host": "https://cmput404-proj-social-app.herokuapp.com/",
                    "displayName": "team19",
                    "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
                },
                "summary": "team19 Likes your comment",
                "object": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a3-67a8-4191-82da-91c85c72371b/comments/6b94e09e-4181-4940-88a5-4d81e10d2cdb"
            },
            {
                "type": "like",
                "author": {
                    "type": "author",
                    "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
                    "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/",
                    "host": "https://cmput404-proj-social-app.herokuapp.com/",
                    "displayName": "team19",
                    "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
                },
                "summary": "team19 Likes your post",
                "object": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a3-67a8-4191-82da-91c85c72371b"
            }
        ]
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)

Getting a list of likes from other authors on a post /author/{AUTHOR_ID}/post/{POST_ID}/likes GET

### URL: ://author/{AUTHOR_ID}/posts/{POST_ID}/likes

- **GET**: Get all likes of a post

  - Example request: `GET /api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/bf2c76dc-bcde-400a-9564-4fb062bf0ce6/likes`

  - Example response:
    - 200 OK

    ```json
    [
        {
            "type": "like",
            "author": {
                "type": "author",
                "authorID": "e4801aff-10b2-43f0-a1dc-ca27dc94c7a9",
                "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/e4801aff10b243f0a1dcca27dc94c7a9/",
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
                "authorID": "c7abd64e-96e6-45d8-bff3-70a2d052d31e",
                "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e96e645d8bff370a2d052d31e/",
                "host": "https://cmput404-proj-social-app.herokuapp.com/",
                "displayName": "team19",
                "github": "https://github.com/GraceFu/CMPUT404-F21-Project.com"
            },
            "summary": "team19 Likes your post",
            "object": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/67a293a3-67a8-4191-82da-91c85c72371b"
        }
    ]
    ```

### URL: ://author/{AUTHOR_ID}/post/{POST_ID}/comments/{COMMENT_ID}/likes

- **GET**: Get all likes of a comment

  - Example request: `GET /api/author/1cd4b70d-b38b-4f45-bb75-4d2940d24532/posts/226acb04-b62f-4b18-b20c-8feb2e490ebd/comments/4b8341d7-d2ea-49c6-9426-7b9f9cba12f5/likes`

  - Example response:
    - 200 OK

    ```json
    {
        "items": [
            {
                "type": "like",
                "author": {
                    "type": "author",
                    "authorID": "1cd4b70d-b38b-4f45-bb75-4d2940d24532",
                    "url": "https://cmput404-proj-social-app/api/author/1cd4b70d-b38b-4f45-bb75-4d2940d24532/",
                    "host": "https://cmput404-proj-social-app/",
                    "displayName": "andiTester",
                    "github": "https://github.com/zhininghjl.com"
                },
                "summary": "andiTester Likes your comment",
                "object": "https://cmput404-proj-social-app/api/author/1cd4b70d-b38b-4f45-bb75-4d2940d24532/posts/226acb04-b62f-4b18-b20c-8feb2e490ebd/comments/4b8341d7-d2ea-49c6-9426-7b9f9cba12f5"
            }
        ]
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)


## Follower & Friend

### URL: ://author/{AUTHOR_ID}/followers

- **GET**: Get author's followers

  - Example request: `GET /api/author/1cd4b70d-b38b-4f45-bb75-4d2940d24532/followers`

  - Example response:
    - 200 OK

    ```json

    ```

### URL: ://author/{AUTHOR_ID}/followees

- **GET**: Get author's followees

  - Example request: `GET /api/author/1cd4b70d-b38b-4f45-bb75-4d2940d24532/followees`

  - Example response:
    - 200 OK

    ```json

    ```

### URL: ://author/{AUTHOR_ID}/friends

- **GET**: Get author's friends (follow for follow)

  - Example request: `GET /api/author/1cd4b70d-b38b-4f45-bb75-4d2940d24532/friends`

  - Example response:
    - 200 OK

    ```json

    ```

### URL: ://author/{AUTHOR_ID}/followers/{FOREIGN_AUTHOR_ID}

- **GET**: Check if the foreign author is a follower of the author

  - Example request: `GET /api/author/1cd4b70d-b38b-4f45-bb75-4d2940d24532/followers/`

  - Example response:
    - 200 OK

    ```json

    ```
    
- **PUT**: Foreign author followers author / foreign author send a friend request to the author

  - Example request: `PUT /api/author/1cd4b70d-b38b-4f45-bb75-4d2940d24532/followers/`

  - Example response:
    - 200 OK

    ```json

    ```

- **DELETE**: Foreign author unfollowers author / delete friend relationship between two authors

  - Example request: `DELETE /api/author/1cd4b70d-b38b-4f45-bb75-4d2940d24532/followers/`

  - Example response:
    - 200 OK

    ```json

    ```


## Inbox

### URL: ://author/{AUTHOR_ID}/inbox

- **GET**: Get all object of author's inbox *(DEFAULT pagenation)*

  - Example request: `GET /api/author/1cd4b70d-b38b-4f45-bb75-4d2940d24532/inbox` with default pagination of size=5

  - Example response:
    - 200 OK

    ```json
    {
        "type": "inbox",
        "author": "https://cmput404-proj-social-app/api/author/3af2be83-2191-45e8-9ca2-2a8ae83b042c/",
        "items": [
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
            "published": "2021-12-05T01:31:48.037419Z",
            "visibility": "PUBLIC",
            "unlisted": false,
            "likes": 0,
            "comments": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb/comments"
        }
      ]
    }
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)

- **POST**: Add an object to author's inbox (post only for now)

  - Example request: `POST /api/author/1cd4b70d-b38b-4f45-bb75-4d2940d24532/inbox`
  ```json
    {
        "type": "post",
        "postID": "70d0a59b-4fee-4e84-b091-1b1161455ebb",
    }
  ```

  - Example response:
    - 200 OK
  ```json
    {
        "type": "post",
        "author": {
                "type": "author",
                "authorID": "e4801aff-10b2-43f0-a1dc-ca27dc94c7a9",
                "url": "https://cmput404-proj-social-app.herokuapp.com/api/author/e4801aff10b243f0a1dcca27dc94c7a9/",
                "host": "https://cmput404-proj-social-app.herokuapp.com/",
                "displayName": "tester19",
                "github": "https://github.com/tester19.com"
            },
        "object": {
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
            "published": "2021-12-05T01:31:48.037419Z",
            "visibility": "PUBLIC",
            "unlisted": false,
            "likes": 0,
            "comments": "https://cmput404-proj-social-app.herokuapp.com/api/author/c7abd64e-96e6-45d8-bff3-70a2d052d31e/posts/70d0a59b-4fee-4e84-b091-1b1161455ebb/comments"
        }
    }
    ```
  
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)
