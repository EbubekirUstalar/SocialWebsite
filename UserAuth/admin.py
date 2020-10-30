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

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ['email', 'username','bio']

# class ProfileAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('General information', {'fields': ['user', 'bio', 'followers']})
#     ]
#     # fieldsets = [
#     #     ('User information', {'fields': ['user.e_mail', 'user.user_name']})
#     # ]
#     list_display = ('user', 'bio')
#     # list_filter = ['user', 'bio']
#     search_fields = ['user']



admin.site.register(Post, PostAdmin)
# admin.site.register(Profile, ProfileAdmin)
# admin.site.unregister(User)
# admin.site.register(CustomUser, CustomUserAdmin)