from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, blank=True, null=True, verbose_name='Image')

    class Meta:
        db_table = 'images'


