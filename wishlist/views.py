from django.shortcuts import (render, redirect, reverse, HttpResponse, 
                            get_object_or_404, HttpResponseRedirect)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from products.models import Product
from profiles.models import UserProfile


# Create your views here.
@login_required
def view_wishlist(request):
    """ A view that renders the files page """

    products = Product.objects.filter(wishlist=request.user)

    return render(request, 'wishlist/view_wishlist.html', {"wishlist": products})


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    #if product.wishlist.filter(id=request.user.id).exists():
     #   product.wishlist.remove(request.user)
      #  messages.success(request, product.name + " has been removed from your WishList")
    #else:
    product.wishlist.add(request.user)
    messages.success(request, "Added " + str(product.id) + " to your WishList")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

