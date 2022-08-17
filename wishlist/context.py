from .models import Wishlist
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

def global_variable(request):
    wishlist = []
    wishlist_product_ids = []

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(username=request.user)

        for product in Wishlist.objects.filter(user=user):
            if product.product.id not in cart_product_ids and product.product.id not in wishlist_product_ids:
                wishlist_product_ids.append(product.product.id)
                
        for product in Wishlist.objects.filter(user=user):
            if product.product.id not in cart_product_ids and product.product.id not in [product.product.id for product in wishlist]:
                wishlist.append(product)
        return {
        'wishlist': wishlist,
        'wishlist_product_ids': wishlist_product_ids
    }