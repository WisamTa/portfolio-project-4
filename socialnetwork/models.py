from django.db import models
from dj.choices import Choices, Choice
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Models for all posts
class Post(models.Model):
    body = models.TextField(max_length="500")
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upload = CloudinaryField('image', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def number_of_likes(self):
        return self.likes.count()


# Models for all comments
class Comment(models.Model):
    comment = models.TextField(max_length="500")
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def number_of_comments(self):
        return self.comment.count()


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
    gender = models.IntegerField(choices=Gender(), default=Gender.other.id)
    location = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    followers = models.ManyToManyField(
        User, blank=True, related_name='followers')

    def number_of_followers(self):
        return self.followers.count()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Using receiver for saving new registerd users in the database
    for not getting errors when loggin in after created a new user.
    """
    if created:
        Users.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
