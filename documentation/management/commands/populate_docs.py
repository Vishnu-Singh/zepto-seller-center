"""
Script to populate initial documentation data
"""
from django.core.management.base import BaseCommand
from documentation.models import APIVersion, APIChange, SetupGuide
from datetime import date


class Command(BaseCommand):
    help = 'Populate initial documentation data'

    def handle(self, *args, **options):
        # Create initial version
        version, created = APIVersion.objects.get_or_create(
            version='v1.0.0',
            defaults={
                'release_date': date(2024, 12, 7),
                'is_active': True,
                'description': 'Initial release of Zepto Seller Center with 6 apps and dual API support'
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created version: {version.version}'))
            
            # Create changes for this version
            changes = [
                {
                    'change_type': 'feature',
                    'app_name': 'products',
                    'endpoint': '/products/api/',
                    'title': 'Product Management API',
                    'description': 'Complete REST and SOAP APIs for product catalog management including images and attributes'
                },
                {
                    'change_type': 'feature',
                    'app_name': 'orders',
                    'endpoint': '/orders/api/',
                    'title': 'Order Processing API',
                    'description': 'Order management with order items, status updates, and filtering capabilities'
                },
                {
                    'change_type': 'feature',
                    'app_name': 'inventory',
                    'endpoint': '/inventory/api/',
                    'title': 'Inventory Management API',
                    'description': 'Stock level tracking with movement history and low stock alerts'
                },
                {
                    'change_type': 'feature',
                    'app_name': 'shipping',
                    'endpoint': '/shipping/api/',
                    'title': 'Shipping & Logistics API',
                    'description': 'Shipment tracking with carrier information and delivery status'
                },
                {
                    'change_type': 'feature',
                    'app_name': 'finance',
                    'endpoint': '/finance/api/',
                    'title': 'Financial Management API',
                    'description': 'Transaction and payout tracking for seller financial operations'
                },
                {
                    'change_type': 'feature',
                    'app_name': 'reports',
                    'endpoint': '/reports/api/',
                    'title': 'Analytics & Reporting API',
                    'description': 'Generate and manage various business reports'
                },
            ]
            
            for change_data in changes:
                APIChange.objects.create(version=version, **change_data)
            
            self.stdout.write(self.style.SUCCESS(f'Created {len(changes)} changes'))
        else:
            self.stdout.write(self.style.WARNING(f'Version {version.version} already exists'))
        
        # Create setup guides
        guides = [
            {
                'title': 'Quick Start Guide',
                'guide_type': 'installation',
                'content': '''Follow these steps to get started:

1. Clone the repository
2. Install dependencies: pip install -r requirements.txt
3. Run migrations: python manage.py migrate
4. Create superuser: python manage.py createsuperuser
5. Start server: python manage.py runserver

Access the API at http://localhost:8000/''',
                'order': 1
            },
            {
                'title': 'Environment Variables',
                'guide_type': 'configuration',
                'content': '''Configure the following environment variables:

- SECRET_KEY: Django secret key (required for production)
- DEBUG: Set to False in production
- ALLOWED_HOSTS: Comma-separated list of allowed hosts
- DATABASE_URL: Database connection string (optional)

For development, these are pre-configured in settings.py''',
                'order': 2
            },
            {
                'title': 'Production Deployment',
                'guide_type': 'deployment',
                'content': '''Steps for production deployment:

1. Set DEBUG=False
2. Configure proper SECRET_KEY
3. Set ALLOWED_HOSTS
4. Use PostgreSQL or MySQL database
5. Configure Gunicorn or uWSGI
6. Set up Nginx reverse proxy
7. Enable HTTPS with SSL certificate
8. Configure static file serving
9. Set up database backups
10. Configure logging and monitoring''',
                'order': 3
            },
            {
                'title': 'Common Issues',
                'guide_type': 'troubleshooting',
                'content': '''Common issues and solutions:

**Import Error: No module named 'django'**
Solution: Install dependencies with pip install -r requirements.txt

**Database Error**
Solution: Run python manage.py migrate

**Permission Denied (403)**
Solution: Check REST_FRAMEWORK permissions in settings.py

**CORS Errors**
Solution: Configure CORS_ALLOWED_ORIGINS in settings.py''',
                'order': 4
            },
        ]
        
        guides_created = 0
        for guide_data in guides:
            guide, created = SetupGuide.objects.get_or_create(
                title=guide_data['title'],
                defaults=guide_data
            )
            if created:
                guides_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {guides_created} setup guides'))
        self.stdout.write(self.style.SUCCESS('Documentation data populated successfully!'))
