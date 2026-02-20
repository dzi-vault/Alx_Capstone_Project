from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManufacturerProfileViewSet

router = DefaultRouter()
router.register(r'manufacturers', ManufacturerProfileViewSet, basename='manufacturer')

urlpatterns = [
    path('', include(router.urls)),
]
