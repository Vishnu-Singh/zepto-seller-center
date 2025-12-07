from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from .soap_views import product_soap_service

# REST API router
router = DefaultRouter()
router.register(r'', ProductViewSet, basename='product')

app_name = 'products'

urlpatterns = [
    # REST API endpoints
    path('api/', include(router.urls)),
    
    # SOAP endpoint
    path('soap/', product_soap_service, name='product-soap'),
]
