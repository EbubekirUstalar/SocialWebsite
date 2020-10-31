from django.contrib import admin
from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
from .models import Post
from django.contrib.auth.models import User

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information', {'fields': ['text', 'owner', 'likes']}),
        ('Date information', {'fields': ['created_time']}),
        ('Edit information', {'fields': ['is_edited']}),
    ]
    list_display = ('text', 'owner', 'likes', 'created_time', 'is_edited')
    list_filter = ['owner', 'likes', 'created_time', 'is_edited']
    search_fields = ['text']

admin.site.register(Post, PostAdmin)
