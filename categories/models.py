from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cat:categories', kwargs={'slug': self.slug})
