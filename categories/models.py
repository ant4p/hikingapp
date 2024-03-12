from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title
