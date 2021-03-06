from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Author, Comment, Post
from .utils import generate_id


class NewUserForm(UserCreationForm):
    displayName = forms.CharField(
        max_length=100, help_text="Enter a name you want to display o.o", required=True)
    github = forms.URLField(help_text="Enter your GitHub link.")

    class Meta:
        model = User
        # password1 is the initial password, password2 is the password confirmation
        fields = ("username", "password1", "password2",
                  "displayName", "github")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        # set user to be inactive first, admin needs to activate it before it can log in
        user.is_active = False
        if commit:
            user.save()
        return user


class NewPostForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Post
        fields = ['title', 'description',
                  'content', 'categories']

class NewCommentForm(forms.ModelForm):
    content = forms.CharField(max_length=500, required=True)

    class Meta:
        model = Comment
        fields = ['content', 'contentType']
