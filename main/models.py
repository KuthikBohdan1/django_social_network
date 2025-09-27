from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Користувач'),
        ('moderator', 'Модератор'),
        ('admin', 'Адміністратор'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    avatar = models.ImageField(upload_to="avatars/",null=True, blank=True)
    user_nikname = models.CharField(max_length=64, null=False, blank=False)

class Post(models.Model):
    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
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

