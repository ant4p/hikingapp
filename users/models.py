from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True, verbose_name='Avatar')
    birthday = models.DateTimeField(blank=True, null=True, verbose_name='Birthday')
