from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductionRequestViewSet

router = DefaultRouter()
router.register(r'production-requests', ProductionRequestViewSet, basename='production-request')

urlpatterns = [
    path('', include(router.urls)),
]
