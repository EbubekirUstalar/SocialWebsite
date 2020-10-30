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


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     # followers = models.ForeignKey('self',on_delete=models.CASCADE, null=True, related_name='employee')
#     # followers = models.ForeignKey('self',on_delete=models.CASCADE, null=True, related_name='employee')
#     # friends = models.ManyToManyField(User)
#     # user = models.OneToOneField(User)  
#     #other fields here

#     def __str__(self):
#         return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# class CustomUser(AbstractUser):
#     pass
#     # add additional fields in here
#     # bio = models.CharField(max_length=200)

#     def __str__(self):
#         return self.username