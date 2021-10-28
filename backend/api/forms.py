from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Author, Post
from .utils import generate_id


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # password1 is the initial password, password2 is the password confirmation
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        # set user to be inactive first, admin needs to activate it before it can log in
        user.is_active = False
        if commit:
            user.save()
        return user


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description',
                  'content', 'categories', 'visibility']
