# Generated by Django 3.2 on 2022-08-08 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
