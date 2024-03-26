from django.contrib.auth import get_user_model
from django.db import models

from django.urls import reverse

from categories.models import Category
from images.models import Image
from tags.models import Tag
from trip.utils import generate_unique_slug


class Trip(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    date = models.DateField(verbose_name='Date')
    title_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True,
                                    verbose_name='Title_photo')
    content = models.TextField(blank=True, verbose_name='Description')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Create time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Update time')
    published = models.BooleanField(verbose_name='Status')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='categories',
                                 verbose_name='Categories')
    tag = models.ManyToManyField(Tag, blank=True, related_name='tags', verbose_name='Tags')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='travelers',
                             null=True, default=None)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='images', verbose_name='Images',
                              null=True, default=None, blank=True)

    class Meta:
        db_table = 'trips'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('trip', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Trip, self.title)
        return super(Trip, self).save(*args, **kwargs)
