from django.urls import path, include
from . import views

urlpatterns = [
    path('emps/', views.employeeView)
]
