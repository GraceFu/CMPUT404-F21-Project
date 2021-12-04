from django.shortcuts import render, redirect
from django.contrib import messages

from rest_framework import status
from rest_framework.response import Response

from api.models import Author, Post
from api.utils import invalid_user_view
from ..forms import NewUserForm

# View of my posts
def profile_view(request, authorID):
    # Check the user is invalid in view
    if invalid_user_view(request):
        return redirect("login")

    content = {}

    # When the request method is GET
    if request.method == "GET":
        if str(request.user.author.authorID) == authorID:
            content['my_profile'] = True

    # When the request method is POST
    elif request.method == "POST":
        # Check the author is exist and the current user is the same author
        if authorID != str(request.user.author.authorID):
            messages.error(request, "Error. Unexpected user.")
            return redirect("logout")

        new_displayName = request.POST['displayName']
        try:
            if Author.objects.get(displayName=new_displayName):
                messages.error(request, "Unsuccessful update. DisplayName has been used, try aother displayName.")
        except:
            form = NewUserForm(request.POST, instance=Author.objects.get(authorID=authorID))
            if form.is_valid():
                form.save()
                messages.info(request, f"Your profile {authorID} has been update.")
            else:
                messages.error(request, "Unsuccessful update. Invalid information.")

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    author = Author.objects.filter(authorID=authorID).first()
    author_post = Post.objects.filter(author__exact=author, visibility__exact="PUBLIC").order_by('-published')
    content['author'] = author
    content['author_post'] = author_post
    content['current_authorID'] = request.user.author.authorID

    return render(request, "profile.html", content)
