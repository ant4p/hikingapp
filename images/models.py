from django.db import models

from trip.models import Trip


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, blank=True, null=True, verbose_name='Image')
    travel = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='images', verbose_name='Images',
                               null=True, default=None, blank=True)

    class Meta:
        db_table = 'images'
