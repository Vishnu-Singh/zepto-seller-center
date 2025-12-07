from django.db import models


class InventoryItem(models.Model):
    """Inventory item model"""
    
    product_sku = models.CharField(max_length=100, unique=True, db_index=True)
    product_name = models.CharField(max_length=255)
    warehouse_location = models.CharField(max_length=100)
    quantity_available = models.IntegerField(default=0)
    quantity_reserved = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=10)
    reorder_quantity = models.IntegerField(default=50)
    last_restocked = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['product_sku']
        verbose_name = 'Inventory Item'
        verbose_name_plural = 'Inventory Items'
    
    def __str__(self):
        return f"{self.product_sku} - {self.quantity_available} available"
    
    @property
    def needs_reorder(self):
        """Check if inventory needs reorder"""
        return self.quantity_available <= self.reorder_level


class StockMovement(models.Model):
    """Track stock movements"""
    
    MOVEMENT_TYPES = [
        ('in', 'Stock In'),
        ('out', 'Stock Out'),
        ('adjustment', 'Adjustment'),
        ('return', 'Return'),
    ]
    
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='movements')
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPES)
    quantity = models.IntegerField()
    reference_number = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Stock Movement'
        verbose_name_plural = 'Stock Movements'
    
    def __str__(self):
        return f"{self.movement_type} - {self.quantity} units of {self.inventory_item.product_sku}"
