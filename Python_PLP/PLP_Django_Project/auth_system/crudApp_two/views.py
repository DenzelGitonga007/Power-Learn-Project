from django.shortcuts import render
# Import the views
from . models import Product

# Create your views here.
# CRUD -- Create, Read, Update, Delete
def product_listing(request):
    products = Product.objects.all()
    # Display the products to the fron-end
    context = {
        "product": products
    }
    return render(request, "listing_p.html", context)