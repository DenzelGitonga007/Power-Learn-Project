from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.sunday_view, name='form'),
    
]