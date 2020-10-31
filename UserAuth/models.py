from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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

