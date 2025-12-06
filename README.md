# Zepto Seller Center

A full-featured Django application for managing Zepto seller operations with both REST and SOAP APIs.

## Features

- **6 App Modules** based on API classifications:
  - **Products**: Product catalog management
  - **Orders**: Order processing and management
  - **Inventory**: Stock and warehouse management
  - **Shipping**: Logistics and shipment tracking
  - **Finance**: Transactions and payouts
  - **Reports**: Analytics and reporting

- **Dual API Support**:
  - REST API (using Django REST Framework)
  - SOAP API (using Spyne)

- **Admin Panel**: Full Django admin interface for each app

- **Comprehensive Tests**: Unit tests for all endpoints

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Vishnu-Singh/zepto-seller-center.git
cd zepto-seller-center
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### REST API Endpoints

All REST APIs follow the pattern: `/{app}/api/`

**Products:**
- `GET /products/api/` - List all products
- `POST /products/api/` - Create a product
- `GET /products/api/{id}/` - Get product details
- `PUT /products/api/{id}/` - Update product
- `DELETE /products/api/{id}/` - Delete product
- `GET /products/api/{id}/images/` - Get product images
- `GET /products/api/{id}/attributes/` - Get product attributes
- `GET /products/api/by_category/?category={category}` - Filter by category

**Orders:**
- `GET /orders/api/` - List all orders
- `POST /orders/api/` - Create an order
- `GET /orders/api/{id}/` - Get order details
- `PUT /orders/api/{id}/` - Update order
- `DELETE /orders/api/{id}/` - Delete order
- `GET /orders/api/{id}/items/` - Get order items
- `POST /orders/api/{id}/update_status/` - Update order status
- `GET /orders/api/by_status/?status={status}` - Filter by status

**Inventory:**
- `GET /inventory/api/` - List all inventory items
- `POST /inventory/api/` - Create inventory item
- `GET /inventory/api/{id}/` - Get inventory details
- `PUT /inventory/api/{id}/` - Update inventory
- `DELETE /inventory/api/{id}/` - Delete inventory
- `GET /inventory/api/{id}/movements/` - Get stock movements
- `POST /inventory/api/{id}/adjust_stock/` - Adjust stock quantity
- `GET /inventory/api/low_stock/` - Get low stock items

**Shipping:**
- `GET /shipping/api/` - List all shipments
- `POST /shipping/api/` - Create shipment
- `GET /shipping/api/{id}/` - Get shipment details
- `PUT /shipping/api/{id}/` - Update shipment
- `POST /shipping/api/{id}/update_status/` - Update shipment status
- `GET /shipping/api/track/?tracking_number={number}` - Track shipment

**Finance:**
- `GET /finance/api/transactions/` - List all transactions
- `POST /finance/api/transactions/` - Create transaction
- `GET /finance/api/transactions/{id}/` - Get transaction details
- `GET /finance/api/transactions/by_type/?type={type}` - Filter by type
- `GET /finance/api/payouts/` - List all payouts
- `GET /finance/api/payouts/pending/` - Get pending payouts

**Reports:**
- `GET /reports/api/` - List all reports
- `POST /reports/api/` - Create report
- `GET /reports/api/{id}/` - Get report details
- `GET /reports/api/by_type/?type={type}` - Filter by type
- `GET /reports/api/completed/` - Get completed reports

### SOAP API Endpoints

All SOAP APIs are available at: `/{app}/soap/`

- `/products/soap/` - Product SOAP services
- `/orders/soap/` - Order SOAP services
- `/inventory/soap/` - Inventory SOAP services
- `/shipping/soap/` - Shipping SOAP services
- `/finance/soap/` - Finance SOAP services
- `/reports/soap/` - Reports SOAP services

You can view WSDL by accessing the SOAP endpoints.

## Admin Panel

Access the admin panel at: `http://localhost:8000/admin/`

Each app has a dedicated admin interface with:
- List views with filtering and search
- Detail views with inline editing
- Custom fieldsets for better organization

## Running Tests

Run all tests:
```bash
python manage.py test
```

Run tests for a specific app:
```bash
python manage.py test products
python manage.py test orders
python manage.py test inventory
python manage.py test shipping
python manage.py test finance
python manage.py test reports
```

## Project Structure

```
zepto-seller-center/
├── manage.py
├── requirements.txt
├── README.md
├── zepto_seller_center/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/
│   ├── models.py
│   ├── views.py
│   ├── soap_views.py
│   ├── serializers.py
│   ├── admin.py
│   ├── tests.py
│   └── urls.py
├── orders/
│   ├── models.py
│   ├── views.py
│   ├── soap_views.py
│   ├── serializers.py
│   ├── admin.py
│   ├── tests.py
│   └── urls.py
├── inventory/
│   ├── models.py
│   ├── views.py
│   ├── soap_views.py
│   ├── serializers.py
│   ├── admin.py
│   ├── tests.py
│   └── urls.py
├── shipping/
│   ├── models.py
│   ├── views.py
│   ├── soap_views.py
│   ├── serializers.py
│   ├── admin.py
│   ├── tests.py
│   └── urls.py
├── finance/
│   ├── models.py
│   ├── views.py
│   ├── soap_views.py
│   ├── serializers.py
│   ├── admin.py
│   ├── tests.py
│   └── urls.py
└── reports/
    ├── models.py
    ├── views.py
    ├── soap_views.py
    ├── serializers.py
    ├── admin.py
    ├── tests.py
    └── urls.py
```

## Technologies Used

- **Django 6.0**: Web framework
- **Django REST Framework 3.16**: REST API framework
- **Spyne 2.14**: SOAP web services framework
- **lxml**: XML processing
- **django-cors-headers**: CORS handling

## Development

To contribute to this project:

1. Create a new branch for your feature
2. Make your changes
3. Write tests for your changes
4. Run all tests to ensure nothing breaks
5. Submit a pull request

## License

This project is open source and available under the MIT License.
