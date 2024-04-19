from django.db import models
from django.urls import reverse


# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=40, db_index=True)
    slug = models.SlugField(max_length=40, db_index=True, unique=True)

    class Meta:
        db_table = 'tags'
        ordering = ['-id']

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag:tag', kwargs={'slug': self.slug})
