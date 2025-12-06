"""
URL configuration for zepto_seller_center project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def api_root(request):
    """API root endpoint with links to all available APIs"""
    return JsonResponse({
        'message': 'Welcome to Zepto Seller Center API',
        'version': '1.0',
        'endpoints': {
            'products': {
                'rest_api': '/products/api/',
                'soap_api': '/products/soap/',
                'description': 'Product management APIs'
            },
            'orders': {
                'rest_api': '/orders/api/',
                'soap_api': '/orders/soap/',
                'description': 'Order management APIs'
            },
            'inventory': {
                'rest_api': '/inventory/api/',
                'soap_api': '/inventory/soap/',
                'description': 'Inventory management APIs'
            },
            'shipping': {
                'rest_api': '/shipping/api/',
                'soap_api': '/shipping/soap/',
                'description': 'Shipping and logistics APIs'
            },
            'finance': {
                'rest_api': '/finance/api/',
                'soap_api': '/finance/soap/',
                'description': 'Financial transaction and payout APIs'
            },
            'reports': {
                'rest_api': '/reports/api/',
                'soap_api': '/reports/soap/',
                'description': 'Analytics and reporting APIs'
            },
            'admin': '/admin/'
        }
    })


urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('inventory/', include('inventory.urls')),
    path('shipping/', include('shipping.urls')),
    path('finance/', include('finance.urls')),
    path('reports/', include('reports.urls')),
]
