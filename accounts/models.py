from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Користувач'),
        ('moderator', 'Модератор'),
        ('admin', 'Адміністратор'),
    )
    STATUS_CHOUSES = (
        ('active','Активний'),
        ('blocked','Заблокований'),
        ('normal','Нормальний'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOUSES, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    avatar = models.ImageField(upload_to="avatars/",null=True, blank=True)
    user_nikname = models.CharField(max_length=64, null=False, blank=False)
