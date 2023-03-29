from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.taskList, name="tasks"),
    path('detail/<int:pk>/', views.taskDetail, name="details")
]