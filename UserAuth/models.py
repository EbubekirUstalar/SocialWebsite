from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User

# from django.contrib.auth.models import AbstractUser

# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=200)
    created_time = models.DateTimeField('date published')
    is_edited = models.BooleanField(default=False)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.text


# class UserProfile(models.Model):  
#     user = models.OneToOneField(User)  
#     #other fields here

#     def __str__(self):  
#     return "%s's profile" % self.user  

# class CustomUser(AbstractUser):
#     pass
#     # add additional fields in here
#     # bio = models.CharField(max_length=200)

#     def __str__(self):
#         return self.username