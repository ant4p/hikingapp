# Generated by Django 5.0.3 on 2024-04-17 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trip',
            options={'ordering': ['-time_create']},
        ),
    ]