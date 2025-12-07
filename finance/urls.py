from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, PayoutViewSet
from .soap_views import finance_soap_service

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'payouts', PayoutViewSet, basename='payout')

app_name = 'finance'

urlpatterns = [
    path('api/', include(router.urls)),
    path('soap/', finance_soap_service, name='finance-soap'),
]
