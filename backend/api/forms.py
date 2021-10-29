from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Author, Post
from .utils import generate_id


class NewUserForm(UserCreationForm):
    display_name = forms.CharField(
        max_length=100, help_text="Enter a name you want to display o.o", required=True)
    github = forms.URLField(help_text="Enter your GitHub link.")

    class Meta:
        model = User
        # password1 is the initial password, password2 is the password confirmation
        fields = ("username", "password1", "password2",
                  "display_name", "github")

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
