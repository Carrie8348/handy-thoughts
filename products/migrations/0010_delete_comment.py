# Generated by Django 3.2 on 2022-08-08 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
