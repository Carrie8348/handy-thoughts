from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from profiles.models import UserProfile
from products.models import Product
    
class Wishlist(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.product.product_name