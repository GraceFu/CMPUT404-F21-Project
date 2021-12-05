from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Post  #
from .models import Author
# from .models import Signup_Request  # need to implement
# Do we want the models in a directory or everything in the models.py file?
from .models import Comment
from .models import Like
from .models import Follower
# from .models import Friend  # need to implement
from .models import Inbox, InboxObject
from .models import Node

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
# admin.site.register(Friend)
admin.site.register(Inbox)
admin.site.register(InboxObject)
admin.site.register(Node)

# custom register
#admin.site.register(Signup_Request, signup_request_admin_list_view)
