
from django.urls import path

from . import views

app_name = 'UserAuth'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('userregister/', views.userregister, name='userregister'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('createpost/', views.createpost, name='createpost'),
    path('deletepost/<int:post_id>', views.deletepost, name='deletepost'),
    path('p/<int:profile_id>', views.profile, name='profile'),
]