from django.shortcuts import render
from stock.models import Product

# Create your views here.

def index(request):
    """ A view to return the index page """
    # checks availability
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    context = {
        'products': products,
    }
    return render(request, 'home/index.html', context)

