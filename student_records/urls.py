from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentRecordViewSet

router = DefaultRouter()
router.register(r'student-records', StudentRecordViewSet, basename='studentrecord')

urlpatterns = [
    path('', include(router.urls)),
]
