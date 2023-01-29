from django.shortcuts import render
# Import the forms
from .forms import ApplicationForm

# Create your views here.

def sunday_view(request):
    form = ApplicationForm()
    return render(request, 'application.html', {})