from rest_framework import serializers
from .models import InventoryItem, StockMovement


class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMovement
        fields = ['id', 'movement_type', 'quantity', 'reference_number', 'notes', 'created_at']


class InventoryItemSerializer(serializers.ModelSerializer):
    needs_reorder = serializers.ReadOnlyField()
    movements = StockMovementSerializer(many=True, read_only=True)
    
    class Meta:
        model = InventoryItem
        fields = ['id', 'product_sku', 'product_name', 'warehouse_location', 
                  'quantity_available', 'quantity_reserved', 'reorder_level', 
                  'reorder_quantity', 'last_restocked', 'needs_reorder', 
                  'created_at', 'updated_at', 'movements']
        read_only_fields = ['created_at', 'updated_at']


class InventoryItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['product_sku', 'product_name', 'warehouse_location', 
                  'quantity_available', 'quantity_reserved', 'reorder_level', 
                  'reorder_quantity', 'last_restocked']
