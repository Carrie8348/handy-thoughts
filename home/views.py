from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def shipping(request):
    """ A view to return the shipping policy page """

    return render(request, 'home/shipping.html')

def about_us(request):
    """ A view to return the about us page """

    return render(request, 'home/about_us.html')