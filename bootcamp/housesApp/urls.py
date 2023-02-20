from django.urls import path
from . import views

urlpatterns = [
    path('', views.houseListings, name = "home"), # list all houses
    path('details/<pk>/', views.retrieveDetails, name = "details")
]       