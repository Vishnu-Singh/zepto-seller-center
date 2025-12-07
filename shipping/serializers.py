from rest_framework import serializers
from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['id', 'tracking_number', 'order_number', 'carrier', 'status', 
                  'shipping_address', 'estimated_delivery', 'actual_delivery', 
                  'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
