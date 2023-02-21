from django.shortcuts import render

# Create your views here.
# The home function
def home(request):
    return render(request, 'home/home.html', {}) # referencing the home.html in home folder in templates
