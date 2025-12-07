from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Product, ProductImage, ProductAttribute


class ProductModelTest(TestCase):
    """Test Product model"""
    
    def setUp(self):
        self.product = Product.objects.create(
            sku='TEST-001',
            name='Test Product',
            description='Test Description',
            price=99.99,
            category='Electronics',
            status='active'
        )
    
    def test_product_creation(self):
        """Test product is created correctly"""
        self.assertEqual(self.product.sku, 'TEST-001')
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 99.99)
        self.assertEqual(self.product.status, 'active')
    
    def test_product_str(self):
        """Test product string representation"""
        self.assertEqual(str(self.product), 'TEST-001 - Test Product')


class ProductAPITest(APITestCase):
    """Test Product REST API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(
            sku='API-001',
            name='API Test Product',
            description='API Test',
            price=149.99,
            category='Books',
            status='active'
        )
    
    def test_get_products_list(self):
        """Test retrieving list of products"""
        url = '/products/api/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)
    
    def test_get_product_detail(self):
        """Test retrieving a single product"""
        url = f'/products/api/{self.product.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sku'], 'API-001')
        self.assertEqual(response.data['name'], 'API Test Product')
    
    def test_create_product(self):
        """Test creating a new product"""
        url = '/products/api/'
        data = {
            'sku': 'NEW-001',
            'name': 'New Product',
            'description': 'New Description',
            'price': 199.99,
            'category': 'Electronics',
            'status': 'active'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.get(sku='NEW-001').name, 'New Product')
    
    def test_update_product(self):
        """Test updating a product"""
        url = f'/products/api/{self.product.id}/'
        data = {
            'sku': 'API-001',
            'name': 'Updated Product Name',
            'description': 'Updated Description',
            'price': 179.99,
            'category': 'Books',
            'status': 'active'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product Name')
    
    def test_delete_product(self):
        """Test deleting a product"""
        url = f'/products/api/{self.product.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
    
    def test_get_product_images(self):
        """Test getting product images"""
        ProductImage.objects.create(
            product=self.product,
            image_url='http://example.com/image1.jpg',
            is_primary=True
        )
        url = f'/products/api/{self.product.id}/images/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_product_attributes(self):
        """Test getting product attributes"""
        ProductAttribute.objects.create(
            product=self.product,
            attribute_name='Color',
            attribute_value='Blue'
        )
        url = f'/products/api/{self.product.id}/attributes/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ProductSOAPTest(TestCase):
    """Test Product SOAP endpoints"""
    
    def setUp(self):
        self.product = Product.objects.create(
            sku='SOAP-001',
            name='SOAP Test Product',
            description='SOAP Test',
            price=99.99,
            category='Electronics',
            status='active'
        )
    
    def test_soap_endpoint_exists(self):
        """Test SOAP endpoint is accessible"""
        response = self.client.get('/products/soap/')
        # SOAP endpoint should return WSDL or accept POST
        self.assertIn(response.status_code, [200, 405])
