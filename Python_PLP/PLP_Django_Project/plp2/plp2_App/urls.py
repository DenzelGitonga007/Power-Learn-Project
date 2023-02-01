from django.urls import path
from . import views

urlpatterns = [
    path('application/', views.application_view, name="application") # name is form ref in templates

]