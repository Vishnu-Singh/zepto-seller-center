from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product_sku', 'product_name', 'quantity', 'unit_price', 'total_price']
        read_only_fields = ['total_price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'customer_name', 'customer_email', 
                  'customer_phone', 'status', 'total_amount', 'shipping_address', 
                  'billing_address', 'notes', 'created_at', 'updated_at', 'items']
        read_only_fields = ['created_at', 'updated_at']


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_number', 'customer_name', 'customer_email', 
                  'customer_phone', 'status', 'total_amount', 'shipping_address', 
                  'billing_address', 'notes']
