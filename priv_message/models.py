from django.db import models
from django.contrib.auth.models import User
from socialnetwork.models import Users



class Inbox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    user_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    read = models.BooleanField(default=False)



class Thread(models.Model):
    thread = models.ForeignKey('Inbox', on_delete=models.CASCADE, blank=True, null=True, related_name='thread')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    body = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
