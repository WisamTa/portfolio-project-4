from django.db import models
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    Comment = models.TextField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
       author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    body = models.TextField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
