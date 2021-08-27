from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    context = {}
    return render(request, 'home/index.html', context)

def cart(request):
    """ A view to return the cart page """
    context = {}
    return render(request, 'home/cart.html', context)

def checkout(request):
    """ A view to return the checkout page """
    context = {}
    return render(request, 'home/checkout.html', context)
