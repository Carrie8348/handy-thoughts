# Generated by Django 3.2.15 on 2022-08-22 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_remove_product_wishlist'),
        ('wishlist', '0002_auto_20220822_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(related_name='product_wishlists', through='wishlist.WishListItem', to='products.Product'),
        ),
    ]