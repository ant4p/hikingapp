from django.contrib.auth import get_user_model
from django.db import models

from categories.models import Category
from tags.models import Tag


# Create your models here.
class Trip(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    title_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True,
                                    verbose_name='Title_photo')
    content = models.TextField(blank=True, verbose_name='Description')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Create time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Update time')
    published = models.BooleanField(verbose_name='Status')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, blank=True, null=True, verbose_name='Photo')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='trips',
                                 verbose_name='Categories')
    tag = models.ManyToManyField(Tag, blank=True, related_name='tags', verbose_name='Tags')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='traveler',
                             null=True, default=None)

    class Meta:
        db_table = 'trip'

    def __str__(self):
        return self.title
