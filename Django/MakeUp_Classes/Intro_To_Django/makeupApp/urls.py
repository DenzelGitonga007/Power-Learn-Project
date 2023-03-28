from django.urls import path
# Import the views
from . import views

urlpatterns = [
    path('', views.home, name="home")
]