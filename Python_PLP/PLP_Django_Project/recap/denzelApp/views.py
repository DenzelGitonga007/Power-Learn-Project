from django.shortcuts import render

# Create your views here.

# Home view
def home_view(request):
    # filter
    name = {
        "first_name": "Denzel",
    }
    return render(request, 'home.html', name)

# About view
def about_view(request):
    return render(request, 'about.html', {})

# Menu view
def menu_view(request):
    return render(request, 'menu.html', {})

# Book view
def book_view(request):
    return render(request, 'book.html', {})