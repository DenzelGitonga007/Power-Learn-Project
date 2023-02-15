from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home_view, name="home"),
    # About
    path('about/', views.about_view, name="about"),
    # Menu
    path('menu/', views.menu_view, name="menu"),
    # Book
    path('book/', views.book_view, name="book"),
]