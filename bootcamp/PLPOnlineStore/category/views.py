from django.shortcuts import render

# import the models
from . models import Category

# Create your views here.
def listCategory(request):
    # fetch all categories
    all_categories = Category.objects.all()

    # return them on the home page of the user
    return render(request, 'home/home.html', {all_categories})