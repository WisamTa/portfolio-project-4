from django.db import models
from dj.choices import Choices, Choice
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Models for all posts
class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upload = CloudinaryField('image', blank=True, null=True)


# Models for all comments
class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


# Class for choosing a gender in the User class
class Gender(Choices):
    male = Choice("Male")
    female = Choice("Female")
    other = Choice("Other")


# Models for User profiles
class Users(models.Model):
    user = models.OneToOneField(
        User,
        primary_key=True,
        verbose_name='user',
        related_name='profile',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, blank=True, null=True)
    picture = CloudinaryField('image', default='placeholder')
    birthday = models.DateField(blank=True, null=True)
    gender = models.IntegerField(choices=Gender(),default=Gender.other.id)
    location = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)


"""
Using receiver for saving new registerd users in the database
for not getting errors when loggin in after created a new user.
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
