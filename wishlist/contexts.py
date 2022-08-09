from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def wishlist_contents(request):
    wishlist_items = []

    wishlist = request.session.get('wishlist', {})

    for item_id, item_data in wishlist.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)

    context = {
        'wishlist_items': wishlist_items,
       
    }

    return context