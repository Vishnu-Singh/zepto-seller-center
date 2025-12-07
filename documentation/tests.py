from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date
from .models import APIVersion, APIChange, SetupGuide


class APIVersionModelTest(TestCase):
    """Test APIVersion model"""
    
    def setUp(self):
        self.version = APIVersion.objects.create(
            version='v1.0.0',
            release_date=date(2024, 1, 1),
            is_active=True,
            description='Initial release'
        )
    
    def test_version_creation(self):
        """Test version is created correctly"""
        self.assertEqual(self.version.version, 'v1.0.0')
        self.assertTrue(self.version.is_active)
        self.assertEqual(str(self.version), 'v1.0.0 - 2024-01-01')


class APIChangeModelTest(TestCase):
    """Test APIChange model"""
    
    def setUp(self):
        self.version = APIVersion.objects.create(
            version='v1.0.0',
            release_date=date(2024, 1, 1),
            description='Initial release'
        )
        self.change = APIChange.objects.create(
            version=self.version,
            change_type='feature',
            app_name='products',
            endpoint='/products/api/',
            title='New Product API',
            description='Added product management API'
        )
    
    def test_change_creation(self):
        """Test API change is created correctly"""
        self.assertEqual(self.change.change_type, 'feature')
        self.assertEqual(self.change.app_name, 'products')
        self.assertEqual(str(self.change), 'feature: New Product API')


class SetupGuideModelTest(TestCase):
    """Test SetupGuide model"""
    
    def setUp(self):
        self.guide = SetupGuide.objects.create(
            title='Installation Guide',
            guide_type='installation',
            content='Step-by-step installation instructions',
            order=1,
            is_published=True
        )
    
    def test_guide_creation(self):
        """Test setup guide is created correctly"""
        self.assertEqual(self.guide.title, 'Installation Guide')
        self.assertEqual(self.guide.guide_type, 'installation')
        self.assertTrue(self.guide.is_published)


class DocumentationViewsTest(TestCase):
    """Test documentation views"""
    
    def setUp(self):
        self.client = Client()
        self.version = APIVersion.objects.create(
            version='v1.0.0',
            release_date=date(2024, 1, 1),
            is_active=True,
            description='Initial release'
        )
        self.change = APIChange.objects.create(
            version=self.version,
            change_type='feature',
            app_name='products',
            endpoint='/products/api/',
            title='New Product API',
            description='Added product management API'
        )
        self.guide = SetupGuide.objects.create(
            title='Quick Start',
            guide_type='installation',
            content='Quick start guide',
            is_published=True
        )
    
    def test_documentation_home(self):
        """Test documentation home page"""
        response = self.client.get(reverse('documentation:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Zepto Seller Center')
    
    def test_api_reference(self):
        """Test API reference page"""
        response = self.client.get(reverse('documentation:api-reference'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'API Reference')
    
    def test_setup_guide(self):
        """Test setup guide page"""
        response = self.client.get(reverse('documentation:setup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Setup & Installation')
    
    def test_changelog(self):
        """Test changelog page"""
        response = self.client.get(reverse('documentation:changelog'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Changelog')


class DocumentationAPITest(APITestCase):
    """Test documentation API endpoints"""
    
    def setUp(self):
        self.version = APIVersion.objects.create(
            version='v1.0.0',
            release_date=date(2024, 1, 1),
            is_active=True,
            description='Initial release'
        )
        self.change = APIChange.objects.create(
            version=self.version,
            change_type='feature',
            app_name='products',
            endpoint='/products/api/',
            title='New Product API',
            description='Added product management API'
        )
    
    def test_api_versions_endpoint(self):
        """Test API versions endpoint"""
        url = reverse('documentation:api-versions')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['version'], 'v1.0.0')
    
    def test_api_changes_endpoint(self):
        """Test API changes endpoint"""
        url = reverse('documentation:api-changes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_api_changes_filter_by_version(self):
        """Test filtering API changes by version"""
        url = reverse('documentation:api-changes') + '?version=v1.0.0'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for change in response.data:
            self.assertEqual(change['version'], 'v1.0.0')

