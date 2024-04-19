from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from trip.models import Trip


class Image(models.Model):
    image = ThumbnailerImageField(upload_to='photos/%Y/%m/%d', default=None, blank=True, null=True, verbose_name='Image')
    travel = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='imagesss', verbose_name='Images',
                               null=True, default=None, blank=True)

    class Meta:
        db_table = 'images'
