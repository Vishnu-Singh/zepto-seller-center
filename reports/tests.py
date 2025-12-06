from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from datetime import date
from .models import Report


class ReportModelTest(TestCase):
    """Test Report model"""
    
    def setUp(self):
        self.report = Report.objects.create(
            report_id='RPT-001',
            report_type='sales',
            status='pending',
            start_date=date(2024, 1, 1),
            end_date=date(2024, 1, 31)
        )
    
    def test_report_creation(self):
        """Test report is created correctly"""
        self.assertEqual(self.report.report_id, 'RPT-001')
        self.assertEqual(self.report.report_type, 'sales')


class ReportAPITest(APITestCase):
    """Test Report REST API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.report = Report.objects.create(
            report_id='API-RPT-001',
            report_type='inventory',
            status='completed',
            start_date=date(2024, 2, 1),
            end_date=date(2024, 2, 28)
        )
    
    def test_get_reports_list(self):
        """Test retrieving list of reports"""
        url = '/reports/api/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
