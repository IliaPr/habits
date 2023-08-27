from django.db import models
from django.contrib.auth.models import AbstractUser
from habits.models import NULLABLE



class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=35, verbose_name='фамилия')
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    chat_id = models.CharField(max_length=100, verbose_name='ID чата телеграмм', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
