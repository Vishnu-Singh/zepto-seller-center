from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet
from .soap_views import order_soap_service

# REST API router
router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

app_name = 'orders'

urlpatterns = [
    # REST API endpoints
    path('api/', include(router.urls)),
    
    # SOAP endpoint
    path('soap/', order_soap_service, name='order-soap'),
]
