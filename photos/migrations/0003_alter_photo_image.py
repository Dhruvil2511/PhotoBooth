# Generated by Django 4.2.6 on 2023-10-14 15:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp', 'webp', 'svg', 'tiff', 'tif', 'gif', 'heif'])]),
        ),
    ]
