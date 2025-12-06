from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShipmentViewSet
from .soap_views import shipping_soap_service

router = DefaultRouter()
router.register(r'', ShipmentViewSet, basename='shipment')

app_name = 'shipping'

urlpatterns = [
    path('api/', include(router.urls)),
    path('soap/', shipping_soap_service, name='shipping-soap'),
]
