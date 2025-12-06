from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import InventoryItem, StockMovement


class InventoryModelTest(TestCase):
    """Test Inventory model"""
    
    def setUp(self):
        self.item = InventoryItem.objects.create(
            product_sku='INV-001',
            product_name='Test Product',
            warehouse_location='Warehouse A',
            quantity_available=100,
            reorder_level=20
        )
    
    def test_inventory_creation(self):
        """Test inventory item is created correctly"""
        self.assertEqual(self.item.product_sku, 'INV-001')
        self.assertEqual(self.item.quantity_available, 100)
    
    def test_needs_reorder_property(self):
        """Test needs_reorder property"""
        self.assertFalse(self.item.needs_reorder)
        self.item.quantity_available = 15
        self.item.save()
        self.assertTrue(self.item.needs_reorder)


class InventoryAPITest(APITestCase):
    """Test Inventory REST API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.item = InventoryItem.objects.create(
            product_sku='API-INV-001',
            product_name='API Test Product',
            warehouse_location='Warehouse B',
            quantity_available=50
        )
    
    def test_get_inventory_list(self):
        """Test retrieving list of inventory items"""
        url = '/inventory/api/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_inventory_detail(self):
        """Test retrieving a single inventory item"""
        url = f'/inventory/api/{self.item.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product_sku'], 'API-INV-001')
    
    def test_adjust_stock(self):
        """Test adjusting stock quantity"""
        url = f'/inventory/api/{self.item.id}/adjust_stock/'
        data = {
            'movement_type': 'in',
            'quantity': 25,
            'notes': 'Restocking'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.quantity_available, 75)


class InventorySOAPTest(TestCase):
    """Test Inventory SOAP endpoints"""
    
    def setUp(self):
        self.item = InventoryItem.objects.create(
            product_sku='SOAP-INV-001',
            product_name='SOAP Product',
            warehouse_location='Warehouse C',
            quantity_available=30
        )
    
    def test_soap_endpoint_exists(self):
        """Test SOAP endpoint is accessible"""
        response = self.client.get('/inventory/soap/')
        self.assertIn(response.status_code, [200, 405])
