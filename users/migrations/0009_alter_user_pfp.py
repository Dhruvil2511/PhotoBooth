# Generated by Django 4.2.6 on 2023-10-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pfp',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='pfp/'),
        ),
    ]
