from django.db import models


# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=40, db_index=True)
    slug = models.SlugField(max_length=40, db_index=True, unique=True)

    def __str__(self):
        return self.tag
