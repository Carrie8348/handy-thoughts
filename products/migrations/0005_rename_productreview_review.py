# Generated by Django 3.2 on 2022-08-07 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productreview'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductReview',
            new_name='Review',
        ),
    ]
