# API Endpoints Documentation

[Author List](#author-list) <br>
[Author](#author) <br>
[Post List](#post-list) <br>
[Post](#post) <br>
[Comment](#comment) <br>
[Liked List](#liked-list) <br>


## Author List

### URL: ://api/authors/

- **GET**: Retrieve all profiles on the server

  - Example request: GET ://api/authors/

  - Example response:
    - 200 OK

    ```
    [
        {
            "type": "author",
            "authorID": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
            "url": "localhost/author/34d9d2fad6844c9ea93399dd491b1689",
            "host": "localhost",
            "displayName": "sss",
            "github": "https://github.com/dashboard"
        },
        {
            "type": "author",
            "authorID": "3d716af0-898c-46ce-8087-253abc555ae0",
            "url": "localhost/author/3d716af0898c46ce8087253abc555ae0",
            "host": "localhost",
            "displayName": "fff",
            "github": "https://stackoverflow.com/questions/"
        }
    ]
    ```
    - 401 Unauthorized (if not logged in)


## Author

### URL: ://api/author/{AUTHOR_ID}/

- **GET**: Retrieve this author's profile

  - Example request: GET ://api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/

  - Example response: 
    - 200 OK

    ```
    {
    "type": "author",
    "authorID": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
    "url": "localhost/author/34d9d2fad6844c9ea93399dd491b1689",
    "host": "localhost",
    "displayName": "sss",
    "github": "https://github.com/dashboard"
    }     
    ```
    - 401 Unauthorized (if not logged in)

- **POST**: Update this author's profile

  - Example request: POST ://api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/
    ```
    {
    "displayName": "sssf",
    "github": "https://github.com/dashboard/sssf"
    }
    ```

  - Example response: 
    - 200 OK
    ```
    {
    "type": "author",
    "authorID": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
    "url": "localhost/author/34d9d2fad6844c9ea93399dd491b1689",
    "host": "localhost",
    "displayName": "sssf",
    "github": "https://github.com/dashboard/sssf"
    }
    ```
    - 400 Bad Request (if form is not valid)
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)


## Post List

### URL: ://api/author/{AUTHOR_ID}/posts/

- **GET**: Retrieve recent posts of this author

  - Example request: GET ://api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/posts/

  - Example response: 
    - 200 OK

    ```
    [
      {
        "type": "post",
        "title": "your title",
        "postID": "f89712a2-0862-4e2a-8473-f57593753514",
        "source": "https://uofa-cmput404.github.io/",
        "origin": "https://uofa-cmput404.github.io/",
        "description": "something magical",
        "contentType": "text/plain",
        "content": "this content",
        "author": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
        "categories": [
            "art",
            "palatte"
        ],
        "count": 0,
        "published": "2021-11-25T01:01:19.381675Z",
        "visibility": "PUBLIC",
        "unlisted": false
      },
      {
        "type": "post",
        "title": "the new title",
        "postID": "ed7c0f7e-bff5-4458-bb6c-06d26a6797c4",
        "source": "https://uofa-cmput404.github.io/",
        "origin": "https://uofa-cmput404.github.io/",
        "description": "my des 2.0",
        "contentType": "text/plain",
        "content": "my new content",
        "author": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
        "categories": [
            "web",
            "tutorial"
        ],
        "count": 0,
        "published": "2021-11-25T00:53:21.013210Z",
        "visibility": "PUBLIC",
        "unlisted": false
      }
    ]
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post does not exist)

- **POST**: Create a post with generated POST_ID

  - Example request: POST ://api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/posts/
    ```
    {
      "title": "the title",
      "source": "https://uofa-cmput404.github.io/",
      "origin": "https://uofa-cmput404.github.io/",
      "description": "my des",
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
    ```
    {
      "type": "post",
      "title": "the title",
      "postID": "ed7c0f7ebff54458bb6c06d26a6797c4",
      "source": "https://uofa-cmput404.github.io/",
      "origin": "https://uofa-cmput404.github.io/",
      "description": "my des",
      "contentType": "text/plain",
      "content": "my content",
      "author": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
      "categories": [
          "web",
          "tutorial"
      ],
      "count": 0,
      "published": "2021-11-25T00:53:21.013210",
      "visibility": "PUBLIC",
      "unlisted": false
    }
    ```
    - 400 Bad Request (if form is not valid)
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)


## Post

### URL: ://api/author/{AUTHOR_ID}/posts/{POST_ID}

- **GET**: Retrieve this public post

  - Example request: GET ://api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/posts/ed7c0f7ebff54458bb6c06d26a6797c4/

  - Example response: 
    - 200 OK

    ```
    [
      {
          "type": "post",
          "title": "the title",
          "postID": "ed7c0f7e-bff5-4458-bb6c-06d26a6797c4",
          "source": "https://uofa-cmput404.github.io/",
          "origin": "https://uofa-cmput404.github.io/",
          "description": "my des",
          "contentType": "text/plain",
          "content": "my content",
          "author": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
          "categories": [
              "web",
              "tutorial"
          ],
          "count": 0,
          "published": "2021-11-25T00:53:21.013210Z",
          "visibility": "PUBLIC",
          "unlisted": false
      }
    ]
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post does not exist)

- **POST**: Update this post

  - Example request: POST ://api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/posts/ed7c0f7ebff54458bb6c06d26a6797c4/
    ```
    {
      "title": "the new title",
      "description": "my des 2.0",
      "content": "my new content",
      "categories": [
          "web",
          "tutorial"
      ]
    }
    ```

  - Example response: 
    - 200 OK
    ```
    {
      "type": "post",
      "title": "the new title",
      "postID": "ed7c0f7e-bff5-4458-bb6c-06d26a6797c4",
      "source": "https://uofa-cmput404.github.io/",
      "origin": "https://uofa-cmput404.github.io/",
      "description": "my des 2.0",
      "contentType": "text/plain",
      "content": "my new content",
      "author": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
      "categories": [
          "web",
          "tutorial"
      ],
      "count": 0,
      "published": "2021-11-25T00:53:21.013210Z",
      "visibility": "PUBLIC",
      "unlisted": false
    } 
    ```
    - 400 Bad Request (if form is not valid)
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post does not exist)

- **DELETE**: Delete this post

  - Example request: DELETE ://api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/posts/ed7c0f7ebff54458bb6c06d26a6797c4/

  - Example response: 
    - 200 OK
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post not exists)

- **PUT**: Create a post with POST_ID

  - Example request: PUT ://api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/posts/f89712a208624e2a8473f57593753514/
    ```
    {
    "title": "your title",
    "source": "https://uofa-cmput404.github.io/",
    "origin": "https://uofa-cmput404.github.io/",
    "description": "something magical",
    "contentType": "text/plain",
    "content": "this content",
    "categories": ["art", "palatte"],
    "visibility": "PUBLIC",
    "unlisted": false
    }
    ```

  - Example response: 
    - 200 OK
    ```
    {
      "type": "post",
      "title": "your title",
      "postID": "f89712a208624e2a8473f57593753514",
      "source": "https://uofa-cmput404.github.io/",
      "origin": "https://uofa-cmput404.github.io/",
      "description": "something magical",
      "contentType": "text/plain",
      "content": "this content",
      "author": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
      "categories": [
          "art",
          "palatte"
      ],
      "count": 0,
      "published": "2021-11-25T01:01:19.381675",
      "visibility": "PUBLIC",
      "unlisted": false
    }
    ```
    - 400 Bad Request (if form is not valid, OR if this POST_ID already exists)
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)

## Comment

### URL: ://api/author/{AUTHOR_ID}/posts/{POST_ID}/comments

- **GET**: Retrieve recent comments of this post

  - Example request: GET ://api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/posts/f89712a2-0862-4e2a-8473-f57593753514/comments

  - Example response: 
    - 200 OK

    ```
    [
      {
        "type": "comment",
        "commentID": "3baf717d-e093-4dd1-b942-24f8d422a292",
        "content": "a comment",
        "author": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
        "post": "f89712a2-0862-4e2a-8473-f57593753514",
        "contentType": "text/plain"
      },
      {
        "type": "comment",
        "commentID": "443a9308-f9bd-40de-aa0f-7f749ef7d069",
        "content": "a new comment",
        "author": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
        "post": "f89712a2-0862-4e2a-8473-f57593753514",
        "contentType": "text/plain"
      }
    ]
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post does not exist)

- **POST**: Create a post with generated POST_ID

  - Example request: POST ://api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/posts/f89712a2-0862-4e2a-8473-f57593753514/comments
    ```
    {
      "content": "a comment",
      "contentType": "text/plain"
    }
    ```

  - Example response: 
    - 200 OK
    ```
    {
      "type": "comment",
      "commentID": "3baf717de0934dd1b94224f8d422a292",
      "content": "a comment",
      "author": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
      "post": "f89712a2-0862-4e2a-8473-f57593753514",
      "contentType": "text/plain"
    }
    ```
    - 400 Bad Request (if form is not valid)
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author or post does not exist)


## Liked List

### URL: ://api/author/{AUTHOR_ID}/liked

- **GET**: Retrieve all public things this author liked

  - Example request: GET ://api/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/liked/

  - Example response:
    - 200 OK

    ```
    [
      {
        "type": "like",
        "author": "34d9d2fa-d684-4c9e-a933-99dd491b1689",
        "summary": "sss likes your post",
        "object": localhost/author/34d9d2fa-d684-4c9e-a933-99dd491b1689/posts/f89712a208624e2a8473f57593753514/
      }
    ]
    ```
    - 401 Unauthorized (if not logged in)
    - 404 Not Found (if this author does not exist)