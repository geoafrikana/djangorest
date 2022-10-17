from django.urls import include, path

from . import views

urlpatterns = [
    path('students/', views.student_list ),
    path('students/<int:pk>', views.student_detail)
]