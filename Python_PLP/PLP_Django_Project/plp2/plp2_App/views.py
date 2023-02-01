from django.shortcuts import render
from .forms import ApplicationForm

# Create your views here.
def application_view(request):
    form = ApplicationForm() # call the application form
    # Check the method to be post
    if request.method == 'POST':
        # populate the form with the details
        form = ApplicationForm(request.POST)
        # check if the details are valid
        if form.is_valid():
            form.save()
    context = {
        "form_data": form # hold every info from the form
    }
    # if all is successfully
    return render(request, 'application.html', context)