from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    description = models.TextField()
    media = models.FileField(upload_to="posts/media/")
    date_publish = models.DateTimeField(auto_now_add=True)

class Post_like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.IntegerField()
    def __str__(self):
        return self.like

class Coment_Post(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    media = models.FileField(upload_to="coment_post/")
    date_publish = models.DateTimeField(auto_now_add=True)

