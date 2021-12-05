from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Post, Author, Comment, Like, Follower, Inbox, Node, Friend

#from .views.adminviews.adminlistview import signup_request_admin_list_view


class AuthorInline(admin.StackedInline):
    model = Author
    can_delete = False
    verbose_name_plural = "author"


class UserAdmin(BaseUserAdmin):
    inlines = (AuthorInline, )

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follower)
admin.site.register(Friend)
admin.site.register(Inbox)
admin.site.register(Node)

# custom register
#admin.site.register(Signup_Request, signup_request_admin_list_view)
