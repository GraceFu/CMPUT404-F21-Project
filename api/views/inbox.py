from django.db.models import query
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.http.response import *
from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponseBadRequest
from django.shortcuts import redirect, get_object_or_404
from django.views import View

from api.models import Author, Like, Post, Follower, Inbox
from api.serializers import InboxSerializer
from api.utils import methods, generate_id, author_not_found, post_not_found
from api.paginaion import CustomPagiantor
from api.models import Inbox

from datetime import datetime, timezone
import json
import base64




""" put request data into instance 
auto-set fields: 

example of an working data:

{

}

"""

"""
class InboxViewSet(viewsets.GenericViewSet):

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    serializer_class = InboxSerializer
    queryset = {}

    @action(methods=[methods.GET], detail=True)
    def get_inbox_items(self, request, authorID):
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)

        # # get all comments that is owned by the post
        # items = Inbox.objects.all().order_by('-published')
        # pagination = CustomPagiantor()
        # qs = pagination.paginate_queryset(items, request)
        # serializer = InboxSerializer(qs, many=True)
        # res = {
        #     "type": "inbox",
        #     # "page": request.GET.get("page"),
        #     # "size": request.GET.get("size"),
        #     "items": [serializer.data]
        # }
        # return Response(res, status=status.HTTP_200_OK)

        queryset = Inbox.objects.filter(author=authorID).order_by('-published')
        
        serializer = InboxSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    @action(methods=[methods.POST], detail=True)
    def add_item_to_inbox(self, request):

        print("---------\n",request)
        type = request["type"]

        authorID = request["author"]
        if author_not_found(authorID):
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InboxSerializer(data=request)
        if serializer.is_valid():
            instance = Inbox(inboxID=generate_id())
            instance.author = Author.objects.get(authorID=authorID)
            instance.published = datetime.now().isoformat()
            if type == "post":
                instance.posts = request
            elif type == "follow":
                instance.requests = request
            elif type == "like":
                instance.likes = request
            instance.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

"""

class InboxView(viewsets.ViewSet):
    
    @login_required(login_url='login')
    def my_inbox_view(request):
    # Check the user is invalid in view
        if invalid_user_view(request):
            return redirect("login")
    
        
    
    def get(self, request, authorID):
        """ GET - Get list of inbox items to send to authorID inbox """

        try:
            page = request.GET.get("page")
            size = request.GET.get("size")
            author = get_object_or_404(LocalAuthor, id=authorID) ## get author object
            posts = author.inbox_posts.all().order_by('-published')

            if page and size:
                page = int(page)
                size = int(size)
                try:
                    if page < 1 or size < 1:
                        return HttpResponseBadRequest(" Page and size must be greater than 0")
                except Exception as e:
                    return HttpResponseBadRequest(e)

            posts = [post.as_json() for post in posts]

            response = {
                "type": "inbox",
                "author": author.url,
                "page": page,
                "size": size,
                "items": posts
            }

        except Http404:
            return HttpResponseNotFound()

        except Exception as e:
            return JsonResponse({
                "error": "An unknown error occurred"
            }, status=500)

        return JsonResponse(response)

    @login_required(login_url='login')
    def post(self, request, authorID):

        try:
            data = json.loads(request.body)

            if str(data["type"]).lower() == "post":

                received_post = Post.objects.get(postID=data["post"]) # get post from postID    
                
                # check if post is already in inbox
                if received_post in request.user.author.inbox_posts.all():
                    return HttpResponseBadRequest("Post is already in inbox")

                # check if post is already in author's posts
                if received_post in request.user.author.posts.all():
                    return HttpResponseBadRequest("Post is already in author's posts")

                
                receiving_author = get_object_or_404(LocalAuthor, id=author_id) ## get author object

                # add post to inbox of author
                receiving_author.inbox_posts.add(received_post)

                return HttpResponse(status=200)

            
            
            
            
            
            
            
            elif str(data["type"]).lower() == "follow":


                # user requests to follow object
                actor, obj = data["actor"], data["object"]

                object_id = #find the authorID of the follower
                if object_id == None:   # if authorID is not found  
                    return HttpResponseBadRequest("AuthorID not found")

                # check if user is already following the author     
                if actor in request.user.author.following.all():
                    return HttpResponseBadRequest("User is already following the author")

                # get or create actor author
                actor_author, created = Author.objects.get_or_create(
                    url = actor["id"]
                )

                # add or update remaining fields
                actor_author.update_with_json(data=actor)

                # add follow request
                object_author.follow_requests.add(actor_author)

                return HttpResponse(status=200)

            
            
            
            
            
            #########incomplete##############
            elif str(data["type"]).lower() == "like":

                # retrieve author
                liking_author, created = Author.objects.get_or_create(
                    url= data["author"]["id"]
                )

                # add or update remaining fields
                liking_author.update_with_json(data=data["author"])

                # add like  
                post = Post.objects.get(postID=data["post"])
                post.likes.add(liking_author)

                





            elif str(data["type"]).lower() == "comment":





                # retrieve author
                commenting_author, created = Author.objects.get_or_create(
                    url= data["author"]["id"]
                )


                # add or update remaining fields
                commenting_author.update_with_json(data=data["author"])

                # get the post
                post = Post.objects.get(postID=data["post"])

                # add comment
                post.comments.add(commenting_author)

                # add remote comment
                Comment.objects.create(
                    author = commenting_author,
                    post = post,
                    comment = data['comment'],
                    content_type = data['contentType'],
                    pub_date= datetime.now(timezone.utc),
                )

                return HttpResponse(status=200)
            else:
                raise ValueError("Unknown object sent to inbox")
        
        except json.decoder.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON"
            }, status=400)

        except Http404:
            return HttpResponseNotFound()



        except ValueError as e:
            return JsonResponse({
                "error": e.args[0]
            }, status=400)

        except Exception as e:
            return JsonResponse({
                "error": "An unknown error occurred"
            }, status=500)

    def delete(self, request, authorID):
        #clear inbox
        try:
            author = get_object_or_404(LocalAuthor, id=authorID)
            author.inbox_posts.clear()
            return HttpResponse("Clear inbox", status=200)
        except Http404:
            return HttpResponseNotFound()


        

