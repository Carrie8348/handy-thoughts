from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.
def view_shopping_cart(request):
    """ A view that renders the shopping cart contents page """

    return render(request, 'shopping_cart/shopping_cart.html')

def add_to_shopping_cart(request, item_id):
    """
    Add quantity to shopping cart
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_cart = request.session.get('shopping_cart', {})

    if item_id in list(shopping_cart.keys()):
        shopping_cart[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity!')
    else:
        shopping_cart[item_id] = quantity
        messages.success(request, f'{product.name} was added to your shopping cart!')

    request.session['shopping_cart'] = shopping_cart
    return redirect(redirect_url)