from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Order, OrderItem


class OrderModelTest(TestCase):
    """Test Order model"""
    
    def setUp(self):
        self.order = Order.objects.create(
            order_number='ORD-001',
            customer_name='John Doe',
            customer_email='john@example.com',
            customer_phone='+1234567890',
            status='pending',
            total_amount=299.99,
            shipping_address='123 Main St, City',
            billing_address='123 Main St, City'
        )
    
    def test_order_creation(self):
        """Test order is created correctly"""
        self.assertEqual(self.order.order_number, 'ORD-001')
        self.assertEqual(self.order.customer_name, 'John Doe')
        self.assertEqual(self.order.status, 'pending')
    
    def test_order_str(self):
        """Test order string representation"""
        self.assertEqual(str(self.order), 'Order ORD-001 - John Doe')


class OrderAPITest(APITestCase):
    """Test Order REST API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.order = Order.objects.create(
            order_number='API-ORD-001',
            customer_name='Jane Smith',
            customer_email='jane@example.com',
            customer_phone='+1987654321',
            status='confirmed',
            total_amount=499.99,
            shipping_address='456 Oak Ave, Town',
            billing_address='456 Oak Ave, Town'
        )
    
    def test_get_orders_list(self):
        """Test retrieving list of orders"""
        url = '/orders/api/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_order_detail(self):
        """Test retrieving a single order"""
        url = f'/orders/api/{self.order.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['order_number'], 'API-ORD-001')
    
    def test_create_order(self):
        """Test creating a new order"""
        url = '/orders/api/'
        data = {
            'order_number': 'NEW-ORD-001',
            'customer_name': 'Test Customer',
            'customer_email': 'test@example.com',
            'customer_phone': '+1111111111',
            'status': 'pending',
            'total_amount': 199.99,
            'shipping_address': '789 Pine St',
            'billing_address': '789 Pine St'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update_order_status(self):
        """Test updating order status"""
        url = f'/orders/api/{self.order.id}/update_status/'
        data = {'status': 'shipped'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'shipped')


class OrderSOAPTest(TestCase):
    """Test Order SOAP endpoints"""
    
    def setUp(self):
        self.order = Order.objects.create(
            order_number='SOAP-ORD-001',
            customer_name='SOAP Customer',
            customer_email='soap@example.com',
            customer_phone='+1222222222',
            status='pending',
            total_amount=99.99,
            shipping_address='SOAP Address',
            billing_address='SOAP Address'
        )
    
    def test_soap_endpoint_exists(self):
        """Test SOAP endpoint is accessible"""
        response = self.client.get('/orders/soap/')
        self.assertIn(response.status_code, [200, 405])
