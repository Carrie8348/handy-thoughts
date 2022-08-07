from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.views import generic, View
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower
from .forms import ReviewForm

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

class product_detail(View):

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_id)
        reviews = product.reviews

        return render(
            request,
            "product_detail.html",
            {
                "product": product,
                "reviews": reviews,
                "reviewed": False,
                "reviews_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ A view to show individual product details """

        product = get_object_or_404(Product, pk=product_id)
        reviews = product.reviews

        reviews_form = ReviewForm(data=request.POST)
        if reviews_form.is_valid():
            reviews_form.instance.email = request.user.email
            reviews_form.instance.name = request.user.username
            reviews = reviews_form.save(commit=False)
            reviews.post = post
            reviews.save()
        else:
            reviews_form = ReviewForm()

        return render(
            request,
            "post_detail.html",
            {
                "product": product,
                "reviews": reviews,
                "reviewed": True,
                "reviews_form": reviews_form,
            },
        )
