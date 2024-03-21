# Generated by Django 5.0.3 on 2024-03-21 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('trip', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='image',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='images.image', verbose_name='Images'),
        ),
    ]
