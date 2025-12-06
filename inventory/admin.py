from django.contrib import admin
from .models import InventoryItem, StockMovement


class StockMovementInline(admin.TabularInline):
    model = StockMovement
    extra = 0
    readonly_fields = ['created_at']


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['product_sku', 'product_name', 'warehouse_location', 
                    'quantity_available', 'quantity_reserved', 'needs_reorder']
    list_filter = ['warehouse_location', 'created_at']
    search_fields = ['product_sku', 'product_name']
    readonly_fields = ['created_at', 'updated_at', 'needs_reorder']
    inlines = [StockMovementInline]
    
    fieldsets = (
        ('Product Information', {
            'fields': ('product_sku', 'product_name', 'warehouse_location')
        }),
        ('Stock Levels', {
            'fields': ('quantity_available', 'quantity_reserved', 'reorder_level', 
                      'reorder_quantity', 'last_restocked', 'needs_reorder')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ['inventory_item', 'movement_type', 'quantity', 'reference_number', 'created_at']
    list_filter = ['movement_type', 'created_at']
    search_fields = ['inventory_item__product_sku', 'reference_number']
    readonly_fields = ['created_at']
