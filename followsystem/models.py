from django.db import models
from django.contrib.auth.models import User
from socialnetwork import models


class Followers(models.Model):
    follower = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    def __str__(self):
        return self.user