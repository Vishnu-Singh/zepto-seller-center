from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet
from .soap_views import inventory_soap_service

# REST API router
router = DefaultRouter()
router.register(r'', InventoryViewSet, basename='inventory')

app_name = 'inventory'

urlpatterns = [
    # REST API endpoints
    path('api/', include(router.urls)),
    
    # SOAP endpoint
    path('soap/', inventory_soap_service, name='inventory-soap'),
]
