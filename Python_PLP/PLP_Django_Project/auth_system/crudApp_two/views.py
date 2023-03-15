from django.shortcuts import render, get_object_or_404, redirect
# Import the views
from . models import Product
# Import the product creation form'
from . forms import ProductCreateForm
# For reverse
from django.urls import reverse

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

# Creating the products
def product_create(request):
    # condition
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse("crudApp_two:listings"))
    else:
        form = ProductCreateForm()

    context = {
        "form": form
    }
    return render(request, "form_p.html", context)