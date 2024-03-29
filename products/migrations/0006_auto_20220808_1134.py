# Generated by Django 3.2 on 2022-08-08 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userprofile_image'),
        ('products', '0005_rename_productreview_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=140)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='profiles.userprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
