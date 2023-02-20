from django.shortcuts import render
from .models import houseListingModel
# Create your views here.
"""
CRUD - Create, Read/Retrieve, Update, Delete, listing all elements
"""

# List all the houses
def houseListings(request):
    # select * from houseListingsModel/table
    listings = houseListingModel.objects.all()
    context = {
        "listings" : listings,
    }
    return render(request, 'listings.html', context)

# CRUD - Read/Retrieve
# View each house by itself
def retrieveDetails(request, pk):
    # Get the house by id
    specific_house = houseListingModel.objects.get(id = pk)
    context = {
        "specific" : specific_house
    }
    return render(request, 'details.html', context) 
