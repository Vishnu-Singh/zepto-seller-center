# Zepto Seller Center - Technical Documentation

## Project Overview

This Django application provides a comprehensive API suite for managing seller operations in the Zepto platform. The project is organized into 6 specialized apps, each handling a specific domain of the seller center functionality.

## Architecture

### Technology Stack
- **Framework**: Django 6.0
- **API Framework**: Django REST Framework 3.16
- **Database**: SQLite (Development) / PostgreSQL (Production recommended)
- **SOAP Support**: Custom SOAP implementation using lxml
- **CORS**: django-cors-headers

### Application Structure

```
zepto-seller-center/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── README.md                    # User documentation
├── TECHNICAL_DOCS.md           # This file
├── api_demo.py                 # API demonstration script
├── .gitignore                  # Git ignore rules
│
├── zepto_seller_center/        # Main project configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Root URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── products/                   # Product management app
│   ├── models.py               # Product, ProductImage, ProductAttribute
│   ├── views.py                # REST API views
│   ├── soap_views.py           # SOAP API views
│   ├── serializers.py          # DRF serializers
│   ├── admin.py                # Django admin configuration
│   ├── tests.py                # Unit tests
│   ├── urls.py                 # URL routing
│   └── migrations/             # Database migrations
│
├── orders/                     # Order management app
│   ├── models.py               # Order, OrderItem
│   ├── views.py                # REST API views
│   ├── soap_views.py           # SOAP API views
│   ├── serializers.py          # DRF serializers
│   ├── admin.py                # Django admin configuration
│   ├── tests.py                # Unit tests
│   ├── urls.py                 # URL routing
│   └── migrations/             # Database migrations
│
├── inventory/                  # Inventory management app
│   ├── models.py               # InventoryItem, StockMovement
│   ├── views.py                # REST API views
│   ├── soap_views.py           # SOAP API views
│   ├── serializers.py          # DRF serializers
│   ├── admin.py                # Django admin configuration
│   ├── tests.py                # Unit tests
│   ├── urls.py                 # URL routing
│   └── migrations/             # Database migrations
│
├── shipping/                   # Shipping and logistics app
│   ├── models.py               # Shipment
│   ├── views.py                # REST API views
│   ├── soap_views.py           # SOAP API views
│   ├── serializers.py          # DRF serializers
│   ├── admin.py                # Django admin configuration
│   ├── tests.py                # Unit tests
│   ├── urls.py                 # URL routing
│   └── migrations/             # Database migrations
│
├── finance/                    # Financial management app
│   ├── models.py               # Transaction, Payout
│   ├── views.py                # REST API views
│   ├── soap_views.py           # SOAP API views
│   ├── serializers.py          # DRF serializers
│   ├── admin.py                # Django admin configuration
│   ├── tests.py                # Unit tests
│   ├── urls.py                 # URL routing
│   └── migrations/             # Database migrations
│
└── reports/                    # Analytics and reporting app
    ├── models.py               # Report
    ├── views.py                # REST API views
    ├── soap_views.py           # SOAP API views
    ├── serializers.py          # DRF serializers
    ├── admin.py                # Django admin configuration
    ├── tests.py                # Unit tests
    ├── urls.py                 # URL routing
    └── migrations/             # Database migrations
```

## Data Models

### Products App

**Product**
- SKU (unique identifier)
- Name, Description
- Price, Cost Price
- Category, Brand
- Status (active/inactive/pending)
- Weight
- Timestamps

**ProductImage**
- Foreign key to Product
- Image URL
- Primary flag
- Display order

**ProductAttribute**
- Foreign key to Product
- Attribute name/value pairs

### Orders App

**Order**
- Order number (unique)
- Customer information (name, email, phone)
- Status (pending, confirmed, processing, shipped, delivered, cancelled)
- Total amount
- Shipping/billing addresses
- Notes
- Timestamps

**OrderItem**
- Foreign key to Order
- Product SKU, name
- Quantity, unit price, total price

### Inventory App

**InventoryItem**
- Product SKU (unique)
- Product name
- Warehouse location
- Quantity available/reserved
- Reorder level/quantity
- Last restocked date
- Computed property: needs_reorder

**StockMovement**
- Foreign key to InventoryItem
- Movement type (in, out, adjustment, return)
- Quantity
- Reference number
- Notes
- Timestamp

### Shipping App

**Shipment**
- Tracking number (unique)
- Order number
- Carrier
- Status (pending, picked_up, in_transit, delivered, failed)
- Shipping address
- Estimated/actual delivery dates
- Timestamps

### Finance App

**Transaction**
- Transaction ID (unique)
- Type (sale, refund, fee, payout)
- Order number
- Amount, currency
- Description
- Timestamp

**Payout**
- Payout ID (unique)
- Amount, currency
- Status (pending, processing, completed, failed)
- Bank account
- Notes
- Created/completed timestamps

### Reports App

**Report**
- Report ID (unique)
- Type (sales, inventory, orders, finance)
- Status (pending, processing, completed, failed)
- Date range (start/end)
- File URL
- Created/completed timestamps

