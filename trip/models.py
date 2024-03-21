from django.contrib.auth import get_user_model
from django.db import models

from categories.models import Category
from images.models import Image
from tags.models import Tag
from users.models import User


# Create your models here.
class Trip(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    date = models.DateTimeField(verbose_name='Date')
    title_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True,
                                    verbose_name='Title_photo')
    content = models.TextField(blank=True, verbose_name='Description')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Create time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Update time')
    published = models.BooleanField(verbose_name='Status')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='categories',
                                 verbose_name='Categories')
    tag = models.ManyToManyField(Tag, blank=True, related_name='tags', verbose_name='Tags')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='travelers',
                             null=True, default=None)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='images', verbose_name='Images',
                              null=True, default=None)

    class Meta:
        db_table = 'trips'

    def __str__(self):
        return self.title
