from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.product_listing, name="listings"), # list all products
    path('details/<int:pk>/', views.product_details, name="details"),
    path('create/', views.product_create, name="create"),
]