# Generated by Django 3.2 on 2022-08-09 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_review_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
