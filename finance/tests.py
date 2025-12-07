from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Transaction, Payout


class TransactionModelTest(TestCase):
    """Test Transaction model"""
    
    def setUp(self):
        self.transaction = Transaction.objects.create(
            transaction_id='TXN-001',
            transaction_type='sale',
            amount=99.99
        )
    
    def test_transaction_creation(self):
        """Test transaction is created correctly"""
        self.assertEqual(self.transaction.transaction_id, 'TXN-001')
        self.assertEqual(self.transaction.amount, 99.99)


class TransactionAPITest(APITestCase):
    """Test Transaction REST API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.transaction = Transaction.objects.create(
            transaction_id='API-TXN-001',
            transaction_type='sale',
            amount=149.99
        )
    
    def test_get_transactions_list(self):
        """Test retrieving list of transactions"""
        url = '/finance/api/transactions/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
