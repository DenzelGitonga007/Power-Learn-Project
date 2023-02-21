from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home") # views.home, home is for the home function in views
]