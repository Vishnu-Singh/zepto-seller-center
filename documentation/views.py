from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import APIVersion, APIChange, SetupGuide
import subprocess
import os


def documentation_home(request):
    """Main documentation landing page"""
    context = {
        'latest_version': APIVersion.objects.filter(is_active=True).first(),
        'setup_guides': SetupGuide.objects.filter(is_published=True)[:5],
        'recent_changes': APIChange.objects.select_related('version')[:10],
    }
    return render(request, 'documentation/home.html', context)


def api_reference(request):
    """API reference documentation"""
    # Get all apps and their endpoints
    apps = [
        {
            'name': 'Products',
            'description': 'Product catalog management',
            'rest_endpoint': '/products/api/',
            'soap_endpoint': '/products/soap/',
            'models': ['Product', 'ProductImage', 'ProductAttribute'],
        },
        {
            'name': 'Orders',
            'description': 'Order processing and management',
            'rest_endpoint': '/orders/api/',
            'soap_endpoint': '/orders/soap/',
            'models': ['Order', 'OrderItem'],
        },
        {
            'name': 'Inventory',
            'description': 'Stock and warehouse management',
            'rest_endpoint': '/inventory/api/',
            'soap_endpoint': '/inventory/soap/',
            'models': ['InventoryItem', 'StockMovement'],
        },
        {
            'name': 'Shipping',
            'description': 'Logistics and shipment tracking',
            'rest_endpoint': '/shipping/api/',
            'soap_endpoint': '/shipping/soap/',
            'models': ['Shipment'],
        },
        {
            'name': 'Finance',
            'description': 'Transactions and payouts',
            'rest_endpoint': '/finance/api/transactions/',
            'soap_endpoint': '/finance/soap/',
            'models': ['Transaction', 'Payout'],
        },
        {
            'name': 'Reports',
            'description': 'Analytics and reporting',
            'rest_endpoint': '/reports/api/',
            'soap_endpoint': '/reports/soap/',
            'models': ['Report'],
        },
    ]
    
    context = {
        'apps': apps,
        'base_url': request.build_absolute_uri('/'),
    }
    return render(request, 'documentation/api_reference.html', context)


def setup_guide(request):
    """Setup and installation guide"""
    guides = SetupGuide.objects.filter(is_published=True)
    context = {
        'installation_guides': guides.filter(guide_type='installation'),
        'configuration_guides': guides.filter(guide_type='configuration'),
        'deployment_guides': guides.filter(guide_type='deployment'),
        'troubleshooting_guides': guides.filter(guide_type='troubleshooting'),
    }
    return render(request, 'documentation/setup_guide.html', context)


def changelog(request):
    """API changelog"""
    versions = APIVersion.objects.prefetch_related('changes').all()
    context = {
        'versions': versions,
    }
    return render(request, 'documentation/changelog.html', context)


@api_view(['GET'])
def api_versions(request):
    """API endpoint to get all versions"""
    versions = APIVersion.objects.all()
    data = [{
        'version': v.version,
        'release_date': v.release_date,
        'is_active': v.is_active,
        'description': v.description,
        'changes_count': v.changes.count(),
    } for v in versions]
    return Response(data)


@api_view(['GET'])
def api_changes_list(request):
    """API endpoint to get all API changes"""
    version = request.query_params.get('version')
    
    if version:
        changes = APIChange.objects.filter(version__version=version)
    else:
        changes = APIChange.objects.all()[:50]
    
    data = [{
        'version': c.version.version,
        'change_type': c.change_type,
        'app_name': c.app_name,
        'endpoint': c.endpoint,
        'title': c.title,
        'description': c.description,
        'created_at': c.created_at,
    } for c in changes]
    return Response(data)
