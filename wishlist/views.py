from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from products.models import Product
from profiles.models import UserProfile
from wishlist.contexts import wishlist_contents

# Create your views here.
@login_required
def view_wishlist(request):
    """ A view that renders the wishlist contents page """

    return render(request, 'wishlist/wishlist.html')

@login_required
def add_to_wishlist(request, item_id):
    """ Add a quantity of the specified product to the wishlist """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        messages.warning(request, f'The {product.name} is already in your wishlist')
    else:
        messages.success(request, f'Added {product.name} to your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)

@login_required
def remove_from_wishlist(request, item_id):
    """Remove the item from the wishlist"""

    try:
         product = get_object_or_404(Product, pk=item_id)
         wishlist = request.session.get('wishlist', {})

         wishlist.pop(item_id)
         messages.success(request, f'Removed {product.name} from your wishlist')

         request.session['wishlist'] = wishlist
         return HttpResponse(status=200)

    except Exception as e:
            messages.error(request, f'Error removing item: {e}')
            return HttpResponse(status=500)