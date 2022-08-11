from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from profiles.models import UserProfile

class Category(models.Model):
    """
    Category Model
    """
    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    """
    Product Model
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="wishlist", blank=True)


    def __str__(self):
        return self.name
