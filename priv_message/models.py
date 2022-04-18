from django.db import models
from django.contrib.auth.models import User


# Model for inbox with receiving threads
class Inbox(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+')
    user_receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+')


# Model for the messages and form
class Thread(models.Model):
    thread = models.ForeignKey(
        'Inbox', on_delete=models.CASCADE, blank=True, related_name='thread')
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receiver')
    body = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
