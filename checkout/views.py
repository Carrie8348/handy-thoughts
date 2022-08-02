from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    shopping_cart = request.session.get('shopping_cart', {})
    if not shopping_cart:
        messages.error(request,"There's nothing in your shopping cart")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HUQulGSUzkapEeIAnA4WnNlKPWynJaQCoyNPip6JuGD8S898ylIjwWmuQixvXltHCCS8NpeH5KeoiAiOgSP1CUo00OIWOCf8t',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)