from django.db import models
from django.core.validators import MinLengthValidator

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
        ('neactive', 'Неактивний')
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOUSES, default='active')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    avatar = models.ImageField(upload_to="avatars/",null=True, blank=True)
    username = models.CharField(max_length=150,
        unique=True,
        validators=[MinLengthValidator(5)],
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": ("A user with that username already exists."),})
    
    def __str__(self):
        return self.email