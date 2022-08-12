from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Reviews
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """
    view to add reviews to the database
    """
    # checks if user has permition to add products
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('products'))

    if request.method == 'POST':
    
        product = get_object_or_404(Product, pk=product_id)
        print(product)        
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.posted_by = request.user
            form.instance.product = product
            form.save()
            messages.success(request, 'review Added')
            return redirect(reverse('products',))
        else:
            messages.error(
                request,
                'The review was not added. Please check the form is valid.'
            )
    else:
        form = ReviewForm()

    template = 'reviews/add_reviews.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """
    view to edit review in the db
    """

    review = get_object_or_404(Reviews, pk=review_id)

    # checks if user has permition to add products
    if request.user != review.posted_by:
        messages.error(request, 'Sorry, only the user the created this review can do that.')
        return redirect(reverse('products'))
    review = get_object_or_404(Reviews, pk=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'item was updated')
            return redirect(reverse('products'))
        else:
            messages.error(
                request, 'review was not updated please'
                ' check the form is valid'
            )
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {review.title}')

    template = 'reviews/edit_reviews.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)
    



@login_required
def delete_review(request, review_id):
    """ Delete a blog from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do that.')
        return redirect(reverse('products'))

    review = get_object_or_404(Reviews, pk=review_id)
    review.delete()
    messages.success(request, f'{review.title} deleted!')
    return redirect(reverse('products'))
