from django.shortcuts import render
# Import the forms
from .forms import ApplicationForm

# Create your views here.

def sunday_view(request):
    form = ApplicationForm()
    context = {
        'form_data': form
    }
    return render(request, 'application.html', context)
    