# Generated by Django 4.2.6 on 2023-10-13 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_user_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_profile_image',
            new_name='pfp',
        ),
    ]