## API Design

### REST API Pattern

All REST APIs follow RESTful conventions:

```
GET    /app/api/           # List all resources
POST   /app/api/           # Create new resource
GET    /app/api/{id}/      # Retrieve specific resource
PUT    /app/api/{id}/      # Update resource (full)
PATCH  /app/api/{id}/      # Update resource (partial)
DELETE /app/api/{id}/      # Delete resource
```

### Custom Endpoints

Each app includes custom action endpoints:

**Products:**
- `GET /products/api/{id}/images/` - Get product images
- `GET /products/api/{id}/attributes/` - Get product attributes
- `GET /products/api/by_category/?category=X` - Filter by category

**Orders:**
- `GET /orders/api/{id}/items/` - Get order items
- `POST /orders/api/{id}/update_status/` - Update order status
- `GET /orders/api/by_status/?status=X` - Filter by status

**Inventory:**
- `GET /inventory/api/{id}/movements/` - Get stock movements
- `POST /inventory/api/{id}/adjust_stock/` - Adjust stock quantity
- `GET /inventory/api/low_stock/` - Get items needing reorder

**Shipping:**
- `POST /shipping/api/{id}/update_status/` - Update shipment status
- `GET /shipping/api/track/?tracking_number=X` - Track shipment

**Finance:**
- `GET /finance/api/transactions/by_type/?type=X` - Filter transactions
- `GET /finance/api/payouts/pending/` - Get pending payouts

**Reports:**
- `GET /reports/api/by_type/?type=X` - Filter reports
- `GET /reports/api/completed/` - Get completed reports

### SOAP API

Each app provides a SOAP endpoint at `/{app}/soap/`:
- GET request returns WSDL
- POST request accepts SOAP messages
- Returns XML responses in SOAP envelope format

## Admin Interface

Each app has a fully configured Django admin interface with:
- List views with filtering, searching, and sorting
- Detail views with inline editing for related models
- Organized fieldsets for better UX
- Read-only fields for computed values and timestamps

## Testing Strategy

### Test Coverage

Each app includes comprehensive tests:

1. **Model Tests**: Verify model creation, properties, and string representations
2. **API Tests**: Test all CRUD operations and custom endpoints
3. **SOAP Tests**: Verify SOAP endpoint accessibility

### Running Tests

```bash
# All tests
python manage.py test

# Specific app
python manage.py test products

# Verbose output
python manage.py test --verbosity=2

# With coverage
coverage run manage.py test
coverage report
```

## Configuration

### Settings

Key configuration in `settings.py`:

```python
# Installed apps
INSTALLED_APPS = [
    # Django defaults
    'django.contrib.admin',
    'django.contrib.auth',
    # ...
    
    # Third-party
    'rest_framework',
    'corsheaders',
    
    # Project apps
    'products',
    'orders',
    'inventory',
    'shipping',
    'finance',
    'reports',
]

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
}

# CORS (Development)
CORS_ALLOW_ALL_ORIGINS = True
```

### URL Configuration

URLs are organized hierarchically:
- Root: API information endpoint
- `/admin/`: Django admin
- `/{app}/api/`: REST API endpoints
- `/{app}/soap/`: SOAP API endpoints

## Development Workflow

### Initial Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Adding New Features

1. Update models in `models.py`
2. Create/update serializers in `serializers.py`
3. Add views in `views.py` and/or `soap_views.py`
4. Configure admin in `admin.py`
5. Write tests in `tests.py`
6. Run migrations if models changed
7. Run tests to verify

## Production Considerations

### Security

- Change `SECRET_KEY` in settings
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Use proper authentication (JWT, OAuth2)
- Enable HTTPS
- Update CORS settings to allow only specific origins
- Use environment variables for sensitive data

### Database

- Switch from SQLite to PostgreSQL or MySQL
- Configure connection pooling
- Set up regular backups
- Enable query logging for optimization

### Performance

- Enable caching (Redis, Memcached)
- Configure static/media file serving
- Use a production WSGI server (Gunicorn, uWSGI)
- Set up load balancing
- Optimize database queries
- Enable compression

### Monitoring

- Set up logging
- Configure error tracking (Sentry)
- Monitor API performance (New Relic, DataDog)
- Set up health check endpoints
- Configure alerts

## API Versioning

For production, consider implementing API versioning:

```python
# URL pattern
/api/v1/products/
/api/v2/products/

# Or header-based
Accept: application/vnd.zepto.v1+json
```

## Extension Points

The architecture supports easy extension:

1. **New Apps**: Follow the same pattern as existing apps
2. **Custom Actions**: Add `@action` decorators to ViewSets
3. **Middleware**: Add custom middleware for logging, auth, etc.
4. **Signals**: Use Django signals for cross-app communication
5. **Background Tasks**: Integrate Celery for async processing
6. **Webhooks**: Add webhook endpoints for event notifications

## Support

For issues or questions:
1. Check the README.md for usage instructions
2. Review test files for examples
3. Check Django and DRF documentation
4. Run `python api_demo.py` for quick reference

## License

This project is open source under the MIT License.
