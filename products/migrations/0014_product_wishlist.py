# Generated by Django 3.2 on 2022-08-11 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userprofile_image'),
        ('products', '0013_delete_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='wishlist', to='profiles.UserProfile'),
        ),
    ]
