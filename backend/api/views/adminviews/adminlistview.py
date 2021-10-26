from django.contrib import admin
from ..services.adminActions import accept_signup_request

# admin list view for signup requests
class signup_request_admin_list_view(admin.ModelAdmin):
    list_display = ['username','displayName', 'github', 'host']
    ordering = ['username']
    actions = [accept_signup_request]