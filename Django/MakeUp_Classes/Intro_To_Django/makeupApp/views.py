from django.shortcuts import render
# Import the model
from . models import Person
# Create your views here.
# Home view
def home(request):
    # Fetch data
    persons = Person.objects.all()
    context = {
        "persons" : "persons"
    }
    
    return render(request, "home.html", context)


# "name" : "Denzel",
#         "email" : "denzel@gmail.com",
#         "age": 21,