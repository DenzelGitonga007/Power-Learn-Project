from django.shortcuts import render
# Import the views
from . models import Product

# Create your views here.
# CRUD -- Create, Read, Update, Delete
# List the product
def product_listing(request):
    products = Product.objects.all()
    # Display the products to the fron-end
    context = {
        "product": products
    }
    return render(request, "listings_p.html", context)

# Product by detail
def product_details(request, pk):
    # product = Product.objects.get(pk=pk)
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
    }
    return render(request, "product_details.html", context)
