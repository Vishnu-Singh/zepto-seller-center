#!/usr/bin/env python3
"""
Test script to demonstrate Zepto Seller Center APIs
"""
import json

def test_api_info():
    """Display API information"""
    print("=" * 70)
    print("ZEPTO SELLER CENTER API - Quick Start Guide")
    print("=" * 70)
    print("\n1. Start the development server:")
    print("   python manage.py runserver")
    print("\n2. Access the API root:")
    print("   http://localhost:8000/")
    print("\n3. Access Django Admin:")
    print("   http://localhost:8000/admin/")
    print("   (First create superuser: python manage.py createsuperuser)")
    
    print("\n" + "=" * 70)
    print("REST API ENDPOINTS")
    print("=" * 70)
    
    apps = {
        'Products': '/products/api/',
        'Orders': '/orders/api/',
        'Inventory': '/inventory/api/',
        'Shipping': '/shipping/api/',
        'Finance (Transactions)': '/finance/api/transactions/',
        'Finance (Payouts)': '/finance/api/payouts/',
        'Reports': '/reports/api/'
    }
    
    for app, endpoint in apps.items():
        print(f"\n{app}:")
        print(f"  - List: GET {endpoint}")
        print(f"  - Create: POST {endpoint}")
        print(f"  - Detail: GET {endpoint}{{id}}/")
        print(f"  - Update: PUT/PATCH {endpoint}{{id}}/")
        print(f"  - Delete: DELETE {endpoint}{{id}}/")
    
    print("\n" + "=" * 70)
    print("SOAP API ENDPOINTS")
    print("=" * 70)
    
    soap_endpoints = [
        '/products/soap/',
        '/orders/soap/',
        '/inventory/soap/',
        '/shipping/soap/',
        '/finance/soap/',
        '/reports/soap/'
    ]
    
    for endpoint in soap_endpoints:
        print(f"  - {endpoint}")
    
    print("\n" + "=" * 70)
    print("EXAMPLE API CALLS (using curl)")
    print("=" * 70)
    
    print("\n# Create a Product:")
    print("""curl -X POST http://localhost:8000/products/api/ \\
  -H "Content-Type: application/json" \\
  -d '{
    "sku": "PROD-001",
    "name": "Sample Product",
    "description": "A test product",
    "price": "99.99",
    "category": "Electronics",
    "status": "active"
  }'""")
    
    print("\n# List Products:")
    print("curl http://localhost:8000/products/api/")
    
    print("\n# Create an Order:")
    print("""curl -X POST http://localhost:8000/orders/api/ \\
  -H "Content-Type: application/json" \\
  -d '{
    "order_number": "ORD-001",
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "customer_phone": "+1234567890",
    "total_amount": "299.99",
    "shipping_address": "123 Main St",
    "billing_address": "123 Main St",
    "status": "pending"
  }'""")
    
    print("\n# Get SOAP WSDL:")
    print("curl http://localhost:8000/products/soap/")
    
    print("\n" + "=" * 70)
    print("TESTING")
    print("=" * 70)
    print("\nRun all tests:")
    print("  python manage.py test")
    print("\nRun specific app tests:")
    print("  python manage.py test products")
    print("  python manage.py test orders")
    print("  python manage.py test inventory")
    print("\n" + "=" * 70)


if __name__ == '__main__':
    test_api_info()
