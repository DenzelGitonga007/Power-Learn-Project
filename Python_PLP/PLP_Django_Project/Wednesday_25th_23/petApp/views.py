from django.shortcuts import render
from .models import Vaccine, Pet

# Create your views here.
def home(request):
    pets = Pet.objects.all() # select all from Pet table

    return render(request, 'home.html', {'pets': pets})
