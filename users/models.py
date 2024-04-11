

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    UNDECIDED = 'U'
    MALE = 'M'
    FEMALE = 'F'
    ATTACK_HELICOPTER = 'H'
    GENDER_LIST = {
        'U': 'Undecided',
        'M': 'Male',
        'F': 'Female',
        'H': 'Attack Helicopter',
    }

    avatar = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True, verbose_name='Avatar')
    birthday = models.DateTimeField(blank=True, null=True, verbose_name='Birthday')
    gender = models.CharField(max_length=3, choices=GENDER_LIST, default=UNDECIDED)
