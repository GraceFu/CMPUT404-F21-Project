from django.contrib import admin
from .models import Post
from .models import Author
from .models import Signup_Request
from .models import Comment           ###Do we want the models in a directory or everything in the models.py file?
from .models import Like
from .models import Follower
from .models import Friend
from .models import Inbox
from .models import Node

from views.admin.adminlistview import signup_request_admin_list_view




# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follower)
admin.site.register(Friend)
admin.site.register(Inbox)
admin.site.register(Node)

# custom register
admin.site.register(Signup_Request, signup_request_admin_list_view)