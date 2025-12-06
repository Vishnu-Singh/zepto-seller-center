from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportViewSet
from .soap_views import reports_soap_service

router = DefaultRouter()
router.register(r'', ReportViewSet, basename='report')

app_name = 'reports'

urlpatterns = [
    path('api/', include(router.urls)),
    path('soap/', reports_soap_service, name='reports-soap'),
]
