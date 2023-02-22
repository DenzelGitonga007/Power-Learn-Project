from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CustomerSignUpForm
# Create your views here.
# login
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # already existing data
        if form.is_valid():
            # Fields to authenticate/confirm
            username = request.POST['username']
            password = request.POST['password']
            # Authenticate
            user = authenticate(username=username, password=password)
            if user is not None: # if user exits.authenticated
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
# register
def register(request):
    if request.method == 'POST': # If user posts data
        form = CustomerSignUpForm(request.POST)
        # Validate the fields in the customersignupform
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = CustomerSignUpForm()
    return render(request, 'registration/register.html', {'form':form})

# Logout
def logout(request):
    pass

