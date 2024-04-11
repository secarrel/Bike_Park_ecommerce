# Generated by Django 5.0.3 on 2024-04-11 08:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_activity_image_url_category_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='activity'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='category'),
        ),
    ]
