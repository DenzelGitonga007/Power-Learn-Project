from django.shortcuts import render
from .models import houseListingModel
# Create your views here.
"""
CRUD - Create, Read/Retrieve, Update, Delete 
"""
def houseListings(request):
    # select * from houseListingsModel/table
    listings = houseListingModel.objects.all()
    context = {
        "listings" : listings
    }
    return render(request, 'listings.html', context)
