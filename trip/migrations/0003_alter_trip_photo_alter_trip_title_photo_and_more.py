# Generated by Django 5.0.3 on 2024-03-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='title_photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Title_photo'),
        ),
        migrations.AlterModelTable(
            name='trip',
            table='trip',
        ),
    ]
