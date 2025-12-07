from django.db import models
from django.utils import timezone


class APIVersion(models.Model):
    """Track API versions and changes"""
    version = models.CharField(max_length=20, unique=True, help_text="e.g., v1.0.0")
    release_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    description = models.TextField(help_text="Summary of changes in this version")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-release_date']
        verbose_name = 'API Version'
        verbose_name_plural = 'API Versions'
    
    def __str__(self):
        return f"{self.version} - {self.release_date}"


class APIChange(models.Model):
    """Track individual API changes"""
    
    CHANGE_TYPES = [
        ('feature', 'New Feature'),
        ('enhancement', 'Enhancement'),
        ('bugfix', 'Bug Fix'),
        ('breaking', 'Breaking Change'),
        ('deprecation', 'Deprecation'),
    ]
    
    version = models.ForeignKey(APIVersion, on_delete=models.CASCADE, related_name='changes')
    change_type = models.CharField(max_length=20, choices=CHANGE_TYPES)
    app_name = models.CharField(max_length=50, help_text="e.g., products, orders")
    endpoint = models.CharField(max_length=200, help_text="e.g., /products/api/")
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'API Change'
        verbose_name_plural = 'API Changes'
    
    def __str__(self):
        return f"{self.change_type}: {self.title}"


class SetupGuide(models.Model):
    """Setup and configuration guides"""
    
    GUIDE_TYPES = [
        ('installation', 'Installation'),
        ('configuration', 'Configuration'),
        ('deployment', 'Deployment'),
        ('troubleshooting', 'Troubleshooting'),
    ]
    
    title = models.CharField(max_length=200)
    guide_type = models.CharField(max_length=20, choices=GUIDE_TYPES)
    content = models.TextField(help_text="Markdown supported")
    order = models.IntegerField(default=0, help_text="Display order")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Setup Guide'
        verbose_name_plural = 'Setup Guides'
    
    def __str__(self):
        return self.title
