from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = "customer_login"), # views.login, login is for the login function in views
    path('register', views.register, name = "customer_signup") # views.register, register is for the register function in views
]