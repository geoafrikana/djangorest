from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', views.StudentViewSet)

urlpatterns = [
    # path('', views.StudentList.as_view()),
    path('v0/', include(router.urls))
    # path('<int:pk>', views.StudentDetail.as_view())
]