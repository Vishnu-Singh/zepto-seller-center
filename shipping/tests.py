from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Shipment


class ShipmentModelTest(TestCase):
    """Test Shipment model"""
    
    def setUp(self):
        self.shipment = Shipment.objects.create(
            tracking_number='TRACK-001',
            order_number='ORD-001',
            carrier='FedEx',
            status='pending',
            shipping_address='123 Main St'
        )
    
    def test_shipment_creation(self):
        """Test shipment is created correctly"""
        self.assertEqual(self.shipment.tracking_number, 'TRACK-001')
        self.assertEqual(self.shipment.status, 'pending')


class ShipmentAPITest(APITestCase):
    """Test Shipment REST API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.shipment = Shipment.objects.create(
            tracking_number='API-TRACK-001',
            order_number='ORD-002',
            carrier='UPS',
            status='in_transit',
            shipping_address='456 Oak Ave'
        )
    
    def test_get_shipments_list(self):
        """Test retrieving list of shipments"""
        url = '/shipping/api/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_track_shipment(self):
        """Test tracking a shipment"""
        url = '/shipping/api/track/?tracking_number=API-TRACK-001'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
